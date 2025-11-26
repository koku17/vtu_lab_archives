#!/bin/bash

[ -d tmp/lab* ] || flutter create tmp/lab_programs

run_labs () {
	printf '%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n> ' \
		"Select Lab : "            \
		"1.  Hello Flutter   [1]"  \
		"2.  Counter         [2]"  \
		"3.  Login Screen    [3]"  \
		"4.  Todo  List      [4]"  \
		"5.  Calculator      [5]"  \
		"6.  Weather         [6]"  \
		"7.  Stopwatch       [7]"  \
		"8.  UI Navigation   [8]"  \
		"9.  E-commerce      [9]"  \
		"10. Logo Animation  [10]" \
		"11. Expenses report [11]" \
		"12. Quiz            [12]" \
		"13. Exit            [E|Q]"
	
	read PROGRAM
	case $PROGRAM in
		E|e|Q|q)
			exit 0
		;;
		1|2|3|4|5|6|7|8|9|"10"|"11"|"12")
			cp lab$PROGRAM.dart tmp/lab*/lib/main.dart || exit 1
		;;
		*)
			echo -e "Invalid Choice !\nSelect again\n"
			run_labs
	esac

	cd tmp/lab*/ && flutter run
	flutter clean tmp/lab_programs
	run_labs
}

run_labs
