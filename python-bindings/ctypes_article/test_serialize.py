#!/usr/bin/env python3
import ctypes as ct
from enum import Enum

def wrap_function(lib, funcname, restype, argtypes):
    ''' Simplify wrapping ctypes functions '''
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

# Replicate the enum from buf_serialize.h
class SerialType(Enum):
    UINT32_TYPE = 0
    UINT8_TYPE = 1
    FLOAT_TYPE = 2
    DOUBLE_TYPE = 3
    STRING_TYPE = 4
    STRING_LIST_TYPE = 5

def wrap_peek_function(libc):
    peekNextType = wrap_function(libc, "peekNextType", ct.c_bool,
                                 [ct.c_void_p, ct.POINTER(ct.c_int)])
    def internal_peek(serial):
        """ Calls the peekNextType function and converts the type value to a
            SerialType enum value. """
        type_ = ct.c_int()
        peekNextType(serial, ct.byref(type_))
        return SerialType(type_.value)

    return internal_peek



class ByRefArg():
    '''Just like a POINTER but accept an argument and pass it byref'''
    def __init__(self, atype):
        self.atype = atype

    def from_param(self, param):
        return ct.byref(self.atype(*param))

def show_intialize(libc):
    initialize_serializer = wrap_function(libc, "initializeSerializer", ct.c_void_p, [])
    free_serializer = wrap_function(libc, "freeSerializer", None, [ct.c_void_p])

    serial = initialize_serializer()
    # Serialize objects here
    free_serializer(serial)

def test_int(libc):
    initialize_serializer = wrap_function(libc, "initializeSerializer", ct.c_void_p, [])
    free_serializer = wrap_function(libc, "freeSerializer", None, [ct.c_void_p])
    serializeUInt8 = wrap_function(libc, "serializeUInt8", None,
                                   [ct.c_void_p, ct.c_ubyte])
    getNextValueUInt8 = wrap_function(libc, "getNextValueUInt8", ct.c_bool,
                                 [ct.c_void_p, ct.POINTER(ct.c_ubyte)])
    peekNextType = wrap_peek_function(libc)

    serial = initialize_serializer()

    serializeUInt8(serial, 18)

    # see what the type of the next item is
    # type_ = ct.c_int()
    # print("before: ", type_.value)
    # peekNextType(serial, ct.byref(type_))
    # print("after: ", type_, SerialType.UINT8_TYPE.value)
    nextType = peekNextType(serial)

    # type_ = ct.c_int(1)

    # JHA fix to use c enum values here
    # if type_.value == SerialType.UINT8_TYPE.value:
    if nextType == SerialType.UINT8_TYPE:
        value = ct.c_ubyte()
        print("getting uint8 - type 1")
        res = getNextValueUInt8(serial, ct.byref(value))
        print(f"Got value: {value.value}")
        print(f"Got res: {res}")
    else:
        print("bad type???", type_)


    free_serializer(serial)


