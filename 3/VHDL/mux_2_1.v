module mux_2_1(
	input i0,
	input i1,
	input s0,
	output y0
);
	assign y0=(s0)?i1:i0;
endmodule
