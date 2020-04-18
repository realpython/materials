#ifndef __C_BUF_WRITER_H__
#define __C_BUF_WRITER_H__

/* Example library for serializing (and deserializing) several data types and
 * data structures into a memory buffer in C.
 * Used to demonstrate different features of ctypes in Python.
 */
typedef enum {
    UINT32_TYPE = 0,
    UINT8_TYPE = 1,
    FLOAT_TYPE = 2,
    DOUBLE_TYPE = 3,
    STRING_TYPE = 4,
    STRING_LIST_TYPE = 5,
    END_OF_TYPES
} SERIAL_TYPE;

void* initializeSerializer(void);
void freeSerializer(void* vser);

bool peekNextType(void* vser, SERIAL_TYPE* type);
bool readNextType(void* vser, SERIAL_TYPE* type);

void serializeUInt8(void* vser, uint8_t value);
bool getNextValueUInt8(void* vser, uint8_t* value);

void serializeDouble(void* vser, double value);
bool getNextValueDouble(void* vser, double* value);

void serializeString(void* vser, char* value);
bool getNextValueString(void* vser, char** value);
void freeString(char* ptr);

void serializeStringList(void* vser, uint8_t count, char **values);
bool getNextValueStringList(void* vser, uint8_t* count, char ***values);
void freeStringList(uint8_t count, char **values);
#endif // __C_BUF_WRITER_H__
