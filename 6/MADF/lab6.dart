import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MaterialApp(home: Scaffold(body: weatherApp())));
}

class weatherApp extends StatefulWidget {
  const weatherApp({super.key});

  @override
  State<weatherApp> createState() => _weatherAppState();
}

class _weatherAppState extends State<weatherApp> {
  final c = TextEditingController();
  String r = '';
  bool l = false;

  fetchWeather() async {
    setState(() {
      l = true;
    });

    final city = c.text.trim();
    try {
      final geoRes = await http.get(
        Uri.parse(
          'https://geocoding-api.open-meteo.com/v1/search?name=$city&count=1',
        ),
      );
      final geo = jsonDecode(geoRes.body);

      if (geo['results'] == null ||
          geo['results'].isEmpty ||
          geo['results'][0]['name'].toString().toLowerCase() !=
              city.toLowerCase()) {
        setState(() {
          r = 'Invalid city';
          l = false;
        });
        return;
      }

      final lat = geo['results'][0]['latitude'];
      final lon = geo['results'][0]['longitude'];

      final wRes = await http.get(
        Uri.parse(
          'https://api.open-meteo.com/v1/forecast?latitude=$lat&longitude=$lon&current_weather=true',
        ),
      );
      final w = jsonDecode(wRes.body);

      final temp = w['current_weather']['temperature'];

      setState(() {
        r = '$city: $temp °C';
        l = false;
      });
    } catch (e) {
      setState(() {
        r = 'Error fetching weather';
        l = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(20),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          TextField(
            controller: c,
            decoration: InputDecoration(hintText: 'Enter city'),
          ),
          ElevatedButton(onPressed: fetchWeather, child: Text('Check weather')),
          if (l) CircularProgressIndicator(),
          if (r.isNotEmpty) Text(r, style: TextStyle(fontSize: 18)),
        ],
      ),
    );
  }
}
