package JavaFiles;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class UTSCollegeIT {
    public static void main(String[] args) {
        
    }
}

class Student {
    String name;
    int studentNumber;
    String course;
    int age;
    ArrayList<String> enrolledSubjects;
    HashMap<String, Double> grades = new HashMap<>();

    public Student(String name, int studentNumber, String course, int age, ArrayList<String> enrolledSubjects) {
        this.name = name;
        this.studentNumber = studentNumber;
        this.course = course;
        this.age = age;
        this.enrolledSubjects = enrolledSubjects;
    }

    public void addGrade(String subject, double grade)
    {
        grades.put(subject, grade);
    }

    public double getAverageGrade()
    {
        double total  = 0.0;
        for(Map.Entry<String, Double> entry : grades.entrySet())
        {
            total += entry.getValue();
        }
        return total / grades.size();
    }

    @Override
    public String toString() {
        String str = "Student: " + name + ", ID: " + studentNumber + ", age: " + age + ", course: " +
                course;
        str += "\nEnrolled Units";
        if (enrolledSubjects.size() == 0)
            str += "\n\tNo units";
        else
            for (String subject : enrolledSubjects) {
                str += "\n\t" + subject;
            }
        str += "\nGrades";
        if (grades.size() == 0)
            str += "\n\tNo grades";
        else
            for (Map.Entry<String, Double> pair : grades.entrySet()) {
                str += "\n\t" + pair.getKey() + " = " + pair.getValue() + "%";
            }
        return str;
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