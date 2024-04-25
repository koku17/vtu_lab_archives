TMP := pdf iso tgz class dvi
doc:
	@latexmk -cd -shell-escape -auxdir=tmp/ doc/*.tex

mclean:
	@echo "Removing misc files *.class *.pdf *.iso *.tgz *.dvi ..."
	@for i in $(TMP) ; do find . -name "*$$i*" -delete ; done
	@rm -rf doc/tmp doc/_minted* doc/short/tmp doc/short/_minted*
	@echo "Removed misc files ..."

ark:	mclean
	@tar -zcvf archive.tgz *
cdrom:	mclean
	@mkisofs --iso-level 4 -o JAVA-CD.iso .
.PHONY : doc
