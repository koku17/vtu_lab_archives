# Programs
JRE = java
JDK = javac

JCLASS = Array1D Arraylist BitOp com.sample.Control com.sample.LinkedList2 Fibonacci LoopBreak \
	 NDimArray QueueExample ReturnEx StackClass

build:
	@echo "Building ..."
	@$(JDK) -d . *.java
	@echo "Build Complete"

run:    build
	@for i in $(JCLASS) ; do clear ; printf "Running class $$i\n" ; \
		$(JRE) $$i ; printf "\nPress Return to continue ..." ; read n ; done

clean:
	@echo "Removing class files ..."
	@rm -rf *.class com/
