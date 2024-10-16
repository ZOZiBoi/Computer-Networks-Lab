#include <stdlib.h>
#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("Input File.txt", "r");

    if (fp == NULL) {
        printf("file can't be opened \n");
        return EXIT_FAILURE;
    }

    char ch;
    printf("Content of the file are:-: \n");

    // Printing what is written in file character by character using loop.
    while ((ch = fgetc(fp)) != EOF) {
        printf("%c", ch);
    }

    fclose(fp);
}