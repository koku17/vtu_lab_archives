module and_gate_tb;
	reg a,b;
	wire y;
	and_gate out(
		.a(a),
		.b(b),
		.y(y)
	);
	initial begin
		$display(".-----------.\n| A | B | Y |\n|-----------|");
		$monitor("| %d | %d | %d |",a,b,y);

		a=0;
		b=0;

		#10
		a=0;
		b=1;

		#10
		a=1;
		b=0;

		#10
		a=1;
		b=1;

		#10
		$display(".-----------.\n");
		$finish;
	end
endmodule
