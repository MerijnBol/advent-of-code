package Day04;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        try {
            String input;
            if (args.length > 0 && args[0].equalsIgnoreCase("test")) {
                input = Files.readString(Paths.get("Day04/test.txt"));
            } else {
                input = Files.readString(Paths.get("Day04/input.txt"));
            }
            Page page = new Page(input);

            System.out.println(page.findWordCount("XMAS"));
            // Too high: 1847
            System.out.println(page.findCrossWords());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}