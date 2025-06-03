== Lab 1 ==
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(title: Text("Hello, World!")),
        body: Center(
          child: Text(
            "Hello, World!",
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
        ),
      ),
    );
  }
}

== Lab 2 ==
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
      appBar: AppBar(title: const Text('Counter Application')),
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
                  child: const Text('-'),
                ),
                const SizedBox(width: 20),
                ElevatedButton(
                  onPressed: () => setState(() => _counter++),
                  child: const Text('+'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

== Lab 3 ==
import 'package:flutter/material.dart';

void main() =>
    runApp(MaterialApp(home: LoginScreen(), debugShowCheckedModeBanner: false));

class LoginScreen extends StatelessWidget {
  final username = TextEditingController(), password = TextEditingController();
  LoginScreen({super.key});
  void login(BuildContext context) {
    final msg = (username.text == 'admin' && password.text == '1234')
        ? 'Login Successful'
        : 'Invalid Credentials';
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(msg)));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Login')),
      body: Padding(
        padding: EdgeInsets.all(20),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: username,
              decoration: InputDecoration(labelText: 'Username'),
            ),
            TextField(
              controller: password,
              obscureText: true,
              decoration: InputDecoration(labelText: 'password'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => login(context),
              child: Text('Login'),
            ),
          ],
        ),
      ),
    );
  }
}

== Lab 4 ==
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(home: TodoApp(), debugShowCheckedModeBanner: false));
}

class TodoApp extends StatefulWidget {
  @override
  _TodoAppState createState() => _TodoAppState();
}

class _TodoAppState extends State<TodoApp> {
  final List<String> tasks = [];
  final TextEditingController taskController = TextEditingController();

  void addTask() {
    if (taskController.text.isNotEmpty) {
      setState(() {
        tasks.add(taskController.text);
      });
      taskController.clear();
    }
  }

  void removeTask(int index) {
    setState(() {
      tasks.removeAt(index);
    });
  }

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('To-Do List')),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: taskController,
              decoration: InputDecoration(
                labelText: 'Enter Task',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 10),
            ElevatedButton(onPressed: addTask, child: Text('Add Task')),
            Expanded(
              child: ListView.builder(
                itemCount: tasks.length,
                itemBuilder: (context, index) {
                  return Card(
                    child: ListTile(
                      title: Text(tasks[index]),
                      trailing: IconButton(
                        icon: Icon(Icons.delete, color: Colors.red),
                        onPressed: () => removeTask(index),
                      ),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}

== Lab 5 ==
import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(home: CalculatorApp(), debugShowCheckedModeBanner: false));
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
                  onPressed: () => calculate('+'),
                  child: Text("+"),
                ),
                ElevatedButton(
                  onPressed: () => calculate('-'),
                  child: Text("-"),
                ),
                ElevatedButton(
                  onPressed: () => calculate('*'),
                  child: Text("x"),
                ),
                ElevatedButton(
                  onPressed: () => calculate('/'),
                  child: Text("/"),
                ),
              ],
            ),
            SizedBox(height: 20),
            Text(
              result,
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }
}

== Lab 7 ==
import 'dart:async';
import 'package:flutter/material.dart';

void main() => runApp(
  MaterialApp(debugShowCheckedModeBanner: false, home: StopwatchApp()),
);

class StopwatchApp extends StatefulWidget {
  @override
  _StopwatchAppState createState() => _StopwatchAppState();
}

class _StopwatchAppState extends State<StopwatchApp> {
  Stopwatch _stopwatch = Stopwatch();
  Timer? _timer;
  void _startStopwatch() {
    if (!_stopwatch.isRunning) {
      _stopwatch.start();
      _timer = Timer.periodic(
        Duration(milliseconds: 50),
        (timer) => setState(() {}),
      );
    }
  }

  void _stopStopwatch() {
    _stopwatch.stop();
    _timer?.cancel();
  }

  void _resetStopwatch() {
    _stopwatch.reset();
    setState(() {});
  }

  String _formattedTime() {
    final ms = _stopwatch.elapsedMilliseconds;
    return "${(ms ~/ 3600000).toString().padLeft(2, '0')}:"
        "${(((ms ~/ 60000) % 60).toString().padLeft(2, '0'))}:"
        "${(((ms ~/ 1000) % 60).toString().padLeft(2, '0'))}."
        "${((ms % 1000 ~/ 10).toString().padLeft(2, '0'))}";
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Stopwatch')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              _formattedTime(),
              style: TextStyle(fontSize: 50, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 30),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                for (var btn in ['Start', 'Stop', 'Reset'])
                  Padding(
                    padding: EdgeInsets.symmetric(horizontal: 5),
                    child: ElevatedButton(
                      onPressed: btn == 'Start'
                          ? _startStopwatch
                          : btn == 'Stop'
                          ? _stopStopwatch
                          : _resetStopwatch,
                      child: Text(btn),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: btn == 'Start'
                            ? Colors.green
                            : btn == 'Stop'
                            ? Colors.red
                            : Colors.blue,
                        padding: EdgeInsets.symmetric(
                          horizontal: 20,
                          vertical: 10,
                        ),
                      ),
                    ),
                  ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

== Lab 8 ==
import 'package:flutter/material.dart';

void main() {
  runApp(NNavigator());
}

class NNavigator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Navigation Demo',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: HomeScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Home Screen')),
      body: Center(
        child: ElevatedButton(
          child: Text('Go to Second Screen'),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => SecondScreen()),
            );
          },
        ),
      ),
    );
  }
}

class SecondScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Second Screen')),
      body: Center(
        child: ElevatedButton(
          child: Text('Go back to Home'),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
    );
  }
}

== Lab 10 ==
import 'package:flutter/material.dart';
import 'dart:math';

void main() => runApp(MaterialApp(home: RotatingLogo(), debugShowCheckedModeBanner: false));

class RotatingLogo extends StatefulWidget {
  @override
  State<RotatingLogo> createState() => _RotatingLogoState();
}

class _RotatingLogoState extends State<RotatingLogo>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller = AnimationController(
    vsync: this,
    duration: const Duration(seconds: 5),
  )..repeat();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: AnimatedBuilder(
          animation: _controller,
          builder: (_, child) =>
              Transform.rotate(angle: _controller.value * 2 * pi, child: child),
          child: Image.asset('chrome-like-logo.png', width: 150),
        ),
      ),
    );
  }

  @override
  void dispose() => _controller.dispose();
}

== Lab 11 ==
import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';

void main() => runApp(
  const MaterialApp(home: ExpenseApp(), debugShowCheckedModeBanner: false),
);

class ExpenseApp extends StatefulWidget {
  const ExpenseApp({super.key});
  @override
  State<ExpenseApp> createState() => _ExpenseAppState();
}

class _ExpenseAppState extends State<ExpenseApp> {
  final _catCtrl = TextEditingController();
  final _amtCtrl = TextEditingController();
  final _data = <Map<String, dynamic>>[];
  final _colors = [Colors.red, Colors.green, Colors.blue, Colors.orange];

  void _add() {
    final c = _catCtrl.text.trim(), a = double.tryParse(_amtCtrl.text);
    if (c.isNotEmpty && a != null) {
      setState(() {
        _data.add({
          'cat': c,
          'amt': a,
          'clr': _colors[_data.length % _colors.length],
        });
        _catCtrl.clear();
        _amtCtrl.clear();
      });
    }
  }

  @override
  Widget build(BuildContext ctx) => Scaffold(
    appBar: AppBar(title: const Text('Expense Tracker')),
    body: Padding(
      padding: const EdgeInsets.all(12),
      child: Column(
        children: [
          TextField(
            controller: _catCtrl,
            decoration: const InputDecoration(labelText: 'Category'),
          ),
          TextField(
            controller: _amtCtrl,
            decoration: const InputDecoration(labelText: 'Amount'),
            keyboardType: TextInputType.number,
          ),
          ElevatedButton(onPressed: _add, child: const Text('Add')),
          const SizedBox(height: 10),
          Expanded(
            child: _data.isEmpty
                ? const Text('No data')
                : PieChart(
                    PieChartData(
                      sections: _data
                          .map(
                            (e) => PieChartSectionData(
                              value: e['amt'],
                              color: e['clr'],
                              title: e['cat'],
                              radius: 60,
                              titleStyle: const TextStyle(
                                fontSize: 12,
                                color: Colors.white,
                              ),
                            ),
                          )
                          .toList(),
                    ),
                  ),
          ),
        ],
      ),
    ),
  );
}

== Lab 12 ==
import 'package:flutter/material.dart';

void main() =>
    runApp(MaterialApp(home: QuizApp(), debugShowCheckedModeBanner: false));

class QuizApp extends StatefulWidget {
  @override
  State<QuizApp> createState() => _QuizAppState();
}

class _QuizAppState extends State<QuizApp> {
  final qns = [
    {
      'q': 'Capital of India?',
      'o': ['Mumbai', 'Delhi', 'Kolkata', 'Chennai'],
      'a': 1,
    },
    {
      'q': '5 + 3 = ?',
      'o': ['6', '8', '9', '7'],
      'a': 1,
    },
    {
      'q': 'Color of sky?',
      'o': ['Red', 'Blue', 'Green', 'Yellow'],
      'a': 1,
    },
  ];

  int i = 0, score = 0;

  void answer(int sel) {
    if (sel == qns[i]['a']) score++;
    setState(() => i++);
  }

  void reset() => setState(() => i = score = 0);

  @override
  Widget build(BuildContext ctx) {
    if (i >= qns.length) {
      return Scaffold(
        appBar: AppBar(title: Text('Result')),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Score: $score / ${qns.length}',
                style: TextStyle(fontSize: 24),
              ),
              ElevatedButton(onPressed: reset, child: Text('Play Again')),
            ],
          ),
        ),
      );
    }

    var q = qns[i];
    return Scaffold(
      appBar: AppBar(title: Text('Quiz App')),
      body: Padding(
        padding: EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Q${i + 1}: ${q['q']}', style: TextStyle(fontSize: 20)),
            SizedBox(height: 20),
            ...(q['o'] as List<String>).asMap().entries.map(
              (e) => ElevatedButton(
                onPressed: () => answer(e.key),
                child: Text(e.value),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
