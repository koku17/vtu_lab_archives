CC=cc
TMP=pdf iso tgz

build:
	@echo "Building ..."
	@for i in *.c ; do $(CC) $$i -Wall -o $${i%.c}.bin -lm ; done
	@echo "Build Done"

clean:
	@echo "Removing compiled files ..."
	@rm -rf *.bin

doc:
	@latexmk -pdf -auxdir=tmp/ -shell-escape -cd doc/*.tex
	@gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=OS-LAB.pdf -dBATCH doc/{1..10}.pdf

ark:
	@tar -zcvf archive.tgz *.c makefile doc/*.tex doc/*.c

cdrom:	ark
	@mkisofs archive.tgz > OS-CD.iso

mclean:
	@echo "Removing misc files *.pdf *.iso *.tgz ..."
	@for i in $(TMP) ; do find . -name "*$$i*" -delete ; done
	@rm -rf doc/tmp doc/_minted*
	@echo "Removed misc files ..."

.PHONY:	doc
