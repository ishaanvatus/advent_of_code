CC = gcc
WFLAGS = -Wall -Wextra -Wpedantic 
OFLAGS = -O3
DFLAGS = -g

ALL_SRCS = $(wildcard *.c)
PROGRAMS = $(ALL_SRCS:.c=)

all: $(PROGRAMS)

%: %.c
	$(CC) $(WFLAGS) $(DFLAGS) $< -o $@

clean:
	rm -f $(PROGRAMS)

