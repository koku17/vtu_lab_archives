module dmux_1_4(
	input i0,
	input [1:0] s0,
	output reg y0,
	output reg y1,
	output reg y2,
	output reg y3
);
	always @* begin
		if(s0==2'b00)
			y0=i0;
		else if(s0==2'b01)
			y1=i0;
		else if(s0==2'b10)
			y2=i0;
		else if(s0==2'b11)
			y3=i0;
		else begin
			y0=1'b0;
			y1=1'b0;
			y2=1'b0;
			y3=1'b0;
		end
	end
endmodule
