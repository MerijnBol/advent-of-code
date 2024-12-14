package Day01;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.List;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        try {
            List<String> input = Files.readAllLines(Paths.get("Day01/input.txt"));
            // List<String> input = Files.readAllLines(Paths.get("Day01/test.txt"));
            int[] leftList = new int[input.size()];
            int[] rightList = new int[input.size()];
            for (int i = 0; i < input.size(); i++) {
                String[] parts = input.get(i).split("\\s+");
                leftList[i] = Integer.parseInt(parts[0]);
                rightList[i] = Integer.parseInt(parts[1]);
            }

            // Sort the arrays
            Arrays.sort(leftList);
            Arrays.sort(rightList);

            // Calculate the gaps
            int[] gaps = new int[leftList.length];
            for (int i = 0; i < leftList.length; i++) {
                gaps[i] = Math.abs(leftList[i] - rightList[i]);
            }

            System.out.println("Total of gaps: " + Arrays.stream(gaps).sum());

            int similarity = 0;
            for (int i = 0; i < leftList.length; i++) {
                int value = leftList[i];
                long count = Arrays.stream(rightList).filter(x -> x == value).count();
                similarity += value * count;
            }

            System.out.println("Similarity score is: " + similarity);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}