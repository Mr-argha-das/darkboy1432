import 'package:flutter/material.dart';
import 'package:untitled/pages/google.dart';

import '../modals/job_list.dart';

class JobCard extends StatefulWidget {
  final Item item;

  const JobCard({Key? key, required this.item})
      : assert(item != null),
        super(key: key);

  @override
  State<JobCard> createState() => _JobCardState();
}

class _JobCardState extends State<JobCard> {
  @override
  Widget build(BuildContext context) {
    final myColor = Color.fromARGB(255, 227, 227, 227);
    return Padding(
      padding: const EdgeInsets.only(right: 18.0),
      child: GestureDetector(
        onTap: () {
          Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => JobDetail(item: widget.item)));
        },
        child: Container(
          height: 190,
          width: 240,
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(15.0),
            color: Colors.white,
          ),
          child: Column(
            children: [
              Container(
                height: 95,
                width: 240,
                decoration: const BoxDecoration(
                    borderRadius: BorderRadius.only(
                        topLeft: Radius.circular(15),
                        topRight: Radius.circular(15)),
                    color: Colors.white),
                child: Row(
                  children: [
                    Container(
                      height: 80,
                      width: 80,
                      margin: const EdgeInsets.only(left: 15),
                      child: Image.asset(widget.item.image),
                    ),
                    Container(
                      height: 40,
                      width: 120,
                      margin: const EdgeInsets.only(left: 10),
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(50),
                        color: myColor,
                      ),
                      child: Center(child: Text(widget.item.time)),
                    ),
                  ],
                ),
              ),
              const SizedBox(
                height: 25,
              ),
              Container(
                height: 65,
                width: 240,
                child: ListTile(
                  title: Text(
                    widget.item.name,
                    style: const TextStyle(
                      fontSize: 20,
                    ),
                  ),
                  trailing: Text(
                    widget.item.salary,
                    style: const TextStyle(fontSize: 22),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
