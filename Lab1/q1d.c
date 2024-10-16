#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>

bool contains_vowel(const char *word) {
    const char *vowels = "aeiouAEIOU";
    for (int i = 0; word[i] != '\0'; i++) {
        if (strchr(vowels, word[i])) {
            return true; 
        }
    }
    return false; 
}

bool is_alphabetic(const char *word) {
    for (int i = 0; word[i] != '\0'; i++) {
        if (!isalpha(word[i])) {
            return false; 
        }
    }
    return true;
}

void invert_word(char *word) {
    int len = strlen(word);
    for (int i = 0; i < len / 2; i++) {
        char temp = word[i];
        word[i] = word[len - 1 - i];
        word[len - 1 - i] = temp;
    }
}

int main() {
    FILE *rp = fopen("Input File.txt", "r");
    FILE *wp = fopen("Output File.txt", "w");

    if (rp == NULL) {
        printf("input file can't be opened \n");
        return EXIT_FAILURE;
    }

    if (wp == NULL) {
        printf("output file can't be created \n");
        fclose(rp);
        return EXIT_FAILURE;
    }

    char word[50];
    printf("Writing inverted words from input file to \"Output_File.txt\"\n");

    while (fscanf(rp, "%49s", word) == 1) {
        if (is_alphabetic(word)) {
            if (contains_vowel(word)) {
                fprintf(wp, "%s ", word);
                invert_word(word);
            }
            fprintf(wp, "%s ", word);
        }
    }

    fclose(wp);
    fclose(rp);

    return 0;
}