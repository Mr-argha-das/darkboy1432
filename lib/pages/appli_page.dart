//import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:untitled/widgets/jobs_item.dart';

import '../modals/job_list.dart';

class appliCations extends StatefulWidget {
  const appliCations({Key? key}) : super(key: key);

  @override
  _appliCationsState createState() => _appliCationsState();
}

class _appliCationsState extends State<appliCations> {
  @override
  Widget build(BuildContext context) {
    var myColor = const Color.fromARGB(255, 227, 227, 227);
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Material(
          child: Scaffold(
        backgroundColor: myColor,
        body: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Padding(
                padding: EdgeInsets.only(top: 30.0, left: 18),
                child: Text(
                  "Your",
                  style: TextStyle(
                    fontSize: 28,
                    fontWeight: FontWeight.w400,
                  ),
                ),
              ),
              const Padding(
                padding: EdgeInsets.only(left: 18.0),
                child: Text(
                  "Applications",
                  style: TextStyle(
                    fontSize: 28,
                    fontWeight: FontWeight.w400,
                  ),
                ),
              ),
              const SizedBox(
                height: 30,
              ),
              Container(
                constraints: BoxConstraints(
                  maxHeight: MediaQuery.of(
                    context,
                  ).size.height,
                ),
                child: ListView.builder(
                    scrollDirection: Axis.vertical,
                    itemCount: JobCart.items.length,
                    itemBuilder: (context, index) {
                      return JobsWidget(
                        item: JobCart.items[index],
                      );
                    }),
              ),
            ],
          ),
        ),
      )),
    );
  }
}
