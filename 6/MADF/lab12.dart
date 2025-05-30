import 'package:flutter/material.dart';

void main() =>
    runApp(MaterialApp(home: QuizApp(), debugShowCheckedModeBanner: false));

class QuizApp extends StatefulWidget {
  @override
  State<QuizApp> createState() => _QuizAppState();
}

class _QuizAppState extends State<QuizApp> {
  final questions = [
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

  void answer(int selected) {
    if (selected == questions[i]['a']) score++;
    setState(() => i++);
  }

  void reset() => setState(() => {i = 0, score = 0});

  @override
  Widget build(BuildContext context) {
    if (i >= questions.length) {
      return Scaffold(
        appBar: AppBar(title: Text('Result')),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Score: $score / ${questions.length}',
                style: TextStyle(fontSize: 24),
              ),
              ElevatedButton(onPressed: reset, child: Text('Play Again')),
            ],
          ),
        ),
      );
    }

    var q = questions[i];
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
              (entry) => ElevatedButton(
                onPressed: () => answer(entry.key),
                child: Text(entry.value),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
