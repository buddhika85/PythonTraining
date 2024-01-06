package exam_1;

import java.util.HashMap;

public class Q11 {
    private String name;
	private HashMap<String,Integer> toppings = new HashMap<>();
	
	public void addTopping(String toppingName, int quantity)
	{
		toppings.put(toppingName, quantity);
	}
}
