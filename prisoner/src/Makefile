CC=gcc
CFLAGS=
SOURCES=$(wildcard *.c)
EXES=$(patsubst %.c,%,$(SOURCES))
OUT=../warriors

all: $(EXES)

$(EXES): % : %.c
	$(CC) $(CFLAGS) $< -o $(OUT)/$@
clean:
	-for i in $(EXES); do rm $(OUT)/$$i; done
	-rm $(OUT)/*.pyc $(OUT)/*.lib $(OUT)/*.fas
