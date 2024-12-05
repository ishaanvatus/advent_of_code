CC=gcc
OPT=O0
CFLAGS=-Wall -Wextra -Wpedantic -g 
CFILES=main.c
OBJECTS=main.o
BINARY=main

all: $(BINARY)

$(BINARY): $(OBJECTS)
	$(CC) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $^

clean:
	rm -rf $(BINARY) $(OBJECTS)
