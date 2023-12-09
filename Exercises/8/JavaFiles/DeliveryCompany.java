class DeliveryCompany
{
    public static void main(String[] args) {
        new OldTruck(7.2, 80).makeDelivery(10);
        new NewTruck(11.3, 100).makeDelivery(10);
    }
}

abstract class  Truck
{
    protected double fuelEfficiency;
    protected double fuelCapacity;
    public Truck(double fuelEfficiency, double fuelCapacity) {
        this.fuelEfficiency = fuelEfficiency;
        this.fuelCapacity = fuelCapacity;
    }
    public abstract void makeDelivery(double distanceTravelled);
}

class OldTruck extends Truck
{
    public OldTruck(double fuelEfficiency, double fuelCapacity) {
        super(fuelEfficiency, fuelCapacity);
    }
    @Override
    public void makeDelivery(double distanceTravelled) {
        System.out.println(distanceTravelled / fuelEfficiency);
    }

}

class NewTruck extends Truck
{
    public NewTruck(double fuelEfficiency, double fuelCapacity) {
        super(fuelEfficiency, fuelCapacity);
    }
    @Override
    public void makeDelivery(double distanceTravelled) {
        System.out.println(distanceTravelled / fuelEfficiency);
    }
}