CC = gcc
CFLAGS = -Wall -Wpedantic -Wextra
OFLAGS = -O3
DFLAGS = -g
SRCS = $(wildcard *.c)
BINARY = trebuchet
OBJS = $(SRCS:.c=.o)

all: $(BINARY)


%.o: %.c
	$(CC) $(CFLAGS) $(DFLAGS) -c $< -o $@

$(BINARY): $(OBJS)
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -f $(OBJS)
