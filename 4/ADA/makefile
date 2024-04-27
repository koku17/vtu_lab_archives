PROGS := "Kruskal's algorithm.c"
CC = cc

build:
	@for i in $(PROGS) ; do $(CC) "$$i" -o "$${i%.*}.bin" ; done

clean:
	@rm -rf *.bin
