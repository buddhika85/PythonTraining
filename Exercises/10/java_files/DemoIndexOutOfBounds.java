import java.util.ArrayList;
import java.util.Arrays;

public class DemoIndexOutOfBounds
{
    public static void main(String[] args) {
        try {
            ArrayList<Integer> nums = new ArrayList<>();
            nums.addAll(Arrays.asList(10,20,30,40));
            System.out.println("Value at index " + 10 + " is: " + nums.get(10));
        } catch (IndexOutOfBoundsException e) {
            System.out.println("IndexOutOfBoundsException: The specified index is out of range. " + e.getMessage());
        }
    }
}