#include <stdio.h>

#include "SkPaint.h"
#include "SkString.h"

int main(int argc, char** argv) {
  SkPaint paint;
  paint.setColor(SK_ColorRED);

  SkString str;
  paint.toString(&str);

  fprintf(stdout, "%s\n", str.c_str());

  return 0;
}