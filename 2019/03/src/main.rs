use std::iter::zip;
use std::{env, fs};

fn main() {
    // let content = read_puzzle_input();
    // let (line_one, line_two) = parse_content(&content);

    let example =
        String::from("R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83");
    let (line_one, line_two) = parse_content(&example);

    puzzle_one(&line_one, &line_two);
}

fn puzzle_one(line_one: &Vec<&str>, line_two: &Vec<&str>) -> i64 {
    let positions_one = get_positions(line_one);
    let positions_two = get_positions(line_two);
    dbg!(&positions_one);
    dbg!(&positions_two);

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
            "R" => x += pos,
            "L" => x -= pos,
            "U" => y += pos,
            "D" => y -= pos,
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
    let mut crossings: Vec<((i64, i64), i64)> = Vec::new();
    for (index, position) in positions_one.iter().enumerate() {
        dbg!(position);
        dbg!(positions_two[index]);
    }
    // for (pos1, pos2) in zip(positions_one, positions_two) {
    //     if pos1 == pos2 {
    //         crossings.push((*pos1, 123));
    //     }
    // }
    // dbg!(crossings);
    123
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
