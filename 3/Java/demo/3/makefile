build:
	@echo "Building ..."
	@javac -d . *.java
	@echo "Build Complete"

run:	build
	@for i in $$(seq 1 14) ; do clear ; printf "Running class Program$$i.Program$$i\n\n" ; \
	java "Program$$i.Program$$i" ; printf "\nPress Retrun to Continue ... " ; read n ; done

clean:
	@echo "Removing class files ..."
	@rm -rf Program*/ *.class
