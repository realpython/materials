#include <Python.h>

static PyObject* greeter_greet(PyObject* self, PyObject* args) {
    const char *name = "anonymous";

    if (!PyArg_ParseTuple(args, "|s", &name)) {
        return NULL;
    }

    return PyUnicode_FromFormat("Hello, %s!", name);
}

static PyMethodDef greeter_methods[] = {
    {"greet", greeter_greet, METH_VARARGS, "Greet someone"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef greeter = {
    PyModuleDef_HEAD_INIT,
    "greeter",
    "Greeting module",
    -1,
    greeter_methods
};

PyMODINIT_FUNC PyInit_greeter(void) {
    return PyModule_Create(&greeter);
}
