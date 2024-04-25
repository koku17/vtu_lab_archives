module mux_4_1(
	input i0,
	input i1,
	input i2,
	input i3,
	input s0,
	input s1,
	output reg y0
);
	always@* begin
		if(s1==0 & s0==0)
			y0=i0;
		else if(s1==0 & s0==1)
			y0=i1;
		else if(s1==1 & s0==0)
			y0=i2;
		else begin
			y0=i3;
		end
	end
endmodule
