build:
	@cc -Wall gcd_algorithms.c -o gcd.bin

clean:
	@rm -rf *.bin

tc:
	@[ -e gcd.bin ] || make build
	@sh auto.sh
