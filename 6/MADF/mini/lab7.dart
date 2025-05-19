import 'package:flutter/material.dart';
import 'dart:math';

void main() => runApp(MaterialApp(home: RotatingLogo()));

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
          child: Image.asset('assets/OIP.jpg', width: 150),
        ),
      ),
    );
  }

  @override
  void dispose() => _controller.dispose();
}
