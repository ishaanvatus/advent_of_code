CC = gcc
CFLAGS = -Wall -Wpedantic -Wextra
OFLAGS = -O3
DFLAGS = -g

ALL_SRCS = $(wildcard *.c)
PROGRAMS = $(ALL_SRCS:.c=)

all: $(PROGRAMS)

%: %.c
	$(CC) $(CFLAGS) $(DFLAGS) $< -o $@

clean:
	rm -f $(PROGRAMS)

