PROGS := "Kruskal's algorithm.c" "Prim's algorithm.c"
CC = cc

build:
	@for i in $(PROGS) ; do $(CC) "$$i" -o "$${i%.*}.bin" ; done

clean:
	@rm -rf *.bin

doc:
	@latexmk -cd -pdf -shell-escape -auxdir=tmp doc/*.tex #1> /dev/null

mclean:
	@rm -rf doc/tmp/ doc/_minted-*/ doc/*.pdf

.PHONY:	doc
