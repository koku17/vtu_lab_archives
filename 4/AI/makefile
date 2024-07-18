exec:
	@chmod +x *.py

unexec:
	@chmod -x *.py

doc:
	@latexmk -cd -pdf -shell-escape -auxdir=tmp doc/*.tex 1> /dev/null

clean:
	@rm -rf doc/tmp/ doc/_minted-*/ doc/*.pdf

run:
	@for i in *.py ; do clear ; ./$$i ; printf "\nPress return to Continue ... " ; read continue ; done
.PHONY:	doc
