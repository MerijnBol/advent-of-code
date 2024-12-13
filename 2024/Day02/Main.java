
package Day02;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        try {
            List<String> input = Files.readAllLines(Paths.get("input.txt"));
            List<String> testInput = Files.readAllLines(Paths.get("test.txt"));
            // ...existing code...
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}