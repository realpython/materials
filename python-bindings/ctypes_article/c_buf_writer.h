#ifndef __C_BUF_WRITER_H__
#define __C_BUF_WRITER_H__

/* Example library for serializing (and deserializing) several data types and
 * data structures into a memory buffer in C.
 * Used to demonstrate different features of ctypes in Python.
 */

int getVersionMajor(void);
int getVersionMinor(void);
char* returnVersionString(void);
void freeVersionString(char*);
void fillInVersionString(char** version);



#endif // __C_BUF_WRITER_H__
