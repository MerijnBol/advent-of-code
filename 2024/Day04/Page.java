package Day04;

import java.util.*;

public class Page {
    private List<String> data;
    private int height;
    private int width;

    public Page(String input) {
        this.data = new ArrayList<>();
        for (String line : input.trim().split("\n")) {
            this.data.add(line);
        }
        this.height = this.data.size();
        this.width = this.data.get(0).length();
    }

    public char getForCoordinate(Coordinate coordinate) {
        return data.get(coordinate.y).charAt(coordinate.x);
    }

    public int findWordCount(String word) {
        int count = 0;
        for (Coordinate coor : this.findAllCharacters(word.charAt(0))) {
            count += this.findWordsFromLetter(word, coor);
        }
        return count;
    }

    public int findCrossWords() {
        String word = "MAS";
        int count = 0;
        List<Coordinate> aPos = new ArrayList<>();
        for (Coordinate coor : this.findAllCharacters('M')) {
            aPos += this.findWordsFromLetter(word, coor);
        }
        return count;
    }

    private List<Coordinate> findAllCharacters(char letter) {
        List<Coordinate> result = new ArrayList<>();
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                Coordinate coor = new Coordinate(x, y);
                if (this.getForCoordinate(coor) == letter) {
                    result.add(coor);
                }
            }
        }
        return result;
    }

    private int findWordsFromLetter(String word, Coordinate coordinate) {
        int occurences = 0;
        List<Coordinate> secondLetters = findChars(word.charAt(1), coordinate);
        for (Coordinate c : secondLetters) {
            List<Coordinate> nextCs = this.getNextTwoCoordinates(coordinate, c);
            try {
                char three = this.getForCoordinate(nextCs.get(0));
                char four = this.getForCoordinate(nextCs.get(1));
                if (three == 'A' && four == 'S') {
                    occurences += 1;
                }
            } catch (Exception e) {
                //
            }
        }
        return occurences;
    }

    /** Look around the given coordinate for the given target letter */
    private List<Coordinate> findChars(char targetLetter, Coordinate coordinate) {
        List<Coordinate> results = new ArrayList<>();
        for (Coordinate toCheck : this.getAllCoor(coordinate)) {
            if (this.getForCoordinate(toCheck) == targetLetter) {
                results.add(toCheck);
            }
        }
        return results;
    }

    private List<Coordinate> getAllCoor(Coordinate coordinate) {
        List<Coordinate> results = new ArrayList<>();
        int[] xLen = { coordinate.x - 1, coordinate.x, coordinate.x + 1 };
        int[] yLen = { coordinate.y - 1, coordinate.y, coordinate.y + 1 };
        for (int y : yLen) {
            for (int x : xLen) {
                if ((x >= 0 && x < this.width) && (y >= 0 && y < this.height)) {
                    results.add(new Coordinate(x, y));
                }
            }
        }
        return results;
    }

    private List<Coordinate> getNextTwoCoordinates(Coordinate c1, Coordinate c2) {
        int dx = c2.x - c1.x;
        int dy = c2.y - c1.y;
        Coordinate c3 = new Coordinate(c2.x + dx, c2.y + dy);
        Coordinate c4 = new Coordinate(c3.x + dx, c3.y + dy);
        return Arrays.asList(c3, c4);
    }
}

class Coordinate {
    public int x;
    public int y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return String.format("Coordinate(x=%d, y=%d)", this.x, this.y);
    }
}