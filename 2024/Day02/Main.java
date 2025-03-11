package Day02;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        try {
            List<String> input = Files.readAllLines(Paths.get("Day02/input.txt"));
            List<Report> reports = parseInput(input);

            // Puzzle 1
            int safeCount = 0;
            List<Report> unsafeReports = new ArrayList<>();
            List<ReportResult> unsafeResults = new ArrayList<>();

            for (Report report : reports) {
                ReportResult result = report.checkSafety();
                if (result.isSafe) {
                    safeCount++;
                } else {
                    unsafeReports.add(report);
                    unsafeResults.add(result);
                }
            }
            System.out.println("Reports safe: " + safeCount);

            // Puzzle 2
            for (int i = 0; i < unsafeReports.size(); i++) {
                Report report = unsafeReports.get(i);
                ReportResult result = unsafeResults.get(i);

                Report[] secondChances = report.createSecondChances(result.position);
                ReportResult resultA = secondChances[0].checkSafety();
                ReportResult resultB = secondChances[1].checkSafety();

                if (resultA.isSafe || resultB.isSafe) {
                    safeCount++;
                }
            }
            System.out.println("Reports safe with V2 regs: " + safeCount);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static List<Report> parseInput(List<String> lines) {
        List<Report> reports = new ArrayList<>();

        for (String line : lines) {
            List<Integer> values = new ArrayList<>();
            String[] split = line.split("\\s+");

            for (String value : split) {
                values.add(Integer.parseInt(value));
            }

            reports.add(new Report(values));
        }

        return reports;
    }
}