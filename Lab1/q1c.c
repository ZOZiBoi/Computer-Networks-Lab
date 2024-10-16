#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int is_non_alphabet_word(const char *word) {
    for (int i = 0; word[i] != '\0'; i++) {
        if (isalpha(word[i])) {
            return 0;
        }
    }
    return 1;
}

int main() {
    FILE *rp = fopen("Input File.txt", "r");
    FILE *wp = fopen("Output File.txt", "w+");

    if (rp == NULL) {
        printf("file can't be opened \n");
        return EXIT_FAILURE;
    }

    if (wp == NULL) {
        printf("output file can't be created \n");
        fclose(rp);
        return EXIT_FAILURE;
    }

    char word[50];
    printf("Writing non-alphabet words from input file to \"Output_File.txt\"\n");

    while (fscanf(rp, "%49s", word) == 1) {
        if (is_non_alphabet_word(word)) {
            fprintf(wp, "%s\n", word);
            printf("%s\n", word);
        }
    }

    fclose(wp);
    fclose(rp);

    return 0;
}