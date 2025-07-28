output:
	@find . -name "*.py" -type f -exec python {} \;

outdoc:
	@find . -name "*.tex" -type f -exec latexmk -pdfxe -auxdir=tmp -shell-escape {} \;

.PHONY: output
