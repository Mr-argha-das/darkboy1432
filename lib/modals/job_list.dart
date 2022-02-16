class Item {
  final num id;
  final String name;
  final String image;
  final String salary;
  final String color;
  final String cumpani;
  final String time;

  Item({
    required this.id,
    required this.name,
    required this.image,
    required this.salary,
    required this.color,
    required this.cumpani,
    required this.time,
  });
}

class JobCart {
  static final items = [
    Item(
        id: 1,
        name: "Flutter UI/UX",
        time: "Full-Time",
        cumpani: "Nike inc",
        salary: "\$40/h",
        color: "#000000",
        image: "assets/images/nike.jpg"),
    Item(
        id: 2,
        name: "Flutter Devloper",
        time: "Part-time",
        cumpani: "Amazon inc.",
        salary: "\$60/h",
        color: "#000000",
        image: "assets/images/amazon.jpg"),
    Item(
        id: 3,
        name: "Lead UI Designer",
        time: "Full-time",
        cumpani: "Apple inc.",
        salary: "\$80/h",
        color: "#000000",
        image: "assets/images/iphone.jpg"),
    Item(
        id: 4,
        name: "UI/Ux Devlopper",
        time: "Part-time",
        cumpani: "Google LLC.",
        salary: "\$85/h",
        color: "#000000",
        image: "assets/images/google.jpg"),
    Item(
        id: 5,
        name: "Java Devloper",
        time: "Full-time",
        cumpani: "Swiggy inc.",
        salary: "\$45/h",
        color: "#000000",
        image: "assets/images/swiggy.jpg"),
    Item(
        id: 6,
        name: "Product Desingner",
        time: "Part-time",
        cumpani: "UberEats inc.",
        salary: "\$55/h",
        color: "#000000",
        image: "assets/images/uberEats2.jpg"),
  ];
}
