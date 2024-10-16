#include <stdlib.h>
#include <stdio.h>

int main() {
    FILE *rp;
    rp = fopen("Input File.txt", "r");
    FILE *wp;
    wp = fopen("Output File.txt", "w+");    

    if (rp == NULL) {
        printf("file can't be opened \n");
        return EXIT_FAILURE;
    }

    char ch;
    printf("Writing numbers from input file to \"Output File.txt\"\n");

    while ((ch = fgetc(rp)) != EOF) {
        if (ch >= '0' && ch <= '9') {
            fputc(ch, wp);
        }
    }

    fclose(wp);
    fclose(rp);
}