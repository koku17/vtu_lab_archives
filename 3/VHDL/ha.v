module ha(
	input a,
	input b,
	output S,
	output C
);
	assign S=a^b;
	assign C=a&b;
endmodule
