//import 'package:flutter/cupertino.dart';
//import 'package:flutter/widgets.dart';
import 'package:flutter/material.dart';
import 'package:untitled/pages/appli_page.dart';
import 'package:untitled/pages/jobpage.dart';
import 'package:untitled/pages/routes/myroutes.dart';

void main() {
  runApp(const Myapp());
}

class Myapp extends StatelessWidget {
  const Myapp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return myAppage();
  }
}

class myAppage extends StatefulWidget {
  const myAppage({Key? key}) : super(key: key);

  @override
  _myAppageState createState() => _myAppageState();
}

class _myAppageState extends State<myAppage> {
  int currentIndex = 0;
  final pages = [
    const jobPage(),
    const appliCations(),
  ];

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
        home: Material(
          child: Scaffold(
            body: pages[currentIndex],
            bottomNavigationBar: BottomNavigationBar(
              selectedFontSize: 18,
              unselectedFontSize: 18,
              iconSize: 5,
              selectedItemColor: Colors.black,
              unselectedItemColor: Colors.black,
              onTap: (index) {
                setState(() {
                  currentIndex = index;
                });
              },
              items: const <BottomNavigationBarItem>[
                BottomNavigationBarItem(
                  label: 'Jobs',
                  icon: Icon(Icons.brightness_1_rounded),
                ),
                BottomNavigationBarItem(
                  label: 'applications',
                  icon: Icon(Icons.brightness_1_rounded),
                ),
              ],
            ),
          ),
        ),
        routes: {
          MyRoutes.jobRoute: (context) => jobPage(),
          MyRoutes.applicationRoute: (context) => appliCations(),
        });
  }
}

// This trailing comma makes auto-formatting nicer for build method
