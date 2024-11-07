doc:
	@find . -name "*.tex" -exec latexmk -cd -auxdir=tmp -pdfxe -shell-escape {} \;
clean:
	@find . -type d -name "tmp" -exec rm -rf {} +
	@find . -type d -name "_minted*" -exec rm -rf {} +

.PHONY: doc
