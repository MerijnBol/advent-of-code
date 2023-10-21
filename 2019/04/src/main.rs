use std::{collections::HashMap, env, fs, i64, vec::Vec};

const INPUT_FILE_NAME: &str = "input.txt";

fn main() {
    let content = read_puzzle_input();
    let (range_start, range_end) = parse_content(&content);
    puzzle_one(&range_start, &range_end);
}

fn puzzle_one(range_start: &i64, range_end: &i64) -> i64 {
    let mut valid = 0;
    for password in *range_start..*range_end + 1 {
        if valid_password(&password.to_string()) {
            valid += 1;
        }
    }
    println!("Num of valid passwords: {}", valid);
    valid
}

fn valid_password(password: &String) -> bool {
    let length = if password.len() == 6 { true } else { false };
    let doubles = {
        let mut charmap = HashMap::new();
        for char in password.chars() {
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
    };
    let incremental = {
        let mut order: Vec<i64> = Vec::new();
        for pos in 0..password.len() {
            order.push(password[pos..pos + 1].parse::<i64>().unwrap());
        }
        let mut last = 0;
        for num in order.iter() {
            if num < &last {
                return false;
            }
            last = *num;
        }
        true
    };

    // Return wether all checks were successful
    length && doubles && incremental
}
#[test]
fn it_passes_for_valid_password() {
    assert_eq!(valid_password(&"122345".to_string()), true);
}
#[test]
fn it_fails_for_non_incremental() {
    assert_eq!(valid_password(&"122315".to_string()), false);
}
#[test]
fn it_fails_for_missing_double() {
    assert_eq!(valid_password(&"123456".to_string()), false);
}
#[test]
fn it_passes_for_multiple_doubles() {
    assert_eq!(valid_password(&"122344".to_string()), true);
}
#[test]
fn it_fails_for_non_6_digit_number() {
    assert_eq!(valid_password(&"1234".to_string()), false);
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
