module fa(
	input a,
	input b,
	input c,
	output S,
	output C1
);
	assign S=(a^b)^c;
	assign C1=(a^b)&c;
endmodule
