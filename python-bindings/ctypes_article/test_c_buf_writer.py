#!/usr/bin/env python
import ctypes


def wrap_function(lib, funcname, restype, argtypes):
    ''' Simplify wrapping ctypes functions '''
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func


# struct Point { }
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

    # def __init__(self, *tpl):
        # self.x, self.y = tpl

    def __repr__(self):
        return '({0}, {1})'.format(self.x, self.y)

class ByRefArg(object):
    '''Just like a POINTER but accept an argument and pass it byref'''
    def __init__(self, atype):
        self.atype = atype

    def from_param(self, param):
        return ctypes.byref(self.atype(*param))


if __name__ == '__main__':
    # load the shared library into c types.  NOTE: don't use a hard-coded path
    # in production code, please
    libc = ctypes.CDLL("./libpoint.so")

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
                                      [ctypes.POINTER(Point)])
    a = Point(5, 6)
    # a = (5, 6)
    print("Point in python is", a)
    move_point_by_ref(a)
    print("Point in python is", a)
    print()



    sp = wrap_function(libc, "SetParams", ctypes.c_uint, [ctypes.c_uint,
                                                          ctypes.POINTER(ctypes.c_char_p)])
    def setParameters(strParamList):
        numParams    = len(strParamList)
        strArrayType = ctypes.c_char_p * numParams
        strArray     = strArrayType()
        for i, param in enumerate(strParamList):
            # NOte: this copies each param to go from string to bytes. Bytes are
            # required for ctypes
            strArray[i] = param.encode()
        sp(numParams, strArray)
        print("in python", strArray[1].decode('utf-8'))

    setParameters(['abc','def','ghi'])

    ###########################################################################
    # https://stackoverflow.com/questions/28283058/python-ctypes-wrong-data-when-reading-structure-passed-as-parameter
    class CieLxy(ctypes.Structure):
        _fields_ = [("L", ctypes.c_double),
                    ("x", ctypes.c_double),
                    ("y", ctypes.c_double)]


    class I1VpCal(ctypes.Structure):
        _fields_ = [("ledCur", ctypes.c_int * 3),
                    ("targetCie", CieLxy),
                    ("modelCie", CieLxy),
                    ("measuredCie", CieLxy)]


    class I1CalArray(ctypes.Structure):
        _fields_ = [("i1CalArray", 8*(7*I1VpCal))]


    Foo = wrap_function(libc, "foo", ctypes.c_int,
                        [ctypes.POINTER(I1CalArray)])
                        # [ctypes.c_void_p])

    def foo( i1CalArray):
        Foo(ctypes.byref(i1CalArray))

    i1CalArray_struct = I1CalArray()
    i1CalArray = i1CalArray_struct.i1CalArray

    for i in range(8):
        for j in range(7):
            temp = i1CalArray[i][j].ledCur[0] = i+j
            temp = i1CalArray[i][j].measuredCie.L = float(i+j)

    foo(i1CalArray_struct)
