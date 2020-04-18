#include <stdio.h>

double returnDouble(int int_param) {
    double return_value = 12.34;
    printf("    In C:      returnDouble: %.2f\n", return_value);
    return return_value;
}


double multiply(int int_param, double double_param) {
    double return_value = int_param * double_param;
    printf("    In C:      multiply: int: %d double %.1f returning  %.1f\n",
            int_param, double_param, return_value);
    return return_value;
}


