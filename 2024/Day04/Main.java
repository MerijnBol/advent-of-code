package Day04;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        try {
            // String input = Files.readString(Paths.get("Day04/input.txt"));
            String input = Files.readString(Paths.get("Day04/test.txt"));
            Page page = new Page(input);

            System.out.println(page.findWordCount("XMAS"));
            System.out.println(page.findCrossWords());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}