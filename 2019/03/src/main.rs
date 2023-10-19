use std::{env, fs};

fn main() {
    let content = read_puzzle_input();
    let (line_one, line_two) = parse_content(&content);

    puzzle_one(&line_one, &line_two);
}

fn puzzle_one(line_one: &Vec<&str>, line_two: &Vec<&str>) -> i64 {
    let positions_one = get_positions(line_one);
    let positions_two = get_positions(line_two);
    let distance_closest_crossing = get_closest_crossing_distance(&positions_one, &positions_two);
    println!(
        "Manhatten distance of closest intersect is: {}",
        distance_closest_crossing
    );
    distance_closest_crossing
}

fn get_positions(instructions: &Vec<&str>) -> Vec<(i64, i64)> {
    let mut positions = Vec::new();
    let mut x: i64 = 0;
    let mut y: i64 = 0;
    positions.push((x, y));
    for instruction in instructions.iter() {
        let command = &instruction[0..1];
        let pos = instruction[1..].parse::<i64>().unwrap();
        match command {
            "R" => {
                for _ in 0..pos {
                    x += 1;
                    positions.push((x, y));
                }
            }
            "L" => {
                for _ in 0..pos {
                    x -= 1;
                    positions.push((x, y));
                }
            }
            "U" => {
                for _ in 0..pos {
                    y += 1;
                    positions.push((x, y));
                }
            }
            "D" => {
                for _ in 0..pos {
                    y -= 1;
                    positions.push((x, y));
                }
            }
            &_ => (),
        }
        positions.push((x, y));
    }
    positions
}

fn get_closest_crossing_distance(
    positions_one: &Vec<(i64, i64)>,
    positions_two: &Vec<(i64, i64)>,
) -> i64 {
    let mut manhattan: i64 = 0;
    for (i, position) in positions_one.iter().enumerate() {
        if i % 1000 == 0 {
            dbg!(i);
        }
        if positions_two.contains(position) {
            let distance = position.0.abs() + position.1.abs();
            if distance < manhattan || manhattan == 0 {
                manhattan = distance;
            }
        }
    }
    manhattan
}

//
// Deal with parsing puzzle input
//
fn create_path_to_file(filename: &str) -> String {
    let mut working_dir = env::current_dir().expect("Get current dir");
    working_dir.push(filename);
    return working_dir.to_str().expect("Must have a path!").into();
}

fn read_puzzle_input() -> String {
    let path = create_path_to_file("input.txt");

    let content = fs::read_to_string(path).expect("Read file");
    content
}

fn parse_content(content: &String) -> (Vec<&str>, Vec<&str>) {
    let mut lines_iterator = content.split("\n");
    let raw_line_one = lines_iterator.next().unwrap();
    let raw_line_two = lines_iterator.next().unwrap();

    (
        instructions_from_line(raw_line_one),
        instructions_from_line(raw_line_two),
    )
}

fn instructions_from_line(line: &str) -> Vec<&str> {
    let mut vector = Vec::new();
    for instruction in line.split(",") {
        if instruction != "" {
            vector.push(instruction)
        }
    }
    vector
}
