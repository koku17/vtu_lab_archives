#!/bin/sh

j=1

while true
do
	tput -x clear
	echo "Time Complexity Test ($j)"

	# Number of tests
	j=$(( j+1 ))

	# Generate RANDOM variable
	p=$RANDOM
	q=$RANDOM

	# Execute 3 algorithm separately
	for i in e m c
	do
		printf "\n"
		time ./gcd.bin $i $p $q
	done

	# Verification
	echo -e "\nVerification"
	printf "qalc 'gcd($p,$q)' = $(qalc -t "gcd($p,$q)")\n\n"

	# Verify each algorithms
	[ $(./gcd.bin e $p $q | \grep "=" | cut -d "=" -f 2) -eq $(qalc -t "gcd($p,$q)") ] || \
		echo "Verification failed for Euclidean Algorithm !"
	[ $(./gcd.bin m $p $q | \grep "=" | cut -d "=" -f 2) -eq $(qalc -t "gcd($p,$q)") ] || \
		echo "Verification failed for Mid-School Algorithm !"
	[ $(./gcd.bin c $p $q | \grep "=" | cut -d "=" -f 2) -eq $(qalc -t "gcd($p,$q)") ] || \
		echo "Verification failed for CIC Algorithm !"
	sleep 3
done
