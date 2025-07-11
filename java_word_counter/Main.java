/**
 * Java Word Frequency Counter
 *
 * This program reads a large text file, counts the frequency of each word,
 * and writes the top 10 most common words to a file.
 *
 * Author: Jose R. Mondragon
 */

import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    /**
     * Reads the file and computes word frequency, printing the top 10 results.
     *
     * @param args not used
     * @throws IOException if the file cannot be read
     */
    public static void main(String[] args) throws IOException {
        long start = System.currentTimeMillis();

        String content = Files.readString(Paths.get("../big_file.txt")).toLowerCase();
        String[] words = content.split("\\s+");

        Map<String, Integer> frequency = new HashMap<>();
        for (String word : words) {
            frequency.put(word, frequency.getOrDefault(word, 0) + 1);
        }

        List<Map.Entry<String, Integer>> topWords = frequency.entrySet()
                .stream()
                .sorted((a, b) -> b.getValue() - a.getValue())
                .limit(10)
                .collect(Collectors.toList());

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("result.txt"))) {
            writer.write("Top 10 most common words:\n");
            for (var entry : topWords) {
                writer.write(entry.getKey() + ": " + entry.getValue() + "\n");
            }
        }

        long end = System.currentTimeMillis();
        System.out.printf("✅ Execution time: %.3f seconds\n", (end - start) / 1000.0);
    }
}
