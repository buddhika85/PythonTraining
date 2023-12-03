import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

/*
# IITC001 Introduction to Technical Communication
# IIIS001 Introduction to Information Systems
# IPRO001 Programming 1
# IWBS001 Web Systems
# IBRM001 Business Requirements Modelling *
# IPRO002 Programming 2 **
# INEF001 Network Fundamentals
# IDBF001 Database Fundamentals **

{'accelerated': 3, 'standard': 3, 'extended': 2}
{21: 2, 19: 2, 18: 2, 20: 1, 17: 1}
Introduction to Technical Communication: 0
Introduction to Information Systems: 3
Programming 1: 0
Web Systems: 5
Business Requirements Modelling: 5
Programming 2: 0
Network Fundamentals: 0
Database Fundamentals: 3
 */
public class UTSCollegeIT {
        public static void main(String[] args) {
                try {
                        Student[] students = ITStudentData.studentData;
                        HashMap<String, Integer> courseCount = new HashMap<>();
                        HashMap<Integer, Integer> ageByCount = new HashMap<>();
                        HashMap<String, Integer> unitByCount = new HashMap<>();
                        unitByCount.put("Introduction to Technical Communication", 0);
                        unitByCount.put("Introduction to Information Systems", 0);
                        unitByCount.put("Programming 1", 0);
                        unitByCount.put("Web Systems", 0);
                        unitByCount.put("Business Requirements Modelling", 0);
                        unitByCount.put("Programming 2", 0);
                        unitByCount.put("Network Fundamentals", 0);
                        unitByCount.put("Database Fundamentals", 0);

                        for (Student student : students) {
                                // course
                                if (courseCount.containsKey(student.course))
                                        courseCount.put(student.course, courseCount.get(student.course) + 1);
                                else
                                        courseCount.put(student.course, 1);
                                // age
                                if (ageByCount.containsKey(student.age))
                                        ageByCount.put(student.age, ageByCount.get(student.age) + 1);
                                else
                                        ageByCount.put(student.age, 1);

                                // unit counts
                                for (String unitCode : student.enrolledSubjects) {
                                        switch (unitCode) {
                                                case "IITC001":
                                                        unitByCount.put("Introduction to Technical Communication",
                                                                        unitByCount.get("Introduction to Technical Communication")
                                                                                        + 1);
                                                        break;
                                                case "IIIS001":
                                                        unitByCount.put("Introduction to Information Systems",
                                                                        unitByCount.get("Introduction to Information Systems")
                                                                                        + 1);
                                                        break;
                                                case "IPRO001":
                                                        unitByCount.put("Programming 1",
                                                                        unitByCount.get("Programming 1") + 1);
                                                        break;
                                                case "IWBS001":
                                                        unitByCount.put("Web Systems",
                                                                        unitByCount.get("Web Systems")
                                                                                        + 1);
                                                        break;
                                                case "IBRM001":
                                                        unitByCount.put("Business Requirements Modelling",
                                                                        unitByCount.get("Business Requirements Modelling") + 1);
                                                        break;
                                                case "IPRO002":
                                                        unitByCount.put("Programming 2",
                                                                        unitByCount.get("Programming 2") + 1);
                                                        break;
                                                case "INEF001":
                                                        unitByCount.put("Network Fundamentals",
                                                                        unitByCount.get("Network Fundamentals") + 1);
                                                        break;
                                                case "IDBF001":
                                                        unitByCount.put("Database Fundamentals",
                                                                        unitByCount.get("Database Fundamentals") + 1);
                                                        break;
                                        }
                                }
                        }
                        System.out.println(courseCount);
                        System.out.println(ageByCount);
                        System.out.println(unitByCount);
                } catch (Exception e) {
                        System.out.println(e.getMessage());
                }
        }
}

class Student {
        String name;
        int studentNumber;
        String course;
        int age;
        ArrayList<String> enrolledSubjects;

        public Student(String name, int studentNumber, String course, int age, ArrayList<String> enrolledSubjects) {
                this.name = name;
                this.studentNumber = studentNumber;
                this.course = course;
                this.age = age;
                this.enrolledSubjects = enrolledSubjects;
        }
}

class ITStudentData {
        public static Student[] studentData = {
                        new Student("Thomas Munster", 34534, "accelerated", 21,
                                        new ArrayList<>(Arrays.asList("IIIS001", "IAPP001", "INET001", "IDBF001"))),
                        new Student("John Smith", 1111, "standard", 19,
                                        new ArrayList<>(Arrays.asList("IWBS001", "IBRM001", "IAPP001"))),
                        new Student("Sarah Johnson", 2222, "accelerated", 18,
                                        new ArrayList<>(Arrays.asList("IBRM001", "IAPP001", "INET001", "IDBF001"))),
                        new Student("Emily Davis", 3333, "extended", 20,
                                        new ArrayList<>(Arrays.asList("IWBS001", "IIIS001", "IAPP001"))),
                        new Student("Michael Thompson", 4444, "standard", 17,
                                        new ArrayList<>(Arrays.asList("IWBS001", "IBRM001", "IPRG001"))),
                        new Student("Jessica Brown", 5555, "accelerated", 21,
                                        new ArrayList<>(Arrays.asList("IBRM001", "IAPP001", "INET001", "IDBF001"))),
                        new Student("Daniel Wilson", 6666, "extended", 19,
                                        new ArrayList<>(Arrays.asList("IWBS001", "IBRM001", "IPRG001"))),
                        new Student("Olivia Miller", 7777, "standard", 18,
                                        new ArrayList<>(Arrays.asList("IWBS001", "IIIS001", "IAPP001")))
        };
}