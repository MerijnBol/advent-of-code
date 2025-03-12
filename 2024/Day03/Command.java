package Day03;

/**
 * Represents a multiplication command with two operands.
 */
public class Command {
    private final String method;
    private final int operand1;
    private final int operand2;

    public Command(String method, int operand1, int operand2) {
        this.method = method;
        this.operand1 = operand1;
        this.operand2 = operand2;
    }

    public boolean isMultiplication() {
        return method.equals("mul");
    }

    public boolean lockMul() {
        return method.equals("don't");
    }

    public boolean unlockMul() {
        return method.equals("do");
    }

    public int execute() {
        return operand1 * operand2;
    }

    @Override
    public String toString() {
        return method + "(" + operand1 + "," + operand2 + ")";
    }
}