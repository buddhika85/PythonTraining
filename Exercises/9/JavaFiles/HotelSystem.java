import java.util.ArrayList;

class Room{
    protected int id, headCount;
    protected String status, bedType;
    protected double pricePerDay;

    public Room(int id, int headCount, String bedType, double pricePerDay) {
        this.id = id;
        this.headCount = headCount;
        this.status = "Available";
        this.bedType = bedType;
        this.pricePerDay = pricePerDay;
    }

    public void book()
    {
        if (status.equals("Available"))
        {
            status = "Booked";
            System.out.println("Room Booked");
        }
        else
            System.out.println("Error - Room is unavailable for booking");
    }

    public void unbook()
    {
        if (status.equals("Booked"))
        {
            status = "Available";
            System.out.println("Room unbooked. - now available");
        }
        else
            System.out.println("Error - Room not booked to cancel the booking");
    }

    public void checkIn()
    {
        if (status.equals("Booked"))
        {
            status = "Checked-In";
            System.out.println("Room checked in");
        }
        else
            System.out.println("Error - Room not booked to check in");
    }

    public void checkOut()
    {
        if (status.equals("Checked-In"))
        {
            status = "Available";
            System.out.println("Room checked out. - now available");
        }
        else
            System.out.println("Error - Room not checked in to check out");
    }

    public double calcPrice(int dayCount)
    {
        return pricePerDay * dayCount;
    }

    public String toString()
    {
        return "ID: " + id + ", Status: " + status + ", bed-type: " + bedType + 
            ", head-count: " + headCount + ", price per day: " + pricePerDay;
    }
}

class StandardRoom extends Room {
    public StandardRoom(int id) {
        super(id, 2, "Double", 10000);
    }

    public String toString()
    {
        return "Standard Room: " +  super.toString();
    }
}

class DeluxRoom extends Room {
    private String view;
    private String[] additionalAmenities = new String[] 
        {"bath tub", "minibar", "smartTV", "electronic SafeBox"};
    private double additionalMealPrice = 1000;
    private int additionalMealCount;

    public DeluxRoom(int id, String view) {
        super(id, 4, "King", 20000);
        this.view = view;
    }

    public void requestMeal()
    {
        ++additionalMealCount;
    }

    public double calcPrice(int dayCount)
    {
        return super.calcPrice(dayCount) + (additionalMealPrice * additionalMealCount);
    }

    public String toString()
    {
        String str = "Delux Room: " +  super.toString() + 
            "View: " + view +
            ", additional meals: " + additionalMealCount +
            ", additional meal price: " +  additionalMealPrice;
        str += "Features: [";
        for (String feature : additionalAmenities) {
            str += feature + ", ";
        }
        str += "]";
        return str;
    }
}

class Hotel
{
    private ArrayList<Room> rooms = new ArrayList<>();
    public void addRoom(Room room)
    {
        rooms.add(room);
    }

    @Override
    public String toString() {
        String str = "All Rooms\n";
        for (Room room : rooms) {
            str += room + "\n";
        }
        return str;
    }
}

public class HotelSystem {
    public static void main(String[] args) {
        // System.out.println("Hotel System");
        // StandardRoom standardRoom = new StandardRoom(1);
        // standardRoom.book();
        // standardRoom.checkIn();
        // System.out.println(standardRoom);
        // standardRoom.checkOut();
        // System.out.println("Price for 2 days = " + standardRoom.calcPrice(2));
        
        // System.out.println("\n");
        // DeluxRoom deluxRoom = new DeluxRoom(2, "River View");
        // deluxRoom.book();
        // deluxRoom.checkIn();
        // deluxRoom.requestMeal();
        // deluxRoom.requestMeal();
        // System.out.println(deluxRoom);
        // deluxRoom.checkOut();
        // System.out.println("Price for 2 days = " + deluxRoom.calcPrice(2));
        var hotel = new Hotel();
        hotel.addRoom(new StandardRoom(1));
        hotel.addRoom( new DeluxRoom(2, "River View"));
        System.out.println(hotel);
    }
}
