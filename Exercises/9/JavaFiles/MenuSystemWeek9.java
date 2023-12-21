package JavaFiles;

import java.util.ArrayList;

class MenuItem {
    private String name, category;

    private double price;

    public MenuItem(String name, String category, double price) {
        // this.name = name;
        // this.category = category;
        // this.price = price;
        setName(name);
        setCategory(category);
        setPrice(price);
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public String getCategory() {
        return category;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String toString()
    {
        return name + "\n\tCategory: " + category + "\n\tPrice: " +  price;
    }
}

class BeefMenuItem extends MenuItem
{
    public BeefMenuItem(String name, double price)
    {
        super(name, "Beef", price);
    }
}

class ChickenMenuItem extends MenuItem
{
    public ChickenMenuItem(String name, double price)
    {
        super(name, "Chicken", price);
    }
}

class BeefBurger extends BeefMenuItem
{
    private boolean isKetchupIncluded;

    public BeefBurger(double price, boolean isKetchupIncluded)
    {
        super("Beef Burger",  price);
        this.isKetchupIncluded = isKetchupIncluded;
    }

    public boolean isKetchupIncluded() {
        return isKetchupIncluded;
    }

    public void setKetchupIncluded(boolean isKetchupIncluded) {
        this.isKetchupIncluded = isKetchupIncluded;
    }

    
    @Override
    public String toString() {
        
        return super.toString() +  "\n\tIs Ketchup Included: " +  isKetchupIncluded;
    }
}

class ChickenNuggets extends ChickenMenuItem
{
    private String wayToPrepare;

    public ChickenNuggets(double price, String wayToPaprepare)
    {
        super("Chicken Nuggets",  price);
        this.wayToPrepare = wayToPaprepare;
    }

    public String getWayToPrepare() {
        return wayToPrepare;
    }

    public void setWayToPrepare(String wayToPrepare) {
        this.wayToPrepare = wayToPrepare;
    }

    @Override
    public String toString() {
        
        return super.toString() +  "\n\tWay prepated: " +  wayToPrepare;
    }
}

class Order
{
    private ArrayList<MenuItem> menuItems = new ArrayList<>();

    public void addItem(MenuItem item)
    {
        menuItems.add(item);
    }

    @Override
    public String toString() {
        String str = "Order Details\n";
        for (MenuItem menuItem : menuItems) {
            str += menuItem + "\n";
        }
        return str;
    }
}

public class MenuSystemWeek9 {
    public static void main(String[] args) {
        // System.out.println("---- Menu ----");
        // BeefBurger beefBurger = new BeefBurger(500, false);
        // ChickenNuggets chickenNuggets = new ChickenNuggets(300, "Fried");
        // System.out.println(beefBurger);
        // System.out.println(chickenNuggets);

        // // using mutators to change state/attributes of the object
        // beefBurger.setPrice(1000);
        // beefBurger.setKetchupIncluded(true);
        // chickenNuggets.setPrice(600);
        // chickenNuggets.setWayToPrepare("Baked");

        // System.out.println("After updating using mutators\n---- Menu ----");
        // System.out.println(beefBurger);
        // System.out.println(chickenNuggets);

        Order order = new Order();
        order.addItem(new ChickenNuggets(300, "Fried"));
        order.addItem(new BeefBurger(500, false));
        System.out.println(order);
    }
}