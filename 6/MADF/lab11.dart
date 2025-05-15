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
