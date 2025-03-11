package Day02;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        try {
            List<String> input = Files.readAllLines(Paths.get("Day02/input.txt"));

            List<List<Integer>> reports = parseInput(input);
            int safeCount = 0;
            for (int i = 0; i < reports.size(); i++) {
                ReportResult result = reportSafe(reports.get(i));
                if (result.isSafe) {
                    safeCount++;
                }
            }
            System.out.println("Reports safe: " + safeCount);

            // Puzzle 2
            safeCount = 0;
            // Any failing report gets stored as a second chance. We need 2
            // lists since removing either of the 2 failing positions could make
            // the report valid.
            List<List<Integer>> secondChanceA = new ArrayList<>();
            List<List<Integer>> secondChanceB = new ArrayList<>();
            for (int i = 0; i < reports.size(); i++) {
                ReportResult result = reportSafe(reports.get(i));
                if (result.isSafe) {
                    safeCount++;
                } else {
                    // Add the 2 second chances
                    List<Integer> reportA = new ArrayList<>(reports.get(i));
                    List<Integer> reportB = new ArrayList<>(reports.get(i));
                    reportA.remove(result.position);
                    reportB.remove(result.position + 1);
                    secondChanceA.add(reportA);
                    secondChanceB.add(reportB);
                }
            }
            // Try the second chances one more time. If one of them is safe, we count it.
            for (int i = 0; i < secondChanceA.size(); i++) {
                ReportResult resultA = reportSafe(secondChanceA.get(i));
                ReportResult resultB = reportSafe(secondChanceB.get(i));
                if (resultA.isSafe || resultB.isSafe) {
                    safeCount++;
                }
            }
            System.out.println("Reports safe with V2 regs: " + safeCount);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static class ReportResult {
        public final boolean isSafe;
        public final int position;

        public ReportResult(boolean isSafe, int position) {
            this.isSafe = isSafe;
            this.position = position;
        }
    }

    public static ReportResult reportSafe(List<Integer> report) {
        int midpoint = report.size() / 2;
        int skippoint = report.size() - report.size() / 2;
        Integer firstHalve = report.stream().limit(midpoint).mapToInt(Integer::intValue).sum();
        Integer secondHalve = report.stream().skip(skippoint).mapToInt(Integer::intValue).sum();
        int direction = 0;
        if (firstHalve < secondHalve) {
            direction = 1;
        } else {
            direction = -1;
        }

        for (int i = 0; i < report.size() - 1; i++) {
            Integer gap = report.get(i + 1) - report.get(i);
            if (!validGap(gap, direction)) {
                return new ReportResult(false, i);
            }
        }
        return new ReportResult(true, -1);
    }

    public static boolean validGap(int gap, int direction) {
        final int MAX_ALLOWED_GAP = 3;
        if (Math.abs(gap) == 0 || Math.abs(gap) > MAX_ALLOWED_GAP || direction * gap < 0) {
            return false;
        }
        return true;
    }

    public static List<List<Integer>> parseInput(List<String> lines) {
        List<List<Integer>> reports = new ArrayList<>();
        for (int i = 0; i < lines.size(); i++) {
            List<Integer> report = new ArrayList<>();
            String[] split = lines.get(i).split("\\s+");
            for (int j = 0; j < split.length; j++) {
                report.add(Integer.parseInt(split[j]));
            }
            reports.add(report);
        }

        return reports;
    }
}