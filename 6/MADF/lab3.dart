import 'package:flutter/material.dart';
 
void main() =>
		runApp(MaterialApp(home: LoginScreen(), debugShowCheckedModeBanner: false));
 
class LoginScreen extends StatelessWidget {
	final username = TextEditingController(), password = TextEditingController();
	LoginScreen({super.key});
	void login(BuildContext context) {
		final msg = (username.text == 'admin' && password.text == '1234')
			? 'Login Successful' : 'Invalid Credentials';
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
