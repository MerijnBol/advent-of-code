package Day02;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        try {
            // List<String> input = Files.readAllLines(Paths.get("Day02/input.txt"));
            List<String> input = Files.readAllLines(Paths.get("Day02/test.txt"));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}