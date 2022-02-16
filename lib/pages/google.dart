import 'package:flutter/material.dart';
import 'package:untitled/modals/job_list.dart';

class JobDetail extends StatefulWidget {
  final Item item;
  const JobDetail({Key? key, required this.item})
      : assert(item != null),
        super(key: key);

  @override
  _JobDetailState createState() => _JobDetailState();
}

class _JobDetailState extends State<JobDetail> {
  bool changeIcon = false;
  bool changeText = false;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Material(
        child: Scaffold(
          backgroundColor: const Color.fromARGB(255, 227, 227, 227),
          body: Column(
            children: [
              Padding(
                padding: const EdgeInsets.only(top: 30.0, right: 320),
                child: InkWell(
                  onTap: () {
                    setState(() {
                      Navigator.pop(context);
                    });
                  },
                  child: Container(
                    height: 50,
                    width: 50,
                    child: const Icon(
                      Icons.close_rounded,
                      size: 30,
                    ),
                  ),
                ),
              ),
              Center(
                child: Text(widget.item.cumpani),
              ),
              Padding(
                padding: const EdgeInsets.only(top: 18.2),
                child: Container(
                  height: 680,
                  width: 500,
                  decoration: const BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.only(
                      topLeft: Radius.circular(50),
                      topRight: Radius.circular(50),
                    ),
                  ),
                  child: Center(
                    child: Column(
                      children: [
                        Container(
                          height: 80,
                          width: 80,
                          margin: const EdgeInsets.only(top: 20, bottom: 15),
                          child: Image.asset(widget.item.image),
                        ),
                        Text(
                          widget.item.name,
                          style: const TextStyle(
                            fontSize: 28,
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                        const Padding(
                          padding: EdgeInsets.only(
                            top: 10.0,
                            bottom: 10,
                          ),
                          child: Text(
                            "San Francisco, California",
                            style: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 15,
                              color: Colors.grey,
                            ),
                          ),
                        ),
                        Container(
                          height: 80,
                          child: Row(
                            children: [
                              Center(
                                child: Container(
                                  height: 40,
                                  width: 170,
                                  margin: const EdgeInsets.only(left: 25),
                                  decoration: BoxDecoration(
                                    color: const Color.fromARGB(
                                        255, 227, 227, 227),
                                    borderRadius: BorderRadius.circular(10),
                                  ),
                                  child: Center(
                                    child: Text(
                                      widget.item.time,
                                      style: const TextStyle(
                                          fontSize: 16,
                                          fontWeight: FontWeight.w500),
                                    ),
                                  ),
                                ),
                              ),
                              Padding(
                                padding: const EdgeInsets.only(left: 30.0),
                                child: Text(
                                  widget.item.salary,
                                  style: const TextStyle(
                                    fontSize: 33,
                                    fontWeight: FontWeight.w400,
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                        const Padding(
                          padding: EdgeInsets.only(right: 230.0),
                          child: Text(
                            "Requirements",
                            style: TextStyle(
                              fontWeight: FontWeight.w500,
                              fontSize: 20,
                            ),
                          ),
                        ),
                        Container(
                          height: 170,
                          width: 500,
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.start,
                            children: const [
                              SizedBox(
                                height: 20,
                              ),
                              Text(
                                "1.  Good UI/UX knowledge",
                                style: TextStyle(color: Colors.grey),
                              ),
                              SizedBox(
                                height: 10,
                              ),
                              Text(
                                  "2.  Know the princples of aimation and you can create",
                                  style: TextStyle(color: Colors.grey)),
                              SizedBox(
                                height: 10,
                              ),
                              Text(
                                  "3.  Eceptional communication skills team-working skills",
                                  style: TextStyle(color: Colors.grey)),
                              SizedBox(
                                height: 10,
                              ),
                              Text(
                                  "4.  Direct experience using Adobe Premiere, Adobe After",
                                  style: TextStyle(color: Colors.grey)),
                              SizedBox(
                                height: 5,
                              ),
                              Text(
                                  "Effects & other tools used to creat videos, animations",
                                  style: TextStyle(color: Colors.grey)),
                            ],
                          ),
                        ),
                        InkWell(
                          onTap: () {
                            setState(() {
                              changeIcon = true;
                            });
                          },
                          child: Container(
                            height: 80,
                            width: 400,
                            margin: const EdgeInsets.only(top: 120),
                            child: Row(
                              children: [
                                Padding(
                                  padding: const EdgeInsets.only(left: 50.0),
                                  child: InkWell(
                                    child: Container(
                                      height: 60,
                                      width: 60,
                                      color: Colors.white,
                                      child: changeIcon
                                          ? const Icon(
                                              Icons.favorite,
                                              size: 30,
                                            )
                                          : const Icon(
                                              Icons.favorite_border,
                                              size: 30,
                                            ),
                                    ),
                                  ),
                                ),
                                Padding(
                                  padding: const EdgeInsets.only(left: 50.0),
                                  child: InkWell(
                                    onTap: () {
                                      setState(() {
                                        changeText = true;
                                      });
                                    },
                                    child: Container(
                                      height: 55,
                                      width: 200,
                                      decoration: BoxDecoration(
                                        color: Colors.deepOrange,
                                        borderRadius: BorderRadius.circular(10),
                                      ),
                                      child: Center(
                                        child: changeText
                                            ? const Text(
                                                "Submitted",
                                                style: TextStyle(
                                                  fontSize: 15,
                                                  fontWeight: FontWeight.w400,
                                                  color: Colors.white,
                                                ),
                                              )
                                            : const Text(
                                                "Apply Now",
                                                style: TextStyle(
                                                  fontSize: 15,
                                                  fontWeight: FontWeight.w400,
                                                  color: Colors.white,
                                                ),
                                              ),
                                      ),
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ],
                    ),
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
