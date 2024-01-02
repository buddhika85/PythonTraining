import java.util.HashMap;
import java.util.Map.Entry;

class BubbleTea
{
	private String name;
	HashMap<String, Integer> toppings =
		new HashMap<>();

	public void addTopping(String toppingName, int quantity)
	{
		toppings.put(toppingName, quantity);
	}
}


public class q11_c
{
	public static void main(String [] args)
	{
		BubbleTea bt = new BubbleTea();
		bt.addTopping("Cream", 10);
		bt.addTopping("Lime", 5);
		bt.addTopping("Cream", 20);	

		for(Entry<String, Integer> et : bt.toppings.entrySet())
		{
			System.out.println(et.getKey() + " " + et.getValue());
		}	
	}
}

