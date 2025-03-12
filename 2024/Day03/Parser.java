package Day03;

import java.util.*;
import java.util.regex.*;

/**
 * Parses input strings to extract multiplication commands.
 */
public class Parser {
    public static List<Command> findAllCommands(String input) {
        List<Command> commands = new ArrayList<>();

        // Matches either "mul(1,2)" or "do()" or "don't()"
        Pattern pattern = Pattern.compile("(?:mul\\((?<val1>\\d+),(?<val2>\\d+)\\)|(?<switcher>do|don't)\\(\\))");
        Matcher matcher = pattern.matcher(input);

        while (matcher.find()) {
            try {
                String switcher = matcher.group("switcher");
                if (switcher != null) {
                    commands.add(new Command(switcher, 0, 0));
                } else {
                    int operand1 = Integer.parseInt(matcher.group("val1"));
                    int operand2 = Integer.parseInt(matcher.group("val2"));
                    commands.add(new Command("mul", operand1, operand2));
                }
            } catch (NumberFormatException e) {
                // Skip this match if we can't parse the numbers
                // This is unlikely to happen given our regex pattern
            }
        }

        return commands;
    }
}
