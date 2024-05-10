import java.util.ArrayList;
import java.util.Arrays;
import java.util.InputMismatchException;

public class Week10 
{
    public static void main(String[] args) 
    {
        ExploreExceptions e = new ExploreExceptions();
        e.readInteger();

        //e.arrayIndexException();
        //e.arrayListIndexException();
    }
}

class ExploreExceptions 
{

     void readIntegerError() {
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

    void readInteger() 
    {
        int number;
        while (true) 
        {
            try 
            {
                System.out.print("Enter an integer: ");
                // number = In.nextInt();
                number = Integer.parseInt(In.nextLine());
                break; // Exit the loop if the input is successfully converted to an integer
            } 
            catch (NumberFormatException e) 
            {
                System.out.println("Invalid input. Please enter an integer! - NumberFormatException");
            }
        }

        // Now you can proceed with the 'number' variable containing a valid integer.
        System.out.println("You entered: " + number);
    }


    void arrayIndexException() {
        try {
            // Creating an array (Java equivalent of a list)
            int[] myArray = { 10, 20, 30, 40, 50 };

            // Trying to access an out-of-range index
            int value = myArray[10];
        } catch (ArrayIndexOutOfBoundsException e) {
            // Handling the ArrayIndexOutOfBoundsException
            System.out.println("ArrayIndexOutOfBoundsException: The specified index is out of range.");
        }
    }

    void arrayListIndexException () {
        try {
            // Creating an arraylist       
            ArrayList<Integer> arraylist = new ArrayList<>(Arrays.asList(0, 20, 30, 40, 50));

            // Trying to access an out-of-range index
            int value = arraylist.get(10);
        } catch (IndexOutOfBoundsException e) {
            // Handling the IndexOutOfBoundsException
            System.out.println("IndexOutOfBoundsException: The specified index is out of range.");
        }
    }

    void handleMultipleExceptions() {
        try {
            int[] myArray = { 10, 20, 30, 40, 50 };

            System.out.print("Enter an index for array indexing: ");
            int index = In.nextInt();

            int value = myArray[index];

            System.out.println("Value at index " + index + " is: " + value);
        } catch (InputMismatchException e) {
            System.out.println("Invalid input. Please enter a valid integer.");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Index out of range. Please enter a valid index within the range of the array.");
        }
    }

    void bankWithdrawalExample() {
        try {
            System.out.print("How much do you want to withdraw? ");
            double amountToWithdraw = In.nextDouble();

            if (amountToWithdraw <= 0) {
                throw new IllegalArgumentException("You must withdraw a positive amount!");
            }
        } catch (InputMismatchException e) {
            System.out.println("Invalid input. Please enter a valid double."); 
        } catch (IllegalArgumentException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}