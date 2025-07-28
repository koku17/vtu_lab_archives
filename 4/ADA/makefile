CC = cc

build:
	@for i in *.c var/*.c ; do $(CC) "$$i" -o "$${i%.*}.bin" -Wall ; done

clean:
	@rm -rf *.bin var/*.bin

doc:
	@latexmk -cd -pdf -shell-escape -auxdir=tmp doc/*.tex #1> /dev/null

mclean:
	@rm -rf doc/tmp/ doc/_minted-*/ doc/*.pdf

.PHONY:	doc
