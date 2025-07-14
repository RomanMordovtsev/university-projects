package tr.edu.ozyegin.cs101.blackbox;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Game {

    public record LaserFire(EdgeLocation entry, EdgeLocation exit) {}

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<LaserFire> laserData = new ArrayList<>();
        List<BlackBox> possibleSolutions = BlackBoxStream.streamBlackBoxes().toList();

        System.out.println("Remaining possibilities " + possibleSolutions.size());

        List<Integer> availableEntries = new ArrayList<>();
        for (int i = 1; i <= 32; i++) {
            availableEntries.add(i);
        }

        // Фиксированный первый выстрел = 2
        int entryId = 2;
        if (availableEntries.contains(entryId)) {
            availableEntries.remove(Integer.valueOf(entryId));
            EdgeLocation entry = EdgeLocation.getEdgeLocationWithId(entryId);

            System.out.println("I press button " + entryId);
            System.out.print("Where does it exit? (H = hit, R = reflection, number = exit edge)\n> ");
            String exitInput = scanner.next();

            EdgeLocation exit = parseExitInput(exitInput, entry);
            laserData.add(new LaserFire(entry, exit));
            possibleSolutions = BlackBoxStream.filterByLaserData(laserData);

            System.out.println("Remaining possibilities " + possibleSolutions.size());
        }

        // Последующие выстрелы на основе энтропии
        while (!availableEntries.isEmpty() && possibleSolutions.size() > 1) {
            entryId = BlackBoxStream.bestLaserId(possibleSolutions, laserData);
            if (entryId == -1) break;

            availableEntries.remove(Integer.valueOf(entryId));
            EdgeLocation entry = EdgeLocation.getEdgeLocationWithId(entryId);

            System.out.println("I press button " + entryId);
            System.out.print("Where does it exit? (H = hit, R = reflection, number = exit edge)\n> ");
            String exitInput = scanner.next();

            EdgeLocation exit = parseExitInput(exitInput, entry);
            laserData.add(new LaserFire(entry, exit));
            possibleSolutions = BlackBoxStream.filterByLaserData(laserData);

            System.out.println("Remaining possibilities " + possibleSolutions.size());

            if (possibleSolutions.isEmpty()) {
                System.out.println("Inconsistent data. No possible configuration.");
                break;
            }

            if (possibleSolutions.size() == 1) {
                System.out.println("Solved");
                System.out.println(possibleSolutions.get(0));
                break;
            }
        }

        scanner.close();
    }

    private static EdgeLocation parseExitInput(String input, EdgeLocation entry) {
        if (input.equalsIgnoreCase("H")) return null;
        if (input.equalsIgnoreCase("R")) return entry;
        return EdgeLocation.getEdgeLocationWithId(Integer.parseInt(input));
    }
}