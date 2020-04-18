#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include "buf_serialize.h"

typedef struct {
    size_t next_to_write;
    size_t next_to_read;
    size_t bytes_allocated;
    unsigned char* buf;
} Serializer;

void* initializeSerializer(void) {
    Serializer* serial = (Serializer*)calloc(sizeof(Serializer), 1);
    serial->next_to_write = 0;
    serial->next_to_read = 0;
    /* Start with a 1K buffer size. We'll need to realloc if this grows too
     * large.  Might be able to implement for article without that logic. */
    serial->bytes_allocated = 1024;
    serial->buf = (unsigned char*)calloc(1, serial->bytes_allocated);
    printf("In %s: allocated serializer %p with buffer %p\n", __func__, serial, serial->buf);
    return serial;
}

void freeSerializer(void* vser) {
    Serializer* serial = (Serializer*)vser;

    if (serial != NULL) {
        printf("In %s: freeing serializer %p with buffer %p\n", __func__, serial, serial->buf);
        free(serial->buf);
        free(serial);
    }
}

bool internalPeekNextType(void* vser, SERIAL_TYPE* type, bool inc_ptr) {
    Serializer* serial = (Serializer*)vser;

    if (serial != NULL) {
        *type = serial->buf[serial->next_to_read];
        if (inc_ptr) {
            serial->next_to_read++;
        }
        return true;
    }
    return false;
}

bool peekNextType(void* vser, SERIAL_TYPE* type) {
    return internalPeekNextType(vser, type, false);
}

bool readNextType(void* vser, SERIAL_TYPE* type) {
    return internalPeekNextType(vser, type, true);
}

////////////////////////////////////////////////////////////////////////////////
void serializeUInt8(void* vser, uint8_t value) {
    Serializer* serial = (Serializer*)vser;
    printf("Serializing UInt8 %d\n", value);

    if (serial != NULL) {
        serial->buf[serial->next_to_write++] = UINT8_TYPE;
        serial->buf[serial->next_to_write++] = value;
    }
}

bool getNextValueUInt8(void* vser, uint8_t* value) {
    Serializer* serial = (Serializer*)vser;

    if (serial != NULL) {
        SERIAL_TYPE type = END_OF_TYPES;
        if (!readNextType(vser, &type) ||
           (type != UINT8_TYPE)) {
            return false;
        }
        *value = serial->buf[serial->next_to_read++];
        return true;
    }
    return false;

}

////////////////////////////////////////////////////////////////////////////////
void serializeDouble(void* vser, double value) {
    Serializer* serial = (Serializer*)vser;
    printf("Serializing Double %f\n", value);

    if (serial != NULL) {
        serial->buf[serial->next_to_write++] = DOUBLE_TYPE;
        uint8_t* ptr = (uint8_t*)&value;
        for (int ii = 0; ii < sizeof(double); ++ii) {
            serial->buf[serial->next_to_write++] = ptr[ii];
        }
    }
}

// https://docs.python.org/3/tutorial/floatingpoint.html
// Need to describe that python only uses doubles and floats can get in-exact
// values when getting boosted up to that size.
//

bool getNextValueDouble(void* vser, double* value) {
    Serializer* serial = (Serializer*)vser;

    if (serial != NULL) {
        SERIAL_TYPE type = END_OF_TYPES;
        if (!readNextType(vser, &type) ||
           (type != DOUBLE_TYPE)) {
            return false;
        }
        uint8_t* ptr = (uint8_t*)value;
        for (int ii = 0; ii < sizeof(double); ++ii) {
            ptr[ii] = serial->buf[serial->next_to_read++];
        }

        return true;
    }
    return false;
}

void serializeString(void* vser, char* value) {
    Serializer* serial = (Serializer*)vser;

    if (serial != NULL) {
        serial->buf[serial->next_to_write++] = STRING_TYPE;
        /* LIMITATION: only able to store strings < 255 bytes in length */
        uint8_t length = (uint8_t)strlen(value);
        printf("Serializing String '%s' of length %u\n", value, length);
        serial->buf[serial->next_to_write++] = length;
        // JHA TODO memcpy, sheesh
        for (int ii = 0; ii < length; ++ii) {
            serial->buf[serial->next_to_write++] = (uint8_t)value[ii];
        }
    }
}

bool getNextValueString(void* vser, char** value) {
    /* NOTE: caller is returned memory that is allocated in C.  Call must
     * return this value to be freed in C. */
    Serializer* serial = (Serializer*)vser;

    if (serial != NULL) {
        SERIAL_TYPE type = END_OF_TYPES;
        if (!readNextType(vser, &type) ||
           (type != STRING_TYPE)) {
            return false;
        }
        uint8_t length = serial->buf[serial->next_to_read++];
        printf("length is %d\n", length);
        uint8_t* ptr = (uint8_t*)malloc(length * sizeof(uint8_t));
        // JHA TODO MEMCPY!!!!!
        for (int ii = 0; ii < length; ++ii) {
            ptr[ii] = serial->buf[serial->next_to_read++];
        }
        *value = (char*)ptr;
        return true;
    }
    return false;
}

void freeString(char* ptr) {
    printf("Freeing string ptr %p\n", ptr);
    free(ptr);
}

void serializeStringList(void* vser, uint8_t count, char** values) {
    Serializer* serial = (Serializer*)vser;
    printf("Serializing String List of length %u\n", count);

    if (serial != NULL) {
        serial->buf[serial->next_to_write++] = STRING_LIST_TYPE;
        serializeUInt8(vser, count);
        for (int ii = 0; ii < count; ++ii) {
            serializeString(vser, values[ii]);
        }
    }
}

bool getNextValueStringList(void* vser, uint8_t* count, char*** values) {
    /* NOTE: caller is returned memory that is allocated in C.  Call must
     * return this value to be freed in C. */
    if (vser != NULL) {
        SERIAL_TYPE type = END_OF_TYPES;
        if (!readNextType(vser, &type) ||
           (type != STRING_LIST_TYPE)) {
            return false;
        }
        uint8_t count = 0;
        if (!getNextValueUInt8(vser, &count)) {
            return false;
        }

        printf("number of strings in list is %d\n", count);
        char** ptr = (char**)malloc(count * sizeof(char*));
        for (int ii = 0; ii < count; ++ii) {
            if (!getNextValueString(vser, &ptr[ii])) {
                free(ptr);
                return false;
            }
        }
        *values = ptr;
        return true;
    }
    return false;
}

void freeStringList(uint8_t count, char **values) {
}
////////////////////////////////////////////////////////////////////////////////
//JHA TODO remove this after integrating these ideas into code


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
