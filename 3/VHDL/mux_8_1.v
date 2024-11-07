module mux_8_1(
	input i0,
	input i1,
	input i2,
	input i3,
	input i4,
	input i5,
	input i6,
	input i7,
	input s0,
	input s1,
	input s2,
	output reg y0
);
	always@* begin
		if(s2==1'b0 & s1==1'b0 & s0==1'b0)
			y0=i0;
		else if(s2==1'b0 & s1==1'b0 & s0==1'b1)
			y0=i1;
		else if(s2==1'b0 & s1==1'b1 & s0==1'b0)
			y0=i2;
		else if(s2==1'b0 & s1==1'b1 & s0==1'b1)
			y0=i3;
		else if(s2==1'b1 & s1==1'b0 & s0==1'b0)
			y0=i4;
		else if(s2==1'b1 & s1==1'b0 & s0==1'b1)
			y0=i6;
		else if(s2==1'b1 & s1==1'b1 & s0==1'b0)
			y0=i6;
		else begin
			y0=i7;
		end
	end
endmodule
