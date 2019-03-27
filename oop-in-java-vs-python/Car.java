/**
 * Car class
 * 
 * Used for the Real Python OOP in Java vs Python article
 * 
 * Requires both Vehicle.java and Device.java
 */

public class Car extends Vehicle implements Device {

    private int year; // Year of our car
    private int voltage; // Battery voltage
    private static int wheels; // How many wheels do we have

    /**
     * Car constructor
     */
    public Car(String color, String model, int year) {
        super(color, model);
        this.year = year;
        this.voltage = 12;
    }

    /**
     * Override the interface method.
     */
    @Override
    public int getVoltage() {
        return voltage;
    }

    /**
     * getYear returns the Car's year
     */
    public int getYear() {
        return year;
    }

    /**
     * setYear changes Car's year
     */
    public void setYear(int year) {
        this.year = year;
    }

    /**
     * getWheels returns the number of wheels
     */
    public static int getWheels() {
        return wheels;
    }

    /**
     * setWheels sets the number wheels
     */
    public static void setWheels(int count) {
        wheels = count;
    }

    /**
     * Return a human readable string reoresenting the Car
     */
    public String toString() {
        return "Car: " + getColor() + " : " + getModel() + " : " + getYear();
    }
}