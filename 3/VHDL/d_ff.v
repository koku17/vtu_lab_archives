module d_ff(
	input d,
	input clk,
	output reg q,
	output qb
);
	always@(posedge clk) begin
		case({d})
			1'b0: q<=1'b0;
			1'b1: q<=1'b1;
		endcase
	end
	assign qb=~q;
endmodule
