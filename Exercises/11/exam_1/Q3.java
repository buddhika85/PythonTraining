package exam_1;

public class Q3 {
    public static void main(String [] args)
	{
		System.out.println("Choose either 3 or 4:");
		int input = In.nextInt();
		if (input == 3)
		{
			System.out.println("Thirsty 3rd");
		}
		else if (input == 4)
		{
			System.out.println("Famished 4th");
		}
		else
		{
			System.out.println("Hmmm");
		}
	}
}
