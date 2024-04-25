#!/bin/sh

j=1

while true
do
	clear
	echo "Time Complexity Test ($j)"
	j=$(( j+1 ))
	p=$RANDOM
	q=$RANDOM
	for i in e m c
	do
		printf "\n"
		time ./gcd.bin $i $p $q
	done
	echo -e "\nVerification"
	printf "qalc 'gcd($p,$q)' = $(qalc -t "gcd($p,$q)")"
	sleep 3
done
