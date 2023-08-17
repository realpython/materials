// parallel/parallel.c

#include <math.h>

void process(
  unsigned char* pixels,
  int length,
  int offset,
  float ev,
  float gamma)
{
    unsigned char lookup_table[256];

    for (int i = 0; i < 256; i++) {
        float value = powf((i / 255.0f * ev), gamma) * 255.0f;
        lookup_table[i] = (unsigned char) fmin(fmax(0.0f, value), 255.0f);
    }

    for (int i = offset; i < length; i += 3) {
        pixels[i] = lookup_table[pixels[i]];
    }
}
