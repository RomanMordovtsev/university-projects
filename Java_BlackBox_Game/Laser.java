package tr.edu.ozyegin.cs101.blackbox;

public class Laser {
    private Location current;
    private Location next;
    private Direction direction;
    private final EdgeLocation firedFrom;

    public Laser(EdgeLocation firedFrom) {
        this.firedFrom = firedFrom;
        this.current = null;
        this.next = firedFrom.getAdjacentLocation();
        this.direction = firedFrom.getDirectionToAdjacentLocation();
    }

    public EdgeLocation findExitEdgeLocation(BlackBox blackBox) {
        while (true) {
            if (this.next == null) {
                return EdgeLocation.getEdgeLocationAdjacentTo(this.current, this.direction);
            }

            boolean ballDeadAhead = blackBox.ballExistsInLocation(this.next);
            boolean ballToTheRightAhead = blackBox.ballExistsInLocation(this.next.locationTowards(this.direction.right()));
            boolean ballToTheLeftAhead = blackBox.ballExistsInLocation(this.next.locationTowards(this.direction.left()));

            if (ballDeadAhead) {
                return null;
            } else if (ballToTheLeftAhead && ballToTheRightAhead) {
                return this.firedFrom;
            } else if (ballToTheRightAhead) {
                if (this.current == null) {
                    return this.firedFrom;
                } else {
                    this.direction = this.direction.left();
                    this.next = this.current.locationTowards(this.direction);
                }
            } else if (ballToTheLeftAhead) {
                if (this.current == null) {
                    return this.firedFrom;
                } else {
                    this.direction = this.direction.right();
                    this.next = this.current.locationTowards(this.direction);
                }
            } else {
                this.current = this.next;
                this.next = this.next.locationTowards(this.direction);
            }
        }
    }
}