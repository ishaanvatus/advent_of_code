#include <stdio.h>

int main(int argc, char **argv) 
{
    char *filename;
    if (argc == 2) 
        filename = argv[1];
    else {
        printf("Program Usage: ./trebuchet_extra input\n");
        return -1;
    }
    FILE *fp = fopen(filename, "r");
    char ch;
    while (ch != EOF) {
        ch = getc(fp);
        printf("%c", ch);
    }
}
