import 'package:flutter/material.dart';

void main() {
	runApp(
		MaterialApp(
			home: TodoApp(),
			debugShowCheckedModeBanner: false
		)
	);
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
								border: OutlineInputBorder()
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
			)
		);
	}
}
