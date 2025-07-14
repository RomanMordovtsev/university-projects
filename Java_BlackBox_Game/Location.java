package tr.edu.ozyegin.cs101.blackbox;

import java.util.Objects;

public class Location {

    private final static int MAX = 63;
    private final int n;

    private Location(int n) {
        this.n = n;
    }

    public static Location locationFromLinearPosition(int n) {
        if (n < 0 || n > MAX) {
            return null;
        }
        return new Location(n);
    }

    public static Location locationFromString(String location) {
        if (location.length() != 2) {
            throw new IllegalArgumentException("Location string length must be 2.");
        }

        int row = location.charAt(0) - 'A';
        int column = location.charAt(1) - '1';

        return locationFromLinearPosition(8 * row + column);
    }

    public static Location locationFromRowAndColumn(int row, int column) {
        if (row < 0 || row > 7 || column < 0 || column > 7) {
            return null;
        }

        return locationFromLinearPosition(8 * row + column);
    }

    public int getRow() {
        return this.n / 8;
    }

    public int getColumn() {
        return this.n % 8;
    }

    public int getN() {
        return this.n;
    }

    @Override
    public String toString() {
        return "" + (char)(this.getRow() + 'A') + (char)(this.getColumn() + '1');
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Location other = (Location) o;
        return this.n == other.n;
    }

    @Override
    public int hashCode() {
        return Objects.hash(n);
    }

    public Location locationTowards(Direction direction) {
        return locationFromRowAndColumn(this.getRow() + direction.getDeltaRow(), this.getColumn() + direction.getDeltaColumn());
    }
}