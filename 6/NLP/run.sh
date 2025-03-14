#!/bin/sh

while true
do
	printf '%s\n%s\n%s\n%s\n%s\n%s\n'    \
		"Select Lab Program :"         \
		"1. Text Preprocessing    [1]" \
		"2. N-gram Probability    [2]" \
		"3. Minimum edit distance [3]" \
		"4. CFG Parser            [4]" \
		"5. Exit                  [E]"

	read -p "> " PROGRAM

	case $PROGRAM in
		E|e)
			exit 0
		;;
		1|2|3|4|5|6|7|8|9)
			python Lab$PROGRAM.py
		;;
		*)
			echo -e "Invalid Choice !\nSelect again\n"
	esac
done
