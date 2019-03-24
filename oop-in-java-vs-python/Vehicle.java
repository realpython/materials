/**
 * Vehicle class
 * 
 * Used for the Real Python OOP in Java vs Python article
 * 
 * Implements basic functionality for our Vehicle
 */
public class Vehicle {

    private String color; // What color are we?
    private String model; // What model vehicle are we?

    /**
     * Vehicle constructor
     */
    public Vehicle(String color, String model) {
        this.color = color;
        this.model = model;
    }

    /**
     * getColor returns the Vehicles color
     */
    public String getColor() {
        return color;
    }

    /**
     * getModel returns the Vehicles model
     */
    public String getModel() {
        return model;
    }

}