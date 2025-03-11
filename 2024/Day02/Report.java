package Day02;

import java.util.ArrayList;
import java.util.List;

public class Report {
    private final List<Integer> values;
    private static final int MAX_ALLOWED_GAP = 3;

    public Report(List<Integer> values) {
        this.values = new ArrayList<>(values); // Make a defensive copy
    }

    /**
     * Checks if the report is safe based on the gap rules
     * 
     * @return A ReportResult containing safety status and failure position
     */
    public ReportResult checkSafety() {
        int midpoint = values.size() / 2;
        int skippoint = values.size() - values.size() / 2;
        int firstHalve = values.stream().limit(midpoint).mapToInt(Integer::intValue).sum();
        int secondHalve = values.stream().skip(skippoint).mapToInt(Integer::intValue).sum();

        int direction = firstHalve < secondHalve ? 1 : -1;

        for (int i = 0; i < values.size() - 1; i++) {
            int gap = values.get(i + 1) - values.get(i);
            if (!isValidGap(gap, direction)) {
                return new ReportResult(false, i);
            }
        }
        return new ReportResult(true, -1);
    }

    /**
     * Creates two modified reports by removing potential problematic elements
     * 
     * @param failurePosition Position where the validation failed
     * @return Array containing two alternative reports
     */
    public Report[] createSecondChances(int failurePosition) {
        Report[] secondChances = new Report[2];

        List<Integer> reportA = new ArrayList<>(values);
        List<Integer> reportB = new ArrayList<>(values);

        reportA.remove(failurePosition);
        reportB.remove(failurePosition + 1);

        secondChances[0] = new Report(reportA);
        secondChances[1] = new Report(reportB);

        return secondChances;
    }

    private boolean isValidGap(int gap, int direction) {
        if (Math.abs(gap) == 0 || Math.abs(gap) > MAX_ALLOWED_GAP || direction * gap < 0) {
            return false;
        }
        return true;
    }

    public List<Integer> getValues() {
        return new ArrayList<>(values); // Return defensive copy
    }

    @Override
    public String toString() {
        return values.toString();
    }
}
