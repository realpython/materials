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

static int greeter_exec(PyObject *module) {
    return 0;
}

static PyModuleDef_Slot greeter_slots[] = {
    {Py_mod_exec, greeter_exec},
    {Py_mod_gil, Py_MOD_GIL_NOT_USED},
    {0, NULL}
};

static struct PyModuleDef greeter = {
    PyModuleDef_HEAD_INIT,
    "greeter",
    "Greeting module",
    0,
    greeter_methods,
    greeter_slots,
};

PyMODINIT_FUNC PyInit_greeter(void) {
    return PyModuleDef_Init(&greeter);
}
