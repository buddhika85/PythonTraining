class MenuItem
{
    private String name, category;
    private double price;

    public MenuItem(String name, String category, double price) {
        this.name = name;
        this.category = category;
        this.price = price;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    
    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}

class BeefMenuItem  extends MenuItem
{
    public BeefMenuItem(String name, double price) {
        super(name, "Beef", price);
    }
}

class ChickenMenuItem  extends MenuItem
{
    public ChickenMenuItem(String name, double price) {
        super(name, "Chicken", price);
    }
}

class BeefBurger extends BeefMenuItem
{
    public BeefBurger(double price) {
        super("Beef Burger", price);
    }
}

class ChickenNuggets  extends ChickenMenuItem
{
    public ChickenNuggets(double price) {
        super("Chicken Nuggets", price);
    }
}

public class MenuItemSystem
{
    public static void main(String[] args) {
        BeefBurger beefBurger = new BeefBurger(500);
        ChickenNuggets chickenNuggets = new ChickenNuggets(300);
        System.out.println(beefBurger.getName());
        System.out.println(chickenNuggets.getName());
    } 
}