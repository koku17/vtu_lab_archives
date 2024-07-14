exec:
	@chmod +x *.py

unexec:
	@chmod -x *.py

doc:
	@latexmk -cd -pdf -shell-escape -auxdir=tmp doc/*.tex 1> /dev/null

clean:
	@rm -rf doc/tmp/ doc/_minted-*/ doc/*.pdf

.PHONY:	doc
