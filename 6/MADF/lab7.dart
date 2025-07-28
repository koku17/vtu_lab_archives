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
