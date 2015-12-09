## Licensed under the MIT Licence
## (C) 2014 Christoph Martin
## For licence text go to http://opensource.org/licenses/MIT

## Makefile
# change to your prefered compiler
CC=gcc
CFLAGS := -fPIC -O3 -g -Wall -Werror
# replace with name of the executable
OUTPUTNAME=productRS
# add all source files here but with '.o' instead of '.c'
OBJS=productRS.o
default: all

all: $(OBJS)
	$(CC) -o $(OUTPUTNAME) $(OBJS)

debug: $(OBJS)
	$(CC) -g -DNDEBUG -o $(OUTPUTNAME) $(OBJS)

opt: $(OBJS)
	$(CC) -O3 -o $(OUTPUTNAME) $(OBJS)

shared: $(OBJS)
	$(CC) -O3 -shared -o $(OUTPUTNAME).so $(OBJS)

.PHONY: clean
clean:
	rm *.o
	rm *.so
	rm $(OUTPUTNAME)
