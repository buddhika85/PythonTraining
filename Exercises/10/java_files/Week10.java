import java.util.InputMismatchException;

public class Week10 {
    public static void main(String[] args) {
        ExploreExceptions e = new ExploreExceptions();
        e.readInteger();
    }
}

class ExploreExceptions {
    void readInteger() {
        int number;

        while (true) {
            try {
                System.out.print("Enter an integer: ");
                number = In.nextInt();
                break; // Exit the loop if the input is successfully converted to an integer
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter an integer!");
            }
        }

        // Now you can proceed with the 'number' variable containing a valid integer.
        System.out.println("You entered: " + number);
    }
}