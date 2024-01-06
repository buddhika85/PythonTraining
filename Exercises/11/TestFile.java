import java.util.ArrayList;

public class TestFile
{
    public static void main(String [] args)
    {
        ArrayList<Integer> nums = new ArrayList<>();
        nums.add(1);
        nums.add(2);
        System.out.println(nums);
        nums.set(0, 3);
        System.out.println(nums);
        System.out.println("index 0: " + nums.get(0));
        //nums.remove(3);
        boolean removed = nums.remove(Integer.valueOf(3));
        System.out.println(nums);
    }
}