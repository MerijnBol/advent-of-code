use std::collections::HashMap;
use std::{env, fs};

fn main() {
    let content = read_puzzle_input();
    let (line_one, line_two) = parse_content(&content);

    puzzle_one(&line_one, &line_two);
}

fn puzzle_one(line_one: &Vec<&str>, line_two: &Vec<&str>) -> i64 {
    let positions_one = get_route(line_one);
    let positions_two = get_route(line_two);
    let distance_closest_crossing = get_closest_crossing_distance(&positions_one, &positions_two);
    println!(
        "Manhatten distance of closest intersect is: {}",
        distance_closest_crossing
    );
    distance_closest_crossing
}
#[test]
fn puzzle_one_result() {
    let content = read_puzzle_input();
    let (line_one, line_two) = parse_content(&content);

    assert_eq!(puzzle_one(&line_one, &line_two), 1064)
}

fn get_route(instructions: &Vec<&str>) -> HashMap<String, (i64, i64)> {
    // For each instruction, add all traveled positions to the hashmap.
    let mut route = HashMap::new();
    let mut x: i64 = 0;
    let mut y: i64 = 0;
    for instruction in instructions.iter() {
        let command = &instruction[0..1];
        let pos = instruction[1..].parse::<i64>().unwrap();
        for _ in 0..pos {
            match command {
                "R" => x += 1,
                "L" => x -= 1,
                "U" => y += 1,
                "D" => y -= 1,
                &_ => (),
            }
            route.insert(position_display(&x, &y), (x, y));
        }
    }
    route
}

fn position_display(x: &i64, y: &i64) -> String {
    format!("({}, {})", x, y)
}

fn get_closest_crossing_distance(
    positions_one: &HashMap<String, (i64, i64)>,
    positions_two: &HashMap<String, (i64, i64)>,
) -> i64 {
    let mut manhattan: i64 = 0;

    for (key, position) in positions_one.iter() {
        if positions_two.contains_key(key) {
            let distance = position.0.abs() + position.1.abs();
            if distance == 0 {
                continue;
            }
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
