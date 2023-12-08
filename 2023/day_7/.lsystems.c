#include <stdio.h>

int main(int argc, char **argv) 
{
    char *filename;
    if (argc == 2) 
        filename = argv[1];
    else {
        printf("program usage: ./lysystem input\n");
        return -1;
    }
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        fprintf("couldn't open file %s\n");
    }
    int rule_count = 0;
    while (ch != '\n');
}
