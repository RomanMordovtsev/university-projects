package tr.edu.ozyegin.cs101.blackbox;

import java.util.Arrays;

public class BlackBox {
    private final Location[] ballLocations;

    public BlackBox(Location ballOne, Location ballTwo, Location ballThree, Location ballFour) {
        Location[] balls = new Location[]{ballOne, ballTwo, ballThree, ballFour};

        for (Location loc : balls) {
            if (loc == null) {
                throw new IllegalArgumentException("Ball location cannot be null.");
            }
        }

        long uniqueCount = Arrays.stream(balls).distinct().count();
        if (uniqueCount < 4) {
            throw new IllegalArgumentException("Ball locations must be unique.");
        }

        this.ballLocations = balls;
    }

    public boolean ballExistsInLocation(Location location) {
        if (location == null) return false; // 🔧 null kontrolü eklendi
        return Arrays.stream(ballLocations).anyMatch(location::equals);
    }

    public boolean laserEntryExitMatches(EdgeLocation entry, EdgeLocation exit) {
        Laser laser = new Laser(entry);
        EdgeLocation actualExit = laser.findExitEdgeLocation(this);
        return (exit == null) ? (actualExit == null) : exit.equals(actualExit);
    }

    @Override
    public String toString() {
        StringBuilder buf = new StringBuilder();
        for (int i = 0; i < 64; i++) {
            if (this.ballExistsInLocation(Location.locationFromLinearPosition(i))) {
                buf.append("*");
            } else {
                buf.append(".");
            }
            if (i % 8 == 7) buf.append("\n");
        }
        return buf.toString();
    }
}