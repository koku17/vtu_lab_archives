import 'package:flutter/material.dart';

void main() {
	runApp(MaterialApp(
		home: CalculatorApp(),
		debugShowCheckedModeBanner: false,
	));
}

class CalculatorApp extends StatefulWidget {
	const CalculatorApp({super.key});
	@override
	_CalculatorAppState createState() => _CalculatorAppState();
}

class _CalculatorAppState extends State<CalculatorApp> {
	final TextEditingController num1Controller = TextEditingController();
	final TextEditingController num2Controller = TextEditingController();
	String result = "";
	void calculate(String operation) {
		double num1 = double.tryParse(num1Controller.text) ?? 0;
		double num2 = double.tryParse(num2Controller.text) ?? 0;
		double res = 0;
		switch (operation) {
			case '+':
				res = num1 + num2;
				break;
			case '-':
				res = num1 - num2;
				break;
			case '*':
				res = num1 * num2;
				break;
			case '/':
				res = (num2 != 0) ? num1 / num2 : double.infinity;
				break;
		}
		setState(() {
			result = "Result:$res";
		});
	}

	@override
	Widget build(BuildContext context) {
		return Scaffold(
			appBar: AppBar(title: Text("Calculator")),
			body: Padding(
				padding: EdgeInsets.all(20),
				child: Column(
					mainAxisAlignment: MainAxisAlignment.center,
					children: [
						TextField(
							controller: num1Controller,
							keyboardType: TextInputType.number,
							decoration: InputDecoration(labelText: "Enter first number"),
						),
						TextField(
							controller: num2Controller,
							keyboardType: TextInputType.number,
							decoration: InputDecoration(labelText: "Enter second number"),
						),
						SizedBox(height: 20),
						Row(
							mainAxisAlignment: MainAxisAlignment.spaceEvenly,
							children: [
								ElevatedButton(
										onPressed: () => calculate('+'), child: Text("+")),
								ElevatedButton(
										onPressed: () => calculate('-'), child: Text("-")),
								ElevatedButton(
										onPressed: () => calculate('*'), child: Text("x")),
								ElevatedButton(
										onPressed: () => calculate('/'), child: Text("/")),
							],
						),
						SizedBox(height: 20),
						Text(result,
								style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
					],
				),
			),
		);
	}
}
