#!/bin/bash

exec_name=$0

raw(){
	lab=$(echo $1 | sed 's/[a-zA-Z\.]//g')
	script -c "mongosh --quiet < $1" -O /dev/null |\
	sed "s/\[1G\[0Jlab$lab> \[7G\/\[90m\/\//\/\//g" |\
	\grep -vE "\[1G\[0Jlab$lab>|\.\.\.|mongosh mongodb:|switched|Script" |\
	sed 's/[]//g;s/\[..m//g;s/\[.m//g' |\
	sed -e ':a;N;$!ba' |\
	sed '/./,$!d' > /tmp/lab$lab.out
	less /tmp/lab$lab.out
	rm -rf /tmp/lab$lab.out
}

colored(){
	lab=$(echo $1 | sed 's/[a-zA-Z\.]//g')
	script -O /dev/null -c "mongosh --quiet < '$1'" |\
	sed "s///g;s/test/\ntest/g;s/\[1G\[0Jlab$lab> \[7G//g" |\
	sed -e ':a;N;$!ba' -e 's/\n\n/\n/g' |\
	\grep -vE 'Script|mongosh mongodb:' > /tmp/lab$lab.out
	batcat -n /tmp/lab$lab.out
	rm -rf /tmp/lab$lab.out
}

for i in $@
do
	case "$i" in
		--colored|-c)
			shift
			colored $1
		;;
		--raw|-r)
			shift
			raw $1
		;;
	esac
done
