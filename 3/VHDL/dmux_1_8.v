module dmux_1_8(
    input i0,
    input [2:0] s0,
    output reg y0,
    output reg y1,
    output reg y2,
    output reg y3,
    output reg y4,
    output reg y5,
    output reg y6,
    output reg y7
);
	always @* begin
	    if(s0==3'b000)
	        y0=i0;
	    else if(s0==3'b001)
	        y1=i0;
	    else if(s0==3'b010)
	        y2=i0;
	    else if(s0==3'b011)
	        y3=i0;
	    else if(s0==3'b100)
	        y4=i0;
	    else if(s0==3'b101)
	        y5=i0;
	    else if(s0==3'b110)
	        y6=i0;
	    else if(s0==3'b111)
	        y7=i0;
	    else begin
	        y0=1'b0;
	        y1=1'b0;
	        y2=1'b0;
	        y3=1'b0;
	        y4=1'b0;
	        y5=1'b0;
	        y6=1'b0;
	        y7=1'b0;
	    end
	end
endmodule
