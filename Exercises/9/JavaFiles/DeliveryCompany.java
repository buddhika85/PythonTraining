package JavaFiles;

import java.util.ArrayList;

public class DeliveryCompany
{
    public static void main(String[] args) {
        /*
         Delivery Company
OLD TRUCK Consumed 1.3888888888888888 litres
NEW TRUCK Consumed 0.8849557522123893 litres
         */
        System.out.println("Delivery Company");
        // OldTruck oldTruck = new OldTruck(7.2, 80);
        // NewTruck newTruck = new NewTruck(11.3, 100);
        // oldTruck.makeDelivery(10);
        // newTruck.makeDelivery(10);

        var trucks = new ArrayList<Truck>();
        trucks.add(new OldTruck(7.2, 80));
        trucks.add(new NewTruck(11.3, 100));
        for (Truck truck : trucks) {
            truck.makeDelivery(10);
        }
    }
}

class Truck
{
    protected double fuelEfficiency;
    protected double capacity;

    public Truck(double fuelEfficiency, double capacity) {
        this.fuelEfficiency = fuelEfficiency;
        this.capacity = capacity;
    }

    public void makeDelivery(double distanceTravelled)
    {
        System.out.println("Consumed " + (distanceTravelled / fuelEfficiency) + " litres");
    }   
}

class OldTruck extends Truck
{
    private final String TYPE = "OLD TRUCK ";
    public OldTruck(double fuelEfficiency, double capacity) {
        super(fuelEfficiency, capacity);       
    }  
    
    @Override
    public void makeDelivery(double distanceTravelled)
    {
        System.out.print(TYPE);       
        super.makeDelivery(distanceTravelled);
    }  
}

class NewTruck extends Truck
{
    private final String TYPE = "NEW TRUCK ";
    public NewTruck(double fuelEfficiency, double capacity) {
        super(fuelEfficiency, capacity);       
    }  

    @Override
    public void makeDelivery(double distanceTravelled)
    {
        System.out.print(TYPE);
        super.makeDelivery(distanceTravelled);
    }  
}