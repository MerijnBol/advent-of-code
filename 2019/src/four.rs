use std::{collections::HashMap, env, fs, i64, vec::Vec};

const INPUT_FILE_NAME: &str = "input.txt";

fn main() {
    let content = read_puzzle_input();
    let (range_start, range_end) = parse_content(&content);
    puzzle_one(&range_start, &range_end);
    puzzle_two(&range_start, &range_end);
}

fn puzzle_one(range_start: &i64, range_end: &i64) -> i64 {
    let mut valid = 0;

    fn is_valid(pass: &String) -> bool {
        has_double(pass) && is_incremental(pass) && valid_length(pass)
    }
    for password in *range_start..*range_end + 1 {
        if is_valid(&password.to_string()) {
            valid += 1;
        }
    }
    println!("Num of valid passwords: {}", valid);
    valid
}

fn puzzle_two(range_start: &i64, range_end: &i64) -> i64 {
    let mut valid = 0;

    fn is_valid(pass: &String) -> bool {
        has_double_strict(pass) && is_incremental(pass) && valid_length(pass)
    }
    for password in *range_start..*range_end + 1 {
        if is_valid(&password.to_string()) {
            valid += 1;
        }
    }
    println!("Num of stricter valid passwords: {}", valid);
    valid
}

fn valid_length(pass: &String) -> bool {
    if pass.len() == 6 {
        true
    } else {
        false
    }
}
#[test]
fn it_passes_for_six() {
    assert_eq!(valid_length(&"123456".to_string()), true);
}
#[test]
fn it_fails_for_less() {
    assert_eq!(valid_length(&"1234".to_string()), false);
}

fn has_double(pass: &String) -> bool {
    let mut charmap = HashMap::new();
    for char in pass.chars() {
        if charmap.contains_key(&char) {
            charmap.insert(char, charmap[&char] + 1);
        } else {
            charmap.insert(char, 1);
        }
    }
    let mut doubles_count = 0;
    for value in charmap.values() {
        if *value > 1 {
            doubles_count += 1;
        }
    }
    doubles_count >= 1
}
#[test]
fn it_fails_for_missing_double() {
    assert_eq!(has_double(&"123456".to_string()), false);
}
#[test]
fn it_passes_for_multiple_doubles() {
    assert_eq!(has_double(&"122344".to_string()), true);
}
fn has_double_strict(pass: &String) -> bool {
    // Only pass if range of precise two exists
    let mut charmap = HashMap::new();
    for char in pass.chars() {
        if charmap.contains_key(&char) {
            charmap.insert(char, charmap[&char] + 1);
        } else {
            charmap.insert(char, 1);
        }
    }
    for value in charmap.values() {
        if *value == 2 {
            return true;
        }
    }
    false
}
#[test]
fn it_fails_for_strict_missing_double() {
    assert_eq!(has_double_strict(&"123456".to_string()), false);
}
#[test]
fn it_fails_for_triple() {
    assert_eq!(has_double_strict(&"122234".to_string()), false);
}
#[test]
fn it_passes_for_strict_double() {
    assert_eq!(has_double_strict(&"111122".to_string()), true);
}

fn is_incremental(pass: &String) -> bool {
    let mut order: Vec<i64> = Vec::new();
    for pos in 0..pass.len() {
        order.push(pass[pos..pos + 1].parse::<i64>().unwrap());
    }
    let mut last = 0;
    for num in order.iter() {
        if num < &last {
            return false;
        }
        last = *num;
    }
    true
}
#[test]
fn it_passes_for_incremental() {
    assert_eq!(is_incremental(&"122345".to_string()), true);
}
#[test]
fn it_fails_for_non_incremental() {
    assert_eq!(is_incremental(&"122315".to_string()), false);
}

//
// Deal with parsing puzzle input
//
fn read_puzzle_input() -> String {
    let mut working_dir = env::current_dir().expect("Get current dir");
    working_dir.push(INPUT_FILE_NAME);
    let path: &str = working_dir.to_str().expect("Must have a path!").into();
    let content = fs::read_to_string(path).expect("Read file");
    content
}

fn parse_content(content: &String) -> (i64, i64) {
    let mut parts: Vec<i64> = Vec::new();
    for part in content.split("-") {
        parts.push(part.parse::<i64>().unwrap());
    }
    if parts.len() != 2 {
        // Failure
        return (0, 0);
    }
    (parts[0], parts[1])
}
