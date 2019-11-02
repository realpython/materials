#include <pybind11/pybind11.h>
#include <cpp_function.hpp>


PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("cpp_function", &cpp_mult, "A function which multiplies two numbers");
}

