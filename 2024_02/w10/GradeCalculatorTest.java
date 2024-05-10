import java.util.ArrayList;

public class GradeCalculatorTest
{
    public static void main(String[] args) 
    {
        GradeCalculator gradeCalculator =  new GradeCalculator();
        gradeCalculator.enterUserInfo();
        gradeCalculator.displaySummary();
    }
}

class GradeCalculator 
{
    private ArrayList<SubjectGrade> grades = new ArrayList<>();

    public void addSubject(String name, double grade)
    {
        grades.add(new SubjectGrade(name, grade));
    }
  
    public void enterUserInfo()
    {
        while(true)
        {
            try
            {
                System.out.println("Enter subject name (or type 'EXIT' to stop): ");
                String subjectName = In.nextLine().toUpperCase();
                if (subjectName.equals("EXIT"))
                {
                    break;      // will exit the loop
                }

                System.out.println("What was your grade for " + subjectName + "?");
                double grade = Double.parseDouble(In.nextLine());
                if (grade < 0 || grade > 100)
                {
                    // will jump to catch block
                    throw new IllegalArgumentException("Invalid grade - " + grade + ", Provide 0 to 100 value");
                }

                // if it reaches this line subject and grade are valid
                addSubject(subjectName, grade);
            }           
            catch(IllegalArgumentException exception)
            {
                System.out.println("Error - " +  exception.getMessage());
            }            
        }
    }

    public void displaySummary() 
    {
        System.out.println("Your grade summary ----------------");
        if (grades.isEmpty())
        {
            System.out.println("\tNo grades to display");
            return;
        }

        double total = 0.0;
        for (SubjectGrade subjectGrade : grades) 
        {
            System.out.println("\t- " + subjectGrade.name + ": " + subjectGrade.grade + " marks.");
            total += subjectGrade.grade;
        }
        System.out.println("\nYou average grade is " + (total / grades.size()));
    }

}

class SubjectGrade 
{
    String name;
    double grade;

    SubjectGrade(String name, double grade) 
    {
        this.name = name;
        this.grade = grade;
    }
}