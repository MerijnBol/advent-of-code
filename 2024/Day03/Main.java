package Day03;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        try {
            String input = Files.readString(Paths.get("Day03/input.txt"));
            // String input = Files.readString(Paths.get("Day03/test.txt"));
            List<Command> commands = Parser.findAllCommands(input);

            Integer result1 = 0;
            for (Command command : commands) {
                if (command.isMultiplication()) {
                    result1 += command.execute();
                }
            }
            System.out.println(result1);

            Integer result2 = 0;
            boolean locked = false;
            for (Command command : commands) {
                if (command.isMultiplication() && !locked) {
                    result2 += command.execute();
                } else if (command.lockMul()) {
                    locked = true;
                } else if (command.unlockMul()) {
                    locked = false;
                }
            }
            System.out.println(result2);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}