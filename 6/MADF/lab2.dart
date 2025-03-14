import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: CounterApp()));

class CounterApp extends StatefulWidget {
  @override
  _CounterAppState createState() => _CounterAppState();
}

class _CounterAppState extends State<CounterApp> {
  int _counter = 0;

  @override
  Widget build(BuildContext context) {
	return Scaffold(
	  appBar: AppBar(title: const Text('Counter Application'),),
	  body: Center(
		child: Column(
		  mainAxisAlignment: MainAxisAlignment.center,
		  children: [
			Text('$_counter', style: const TextStyle(fontSize: 40)),
			Row(
			  mainAxisAlignment: MainAxisAlignment.center,
			  children: [
				ElevatedButton(
				  onPressed: () => setState(() => _counter--),
				  child: const Text('-')
				),
				const SizedBox(width: 20),
				ElevatedButton(
				  onPressed: () => setState(() => _counter++),
				  child: const Text('+')
				),
			  ],
			),
		  ],
		),
	  ),
	);
  }
}
