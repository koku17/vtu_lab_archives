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
