import 'package:flutter/material.dart';
import 'package:untitled/widgets/JobCard.dart';

import '../modals/job_list.dart';
import 'google.dart';

class jobPage extends StatefulWidget {
  const jobPage({Key? key}) : super(key: key);

  @override
  _jobPageState createState() => _jobPageState();
}

class _jobPageState extends State<jobPage> {
  @override
  Widget build(BuildContext context) {
    var myColor = const Color.fromARGB(255, 227, 227, 227);
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Material(
        child: Scaffold(
          backgroundColor: myColor,
          appBar: AppBar(
            backgroundColor: myColor,
            elevation: 0.0,
            iconTheme: const IconThemeData(color: Colors.black),
            shape: const RoundedRectangleBorder(
              borderRadius: BorderRadius.vertical(
                bottom: Radius.circular(30),
              ),
            ),
          ),
          drawer: const Drawer(),
          body: Container(
            margin: const EdgeInsets.only(left: 15),
            child: SingleChildScrollView(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  const SizedBox(
                    height: 30,
                  ),
                  const Text(
                    "Devloper",
                    style: TextStyle(
                      fontWeight: FontWeight.w400,
                      fontSize: 40,
                    ),
                  ),
                  const Text(
                    "Jobs",
                    style: TextStyle(
                      fontWeight: FontWeight.w400,
                      fontSize: 40,
                    ),
                  ),
                  const SizedBox(
                    height: 55,
                  ),
                  const Text(
                    "Recommended for you",
                    style: TextStyle(
                      fontWeight: FontWeight.w500,
                      fontSize: 20,
                    ),
                  ),
                  const SizedBox(
                    height: 15,
                  ),
                  Container(
                    height: 200,
                    width: double.infinity,
                    child: ListView.builder(
                        scrollDirection: Axis.horizontal,
                        itemCount: JobCart.items.length,
                        itemBuilder: (context, index) {
                          return JobCard(
                            item: JobCart.items[index],
                          );
                        }),
                  ),
                  const SizedBox(
                    height: 15,
                  ),
                  const Text(
                    "Reccent add",
                    style: TextStyle(
                      fontWeight: FontWeight.w400,
                      fontSize: 20,
                    ),
                  ),
                  const SizedBox(
                    height: 15,
                  ),
                  ListView.builder(
                      scrollDirection: Axis.vertical,
                      itemCount: JobCart.items.length,
                      physics: ScrollPhysics(),
                      shrinkWrap: true,
                      itemBuilder: (context, index) {
                        return JobItemCard(
                          items: JobCart.items[index],
                        );
                      }),
                  const SizedBox(
                    height: 15,
                  )
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class JobItemCard extends StatefulWidget {
  final Item items;
  const JobItemCard({Key? key, required this.items})
      : assert(items != null),
        super(key: key);

  @override
  _JobItemCardState createState() => _JobItemCardState();
}

class _JobItemCardState extends State<JobItemCard> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(top: 15.0, left: 3, right: 15),
      child: GestureDetector(
        onTap: () {
          Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => JobDetail(item: widget.items)));
        },
        child: Container(
          height: 90,
          width: 350,
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(12),
          ),
          child: Row(
            children: [
              Padding(
                padding: const EdgeInsets.all(9.0),
                child: Image.asset(
                  widget.items.image,
                  height: 75,
                  width: 75,
                ),
              ),
              Container(
                height: 78,
                width: 260,
                color: Colors.white,
                child: ListTile(
                  title: Text(
                    widget.items.name,
                    style: const TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w400,
                    ),
                  ),
                  subtitle: Text(widget.items.cumpani),
                  trailing: Text(
                    widget.items.salary,
                    style: const TextStyle(
                      fontWeight: FontWeight.w300,
                      fontSize: 22,
                    ),
                  ),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
