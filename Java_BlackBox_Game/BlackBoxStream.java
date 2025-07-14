package tr.edu.ozyegin.cs101.blackbox;

import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import tr.edu.ozyegin.cs101.blackbox.Game.LaserFire;

public class BlackBoxStream {

    /**
     * Mevcut tüm olası kutuları oluşturur (a < b < c < d koşulunu sağlayan).
     */
    public static Stream<BlackBox> streamBlackBoxes() {
        return IntStream.range(0, 1 << 24)
                .mapToObj(bits -> {
                    int a = (bits >> 18) & 0x3F;
                    int b = (bits >> 12) & 0x3F;
                    int c = (bits >> 6) & 0x3F;
                    int d = bits & 0x3F;
                    if (a < b && b < c && c < d) {
                        return new BlackBox(
                                Location.locationFromLinearPosition(a),
                                Location.locationFromLinearPosition(b),
                                Location.locationFromLinearPosition(c),
                                Location.locationFromLinearPosition(d));
                    } else {
                        return null;
                    }
                })
                .filter(box -> box != null);
    }

    /**
     * Girilen tüm lazer verilerine uyan kutuları filtreler.
     */
    public static List<BlackBox> filterByLaserData(List<LaserFire> laserFires) {
        return streamBlackBoxes()
                .filter(box -> laserFires.stream()
                        .allMatch(fire -> box.laserEntryExitMatches(fire.entry(), fire.exit())))
                .toList();
    }

    /**
     * Verilen kutu listesi içinde en çok bilgi sağlayan lazer girişini (1–32) bulur.
     * Bu lazer, farklı çıkışlar üretme sayısı en yüksek olandır.
     */
    public static int bestLaserId(List<BlackBox> candidates, List<LaserFire> usedFires) {
        int bestId = -1;
        int maxGroups = -1;

        for (int id = 1; id <= 32; id++) {
            final int currentId = id; // Lambda için final kopya

            // Daha önce bu lazer kullanıldıysa atla
            boolean alreadyUsed = usedFires.stream()
                    .anyMatch(f -> f.entry().getEdgeLocationId() == currentId);

            if (alreadyUsed) continue;

            EdgeLocation entry = EdgeLocation.getEdgeLocationWithId(currentId);
            Map<String, Integer> outcomeCounts = new HashMap<>();

            for (BlackBox box : candidates) {
                EdgeLocation result = new Laser(entry).findExitEdgeLocation(box);
                String key = (result == null) ? "HIT" : String.valueOf(result.getEdgeLocationId());
                outcomeCounts.put(key, outcomeCounts.getOrDefault(key, 0) + 1);
            }

            if (outcomeCounts.size() > maxGroups) {
                maxGroups = outcomeCounts.size();
                bestId = currentId;
            }
        }

        return bestId;
    }
}