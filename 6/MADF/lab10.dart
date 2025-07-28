import 'package:flutter/material.dart';
import 'dart:math';

void main() => runApp(
  const MaterialApp(
    home: AnimatedLogoScreen(),
    debugShowCheckedModeBanner: false,
  ),
);

class AnimatedLogoScreen extends StatefulWidget {
  const AnimatedLogoScreen({super.key});
  @override
  State<AnimatedLogoScreen> createState() => _AnimatedLogoScreenState();
}

class _AnimatedLogoScreenState extends State<AnimatedLogoScreen>
    with TickerProviderStateMixin {
  late final AnimationController _rotationController = AnimationController(
    vsync: this,
    duration: const Duration(seconds: 5),
  )..repeat();
  late final Animation<double> _rotationAnimation = Tween(
    begin: 0.0,
    end: 2 * pi,
  ).animate(CurvedAnimation(parent: _rotationController, curve: Curves.linear));

  late final AnimationController _opacityController = AnimationController(
    vsync: this,
    duration: const Duration(seconds: 3),
  )..forward();
  late final Animation<double> _opacityAnimation = Tween(begin: 0.0, end: 1.0)
      .animate(
        CurvedAnimation(parent: _opacityController, curve: Curves.easeInOut),
      );
  @override
  void dispose() {
    _rotationController.dispose();
    _opacityController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueAccent,
      appBar: AppBar(title: const Text("Animated Logo")),
      body: Center(
        child: AnimatedBuilder(
          animation: _rotationController,
          builder: (context, child) => FadeTransition(
            opacity: _opacityAnimation,
            child: Transform.rotate(
              angle: _rotationAnimation.value,
              child: child,
            ),
          ),
          child: Image.asset(
            'assets/chrome-like-logo.png',
            width: 150,
            height: 150,
          ),
        ),
      ),
    );
  }
}
