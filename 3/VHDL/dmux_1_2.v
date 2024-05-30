module dmux_1_2(
	input i0,
	input s0,
	output reg y0,
	output reg y1
);
	always@(i0 or s0) begin
		if(s0==0)
			y0=i0;
		else begin
			y1=i0;
		end
	end
endmodule
