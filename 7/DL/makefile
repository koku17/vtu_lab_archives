doc:
	@find -type f -name "*.tex" -exec \
		latexmk -pdfxe -auxdir=tmp -shell-escape {} +

clean:
	@find -type d -name "tmp" -exec rm -rf {} +