if __name__ == '__main__':
    # load the shared library into c types.  NOTE: don't use a hard-coded path
    # in production code, please
    libc = ct.CDLL("./libbuf_serialize.so")
    test_int(libc)

    """
    initialize_serializer = wrap_function(libc, "initializeSerializer", ct.c_void_p, [])
    free_serializer = wrap_function(libc, "freeSerializer", None, [ct.c_void_p])

    serializeDouble = wrap_function(libc, "serializeDouble", None,
                                   [ct.c_void_p, ct.c_double])
    getNextValueDouble = wrap_function(libc, "getNextValueDouble", ct.c_bool,
                                 [ct.c_void_p, ct.POINTER(ct.c_double)])


    peekNextType = wrap_function(libc, "peekNextType", ct.c_bool,
                                 [ct.c_void_p, ct.POINTER(ct.c_int)])
    ############################################################
    # int8 and double
    ############################################################
    serializeUInt8 = wrap_function(libc, "serializeUInt8", None,
                                   [ct.c_void_p, ct.c_ubyte])
    getNextValueUInt8 = wrap_function(libc, "getNextValueUInt8", ct.c_bool,
                                 [ct.c_void_p, ct.POINTER(ct.c_ubyte)])
    serializeDouble = wrap_function(libc, "serializeDouble", None,
                                   [ct.c_void_p, ct.c_double])
    getNextValueDouble = wrap_function(libc, "getNextValueDouble", ct.c_bool,
                                 [ct.c_void_p, ct.POINTER(ct.c_double)])
    serial = initialize_serializer()
    serializeUInt8(serial, 18)
    serializeDouble(serial, 1.234)
    type_ = ct.c_int()
    print("before: ", type_)
    peekNextType(serial, ct.byref(type_))
    print("after: ", type_)

    # JHA fix to use c enum values here
    if type_.value == 1:
        value = ct.c_ubyte()
        print("getting uint8 - type 1")
        res = getNextValueUInt8(serial, ct.byref(value))
        print(f"Got value: {value.value}")
        print(f"Got res: {res}")
    else:
        print("bad type???", type_)

    value = ct.c_double(0)
    res = getNextValueDouble(serial, ct.byref(value))
    print(f"Got value: {value.value}")
    print(f"Got res: {res}")


    ############################################################
    # string
    ############################################################
    serializeString = wrap_function(libc, "serializeString", None,
                                   [ct.c_void_p, ct.c_char_p])
    getNextValueString = wrap_function(libc, "getNextValueString", ct.c_bool,
                                 [ct.c_void_p, ct.POINTER(ct.c_char_p)])
    freeString = wrap_function(libc, "freeString", None, [ct.c_char_p])

    aaa = "Real Python Demo"
    # serializeString(serial, ct.c_char_p("fred"))
    serializeString(serial, b"Real Python Demo")
    value = ct.c_char_p()
    res = getNextValueString(serial, ct.byref(value))
    print(f"Got value: {value.value.decode('utf-8')}")
    print(f"Got res: {res}")
    freeString(value)



    ############################################################
    # List of strings
    ############################################################
    getNextValueStringList = wrap_function(libc, "getNextValueStringList",
                                           ct.c_bool,
                                           [ct.c_void_p, ct.POINTER(ct.c_ubyte),
                                            ct.POINTER(ct.POINTER(ct.c_char_p))])
    freeStringList = wrap_function(libc, "freeStringList", None,
                                    [ct.c_ubyte, ct.POINTER(ct.c_char_p)])

    def serializeStringList(strParamList):
        serializeString = wrap_function(libc, "serializeStringList", None,
                                        [ct.c_void_p, ct.c_uint, ct.POINTER(ct.c_char_p)])
        numParams    = len(strParamList)
        strArrayType = ct.c_char_p * numParams
        strArray     = strArrayType()
        for i, param in enumerate(strParamList):
            # NOte: this copies each param to go from string to bytes. Bytes are
            # required for ct
            strArray[i] = param.encode()
        serializeString(serial, numParams, strArray)

    serializeStringList(['abc','def','ghi'])
    # serializeStringList(['this','is', 'a','longer', 'list'])


    # JHA TODO in article write up difference between ct.POINTER which creates
    # a type and ct.pointer which creates a pointer to a storage location
    count = ct.c_ubyte()
    value = ct.pointer(ct.c_char_p())
    res = getNextValueStringList(serial, ct.byref(count), ct.byref(value))
    print("JIMA", value.contents)
    for x in dir(value.contents):
        print(f"\t{x}")
    # print(value.contents.value.decode('utf-8'))
    print(value.contents.value)
    print("COUNT", count.value)


    ############################################################
    # C struct
    ############################################################


    ############################################################
    # Nested C struct
    ############################################################

    ############################################################
    # Python Class
    ############################################################

    ############################################################
    # Nested Python Class
    ############################################################

    free_serializer(serial)
    """

################################################################################
# JHA TODO remove this after integrating these ideas into code

# struct Point { }
class Point(ct.Structure):
    _fields_ = [('x', ct.c_int), ('y', ct.c_int)]

    # def __init__(self, *tpl):
        # self.x, self.y = tpl

    def __repr__(self):
        return '({0}, {1})'.format(self.x, self.y)


def old_main():
    # load the shared library into c types.  NOTE: don't use a hard-coded path
    # in production code, please
    libc = ct.CDLL("./libpoint.so")

    ###########################################################################
    print("Pass by byref")
    move_point_by_ref = wrap_function(libc, 'move_point_by_ref', None,
                                      [ByRefArg(Point)])
    a = (5, 6)
    print("Point in python is", a)
    move_point_by_ref(a)
    print("Point in python is", a)
    print()

    ###########################################################################
    # print("Pass a struct into C")
    # show_point = wrap_function(libc, 'show_point', None, [Point])
    # a = Point(1, 2)
    # print("Point in python is", a)
    # show_point(a)
    # print()

    ###########################################################################
    # print("Pass by value")
    # move_point = wrap_function(libc, 'move_point', None, [Point])
    # a = Point(5, 6)
    # print("Point in python is", a)
    # move_point(a)
    # print("Point in python is", a)
    # print()

    ###########################################################################
    print("Pass by reference")
    move_point_by_ref = wrap_function(libc, 'move_point_by_ref', None,
                                      [ct.POINTER(Point)])
    a = Point(5, 6)
    # a = (5, 6)
    print("Point in python is", a)
    move_point_by_ref(a)
    print("Point in python is", a)
    print()



    ###########################################################################
    # https://stackoverflow.com/questions/28283058/python-ct-wrong-data-when-reading-structure-passed-as-parameter
    class CieLxy(ct.Structure):
        _fields_ = [("L", ct.c_double),
                    ("x", ct.c_double),
                    ("y", ct.c_double)]


    class I1VpCal(ct.Structure):
        _fields_ = [("ledCur", ct.c_int * 3),
                    ("targetCie", CieLxy),
                    ("modelCie", CieLxy),
                    ("measuredCie", CieLxy)]


    class I1CalArray(ct.Structure):
        _fields_ = [("i1CalArray", 8*(7*I1VpCal))]


    Foo = wrap_function(libc, "foo", ct.c_int,
                        [ct.POINTER(I1CalArray)])
                        # [ct.c_void_p])

    def foo( i1CalArray):
        Foo(ct.byref(i1CalArray))

    i1CalArray_struct = I1CalArray()
    i1CalArray = i1CalArray_struct.i1CalArray

    for i in range(8):
        for j in range(7):
            temp = i1CalArray[i][j].ledCur[0] = i+j
            temp = i1CalArray[i][j].measuredCie.L = float(i+j)

    foo(i1CalArray_struct)
