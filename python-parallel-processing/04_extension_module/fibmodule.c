#include <Python.h>

int fib(int n) {
    return n < 2 ? n : fib(n - 2) + fib(n - 1);
}

static PyObject* fibmodule_fib(PyObject* self, PyObject* args) {
    int n, result;

    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
    result = fib(n);
    Py_END_ALLOW_THREADS

    return Py_BuildValue("i", result);
}

static PyMethodDef fib_methods[] = {
    {"fib", fibmodule_fib, METH_VARARGS, "Calculate the nth Fibonacci"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fibmodule = {
    PyModuleDef_HEAD_INIT,
    "fibmodule",
    "Efficient Fibonacci number calculator",
    -1,
    fib_methods
};

PyMODINIT_FUNC PyInit_fibmodule(void) {
    return PyModule_Create(&fibmodule);
}

