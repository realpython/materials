""" Example cython interface definition """

cdef extern from "cppmult.hpp":
    float cppmult(int int_param, float float_param)

def pymult( ip, fp ):
    return cppmult( ip, fp )
