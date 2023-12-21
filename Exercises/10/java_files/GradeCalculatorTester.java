import java.util.ArrayList;
import java.util.InputMismatchException;

public class GradeCalculatorTester {
    public static void main(String[] args) {
        new GradeCalculator().enterUserInfo();
    }
}

class GradeCalculator {

    private ArrayList<SubjectGrade> grades = new ArrayList<>();

    private void addSubject(String name, double grade) {
        grades.add(new SubjectGrade(name, grade));
    }

    public void enterUserInfo() {
        boolean exit = false;
        while (!exit) {
            System.out.println("Enter subject name (or type 'EXIT' to stop): ");
            String input = In.nextLine().toUpperCase();
            if (input.equals("EXIT")) {
                displaySummary();
                exit = true;
            } else {
                double grade = readGrade(input);
                addSubject(input, grade);
            }
        }
    }

    private double readGrade(String subject) {
        while (true) {
            System.out.println("What was your grade for " + subject + "? ");
            try {
                double grade = Double.parseDouble(In.nextLine());
                if (grade < 0 || grade > 100)
                    throw new IllegalArgumentException("grade should be between 0 to 100");
                return grade;
            } catch (IllegalArgumentException e) {
                System.out.println("Invalid Input: 0 to 100");
            }

        }
    }

    private void displaySummary() {
        System.out.println("Your grade summary ----------------");
        if (grades.size() == 0) {
            System.out.println("\tNo grades found");
            return;
        }
        double total = 0;
        for (SubjectGrade subjectGrade : grades) {
            System.out.println("\t- " + subjectGrade.name + ": " + subjectGrade.grade + " marks");
            total += subjectGrade.grade;
        }
        System.out.println("Your average grade is " + (total / grades.size()));
    }
}

class SubjectGrade {
    String name;
    double grade;

    SubjectGrade(String name, double grade) {
        this.name = name;
        this.grade = grade;
    }
}