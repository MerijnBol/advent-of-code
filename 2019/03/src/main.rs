use std::collections::HashMap;
use std::{env, fs};

fn main() {
    let content = read_puzzle_input();
    let (line_one, line_two) = parse_content(&content);
    let (positions_one, ordered_one) = get_route(&line_one);
    let (positions_two, ordered_two) = get_route(&line_two);

    puzzle_one(&positions_one, &positions_two);
    puzzle_two(&ordered_one, &ordered_two, &positions_two);
}

fn puzzle_one(
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
    println!("Manhatten distance of closest intersect is: {}", manhattan);
    manhattan
}
#[test]
fn puzzle_one_result() {
    let content = read_puzzle_input();
    let (line_one, line_two) = parse_content(&content);
    let (positions_one, _ordered_one) = get_route(&line_one);
    let (positions_two, _ordered_two) = get_route(&line_two);

    assert_eq!(puzzle_one(&positions_one, &positions_two), 1064)
}

fn puzzle_two(
    line_one: &Vec<String>,
    line_two: &Vec<String>,
    hash_two: &HashMap<String, (i64, i64)>,
) -> i64 {
    // Hashmap for storing each junction, and how long each route takes to get there.
    let mut distances: HashMap<&str, i64> = HashMap::new();
    let mut counter = 1;
    for position in line_one.iter() {
        if hash_two.contains_key(position.as_str()) {
            distances.insert(position.as_str(), counter);
        }
        counter += 1;
    }
    counter = 1;
    for position in line_two.iter() {
        if distances.contains_key(position.as_str()) {
            distances.insert(position.as_str(), distances[position.as_str()] + counter);
        }
        counter += 1;
    }
    let mut result = 0;
    for value in distances.values() {
        if *value < result || result == 0 {
            result = *value;
        }
    }
    println!("Shortest combined distance is '{}'", result);
    result
}
#[test]
fn puzzle_two_result() {
    let content = read_puzzle_input();
    let (line_one, line_two) = parse_content(&content);
    let (_positions_one, ordered_one) = get_route(&line_one);
    let (positions_two, ordered_two) = get_route(&line_two);

    assert_eq!(
        puzzle_two(&ordered_one, &ordered_two, &positions_two),
        25676
    )
}

fn get_route(instructions: &Vec<&str>) -> (HashMap<String, (i64, i64)>, Vec<String>) {
    // For each instruction, add all traveled positions to a hasmap and ordered
    // vector.
    let mut hashmap = HashMap::new();
    let mut route = Vec::new();
    let mut x: i64 = 0;
    let mut y: i64 = 0;
    for instruction in instructions.iter() {
        let command = &instruction[0..1];
        let moves = instruction[1..].parse::<i64>().unwrap();
        for _ in 0..moves {
            match command {
                "R" => x += 1,
                "L" => x -= 1,
                "U" => y += 1,
                "D" => y -= 1,
                &_ => (),
            }
            route.push(position_display(&(x, y)));
            hashmap.insert(position_display(&(x, y)), (x, y));
        }
    }
    (hashmap, route)
}

fn position_display(pos: &(i64, i64)) -> String {
    format!("({}, {})", pos.0, pos.1)
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
