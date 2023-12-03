#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    char *filename;
    if (argc == 2)
        filename = argv[1];
    else {
        printf("Program usage: ./trebuchet input\n");
        return -1;
    }

    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Couldn't open file %s\n", filename);
        return -1;
    }

    char ch;
    int string_len = 0;
    int max_string_len = 0;
    while (fscanf(fp, "%c", &ch) != EOF) {
        string_len++;
        if (ch == '\n') {
            if (string_len > max_string_len)
                max_string_len = string_len;
            string_len = 0;
        }
    }
    rewind(fp);
    
    int sum = 0, offset, first, last;
    char buffer = 0; 
    while (fscanf(fp, "%c", &buffer) != EOF) {
        offset = 0, first = 0, last = 0;
        while (buffer != '\n') {
            if ((buffer <= '9') && (buffer >= '0')) {
                first = buffer - '0';
                break;
            }
            fscanf(fp, "%c", &buffer);
            offset++;
        }
        fseek(fp, -offset, SEEK_CUR);
        offset = 0;
        while (buffer != '\n') {
            if ((buffer <= '9') && (buffer >= '0')) {
                last = buffer - '0';
            }
            fscanf(fp, "%c", &buffer);
            offset++;
        }
        sum += first*10 + last;
    }
    printf("%d\n", sum);
    fclose(fp);
    return 0;
}
