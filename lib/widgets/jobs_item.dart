import 'package:flutter/material.dart';
import 'package:untitled/modals/job_list.dart';

import '../pages/google.dart';

class JobsWidget extends StatefulWidget {
  final Item item;

  const JobsWidget({Key? key, required this.item})
      : assert(item != null),
        super(key: key);

  @override
  State<JobsWidget> createState() => _JobsWidgetState();
}

class _JobsWidgetState extends State<JobsWidget> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(left: 18, right: 18.0, top: 8, bottom: 8),
      child: Container(
          height: 170,
          width: 200,
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(13),
          ),
          child: Column(
            children: [
              Container(
                height: 83,
                width: 350,
                margin: const EdgeInsets.only(top: 5),
                child: Row(
                  children: [
                    Container(
                      height: 80,
                      width: 80,
                      margin: const EdgeInsets.only(left: 23),
                      child: Image.asset(
                        widget.item.image,
                        height: 80,
                        width: 80,
                      ),
                    ),
                    Container(
                      height: 70,
                      width: 220,
                      margin: const EdgeInsets.only(left: 15),
                      child: ListTile(
                        title: Text(widget.item.name),
                        subtitle: Text(widget.item.cumpani),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(
                height: 7,
              ),
              Container(
                height: 75,
                width: 350,
                child: ListTile(
                  onTap: () {
                    Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) =>
                                JobDetail(item: widget.item)));
                  },
                  leading: Container(
                    height: 52,
                    width: 160,
                    margin: const EdgeInsets.only(left: 10),
                    decoration: BoxDecoration(
                        color: const Color.fromARGB(255, 227, 227, 227),
                        borderRadius: BorderRadius.circular(12),
                        boxShadow: [
                          const BoxShadow(
                            blurRadius: 15,
                            offset: Offset(-4, -4),
                            color: Colors.white,
                            spreadRadius: 1,
                          ),
                          BoxShadow(
                            blurRadius: 15,
                            offset: const Offset(4, 4),
                            color: Colors.grey.shade300,
                            spreadRadius: 1,
                          )
                        ]),
                    child: const Center(
                      child: Text(
                        "Apply",
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w500,
                          color: Colors.deepOrange,
                        ),
                      ),
                    ),
                  ),
                  trailing: Text(
                    widget.item.salary,
                    style: const TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.w400,
                    ),
                  ),
                ),
              ),
            ],
          )),
    );
  }
}
