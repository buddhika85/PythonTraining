class UberCar {
    String model;
    String licensePlate;
    boolean isAvailable;
    double earnings;

    UberCar(String model, String licensePlate) {
        this.model = model;
        this.licensePlate = licensePlate;
        this.isAvailable = true;
        this.earnings = 0.0;
    }

    void driveTo(double distance) {
        if (this.isAvailable) {
            System.out.println("Driving " + distance + " kilometers.");
            earnings += calculateFare(distance);
        } else {
            System.out.println("This Uber car is currently unavailable.");
        }
    }

    double calculateFare(double distance) {
        // Assume a simple fare calculation based on distance
        return distance * 1.5;
    }

    void setAvailability(boolean availability) {
        this.isAvailable = availability;
        if (this.isAvailable) {
            System.out.println("This Uber car is now available.");
        } else {
            System.out.println("This Uber car is now unavailable.");
        }
    }

    public String toString() {
        return "Model: " + this.model
                + ", License Plate: " + this.licensePlate
                + ", Is available: " + this.isAvailable
                + ", Earnings: $" + this.earnings;
    }
}