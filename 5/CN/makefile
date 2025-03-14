doc:
	@find . -name "*.tex" -exec latexmk -pdf -auxdir=tmp/ -cd -shell-escape "{}" \;

clean:
	@echo "Removing misc files ..."
	@for i in '*.tr' '*.class' '*.plot' '*.nam' ; do find . -name "$$i" -exec rm -rf "{}" + ; done
	@echo "Removing auxilary files ..."
	@for i in '_minted*' tmp ; do find . -name "$$i" -exec rm -rf "{}" + ; done
	@echo "Cleaning done"

.PHONY: doc
