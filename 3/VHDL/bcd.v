module bcd(
	input [3:0] a,
	input [3:0] b,
	input carry_in,
	output reg [3:0] sum,
	output reg carry
);
	reg [4:0] sum_temp;
	always@(a,b,carry_in) begin
		sum_temp=a+b+carry_in;
		if(sum_temp>9) begin
			sum=sum_temp+6;
			carry=1;
		end
		else begin
			carry=0;
			sum=sum_temp[3:0];
		end
	end
endmodule
