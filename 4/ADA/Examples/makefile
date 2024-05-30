# Uncomment '#' in the  beginning to enable the commands

build:
	@cc -Wall gcd_algorithms.c -o gcd.bin

clean:
	@rm -rf *.bin

tc:
	@[ -e gcd.bin ] || make build
	@sh auto.sh
	#@sh auto.sh 1>&2 | less # output to less and not storm terminal screen
