import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class StudentManagement {
    private static ArrayList<Student> students = new ArrayList<>();
    public static void main(String[] args) {
        addStudent(1, "John Smith", 18);
        addStudent(2, "James Gunn", 19);
        addGradeForStudent(1, "Prog1", 90.0);
        addGradeForStudent(1, "Prog2",86.0);
        double avg = calculateAverageGrade(1);
        System.out.println("Average is : " + avg) ;
        printStudentDetails(1);
        printStudentDetails(2);
    }

    private static void addStudent(int id, String name, int age)
    {
        students.add(new Student(name, id, name, age, new ArrayList<>()));
    }

    private static void addGradeForStudent(int id, String subject, double grade)
    {
        Student studentById = findById(id);
        if (studentById == null)
        {
            System.out.println("-------------Error - no student with student ID " + id);
        }
        else
        {
            if (!studentById.enrolledSubjects.contains(subject))
            {
                studentById.enrolledSubjects.add(subject);
            }
            studentById.addGrade(subject, grade);
        }
    }

    private static Student findById(int id) {
        for (Student student : students) {
            if (student.studentNumber == id)
                return student;
        }
        return null;
    }

    private static double calculateAverageGrade(int id)
    {
        Student studentById = findById(id);
        if (studentById == null)
        {
            System.out.println("-------------Error - no student with student ID " + id);
            return -1;
        }
        else
        {
            return studentById.getAverageGrade();
        }
    }

    private static void printStudentDetails(int id)
    {
        Student studentById = findById(id);
        if (studentById == null)
        {
            System.out.println("-------------Error - no student with student ID " + id);          
        }
        else
        {
            System.out.println(studentById.toString());
        }
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
            double total = 0.0;
            for (Map.Entry<String, Double> entry : grades.entrySet()) {
                total += entry.getValue();
            }
            return total / grades.size();
        }

        @Override
        public String toString() {
            var str = "Student " +  name  + " ID: " + studentNumber + " Age: " + age + " Enrolled to : " + enrolledSubjects;
            for (Map.Entry<String, Double> entry :grades.entrySet()) {
                str += "\n" + entry.getKey() + " - " + entry.getValue() + "%";
            }
            return str;
        }
}

