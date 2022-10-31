/*******************************************************************************
Calculate a complement color from a supplied 24bit color.
Copyright 2022. thomas.cherry@gmail.com
*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

char* as_color(int color[], char* text) {
  int r = color[0];
  int g = color[1];
  int b = color[2];
  char *out = (char*) malloc(80*sizeof(char));

  sprintf(out, "\033[38;2;%d;%d;%dm%s\033[00m", r, g, b, text);
  return out;
} 

char* expand_color(int color[]) {
  char* box = as_color(color, "\uEE03\uEE04\uEE05");
  char *out = (char*) malloc(80*sizeof(char));
  sprintf (out, "%s %d,%d,%d", box, color[0], color[1], color[2]);
  return out;
}

int ask_for_number(char* name) {
  int value = -1;
  while (value<0 || 255 < value) {
    printf("Enter a number for %s: ", name);
    scanf("%d",&value);
  }
  return value;
}

int* ask_for_numbers() {
  int red = ask_for_number("red");
  int green = ask_for_number("green");
  int blue = ask_for_number("blue");
  
  static int ans[3];
  ans[0] = red;
  ans[1] = green;
  ans[2] = blue;

  return ans;
}

int* find_compliment(int colors[]) {
  static int ans[3];
  ans[0] = 255 - colors[0];
  ans[1] = 255 - colors[1];
  ans[2] = 255 - colors[2];
  return ans;
}

int main() {
  printf ("Find a compliment color from a given color:\n");
  int* colors = ask_for_numbers();
  int* compliment = find_compliment(colors);
  
  printf("%s -> %s\n", expand_color(colors), expand_color(compliment));
}
