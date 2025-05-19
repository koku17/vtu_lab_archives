import 'dart:async';
import 'package:flutter/material.dart';

void main() => runApp(StopwatchApp());

class StopwatchApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: StopwatchScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class StopwatchScreen extends StatefulWidget {
  @override
  _StopwatchScreenState createState() => _StopwatchScreenState();
}

class _StopwatchScreenState extends State<StopwatchScreen> {
  late Timer _timer;
  int _milliseconds = 0;
  bool _isRunning = false;

  void _startTimer() {
    _timer = Timer.periodic(Duration(milliseconds: 100), (timer) {
      setState(() {
        _milliseconds += 100;
      });
    });
  }

  void _startStopwatch() {
    if (!_isRunning) {
      _startTimer();
      setState(() {
        _isRunning = true;
      });
    }
  }

  void _stopStopwatch() {
    if (_isRunning) {
      _timer.cancel();
      setState(() {
        _isRunning = false;
      });
    }
  }

  void _resetStopwatch() {
    _timer.cancel();
    setState(() {
      _milliseconds = 0;
      _isRunning = false;
    });
  }

  String _formattedTime() {
    int seconds = (_milliseconds / 1000).floor() % 60;
    int minutes = (_milliseconds / 60000).floor();
    int centiseconds = (_milliseconds / 10).floor() % 100;

    return '$minutes:${seconds.toString().padLeft(2, '0')}.${centiseconds.toString().padLeft(2, '0')}';
  }

  @override
  void dispose() {
    if (_isRunning) _timer.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Stopwatch')),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            _formattedTime(),
            style: TextStyle(fontSize: 48, fontWeight: FontWeight.bold),
          ),
          SizedBox(height: 30),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              ElevatedButton(onPressed: _startStopwatch, child: Text('Start')),
              SizedBox(width: 10),
              ElevatedButton(onPressed: _stopStopwatch, child: Text('Stop')),
              SizedBox(width: 10),
              ElevatedButton(onPressed: _resetStopwatch, child: Text('Reset')),
            ],
          ),
        ],
      ),
    );
  }
}
