#include <stdio.h>
#include "c_buf_writer.h"


/* unsigned int SetParams(unsigned int count, const char **params) { */
unsigned int SetParams(unsigned int count, char **params) {
    printf("In C got count %d\n", count);
    printf("First: %s\n", params[0]);
    printf("Second: %s\n", params[1]);
    params[1][1] = 'x';
    printf("newSecond: %s\n", params[1]);
    return(count+32);
}

////////////////////////////////////////////////////////////////////////////////
typedef struct {
    double L, x, y;
} CieLxy;


typedef struct {
    int ledCur[3];
    CieLxy targetCie, modelCie, measuredCie;
} I1VpCal;


typedef struct {
    I1VpCal i1CalArray[8][7];
} I1CalArray;

int foo(I1CalArray* p_i1CalArray) {
    int i, j;

    for (i=0; i<8; i++) {
        for (j=0; j<7; j++) {
            printf("in dll, i1CalArray[%d][%d].ledCur[0] = %d\n",
                   i, j, p_i1CalArray->i1CalArray[i][j].ledCur[0]);
            printf("in dll, i1CalArray[%d][%d].measuredCie.L = %f\n",
                   i, j, p_i1CalArray->i1CalArray[i][j].measuredCie.L);
        }
    }
    return 10;
}
