#include <stdio.h>

int main() {
    int x;
    while (x = fgetc(stdin)) {
        if (x == EOF)
            break;
        putchar(x);
    }
    return 0;
}
