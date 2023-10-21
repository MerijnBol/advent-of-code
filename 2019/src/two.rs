use std::env;
use std::fs;

const INPUT_FILE_NAME: &str = "two.txt";

pub fn main() {
    let path: String = create_path_to_file();

    // TODO Find out how to do this properly
    let intcode = read_input(&path);
    puzzle_one(intcode);
    let intcode = read_input(&path);
    puzzle_two(intcode);
}

fn puzzle_one(intcode: Vec<u64>) -> u64 {
    let mut intcode = intcode;
    intcode[1] = 12;
    intcode[2] = 2;
    let result = run_intcode(intcode);
    println!("Program found value '{}' on position 0!", result[0]);
    result[0]
}
#[test]
fn puzzle_one_gives_correct_answer() {
    let path: String = create_path_to_file("input.txt");
    let intcode = read_input(&path);
    assert_eq!(puzzle_one(intcode), 3562624);
}

fn puzzle_two(intcode: Vec<u64>) -> u64 {
    let expected = 19690720;
    let mut noun = 0 as u64;
    let mut verb = 0 as u64;
    // Test all noun and verb combinations until expected answer is found.
    loop {
        let mut address = intcode.clone();
        address[1] = noun;
        address[2] = verb;
        let result = run_intcode(address);

        if result[0] == expected {
            break;
        }

        if verb < 100 {
            verb += 1;
        } else {
            verb = 0;
            noun += 1;
        }
    }

    let code = 100 * noun + verb;
    println!("Expected result provided by code: '{}'", code);
    code
}

#[test]
fn test_puzzle_two_result() {
    let path: String = create_path_to_file("input.txt");
    let intcode = read_input(&path);
    assert_eq!(puzzle_two(intcode), 8298);
}

fn run_intcode(intcode: Vec<u64>) -> Vec<u64> {
    let mut intcode = intcode;
    let mut pointer: usize = 0;
    loop {
        let instruction = intcode[pointer];
        let target_index_1 = intcode[pointer + 1] as usize;
        let target_index_2 = intcode[pointer + 2] as usize;
        let target_index_3 = intcode[pointer + 3] as usize;
        let out_of_bounds = target_index_1 >= intcode.len()
            || target_index_2 >= intcode.len()
            || target_index_3 >= intcode.len();

        if instruction == 99 || out_of_bounds {
            break;
        } else if instruction == 1 {
            intcode[target_index_3] = intcode[target_index_1] + intcode[target_index_2];
            pointer += 4;
        } else if instruction == 2 {
            intcode[target_index_3] = intcode[target_index_1] * intcode[target_index_2];
            pointer += 4;
        }
    }
    intcode
}

fn create_path_to_file() -> String {
    let mut working_dir = env::current_dir().expect("Get current dir");
    working_dir.push("inputs");
    working_dir.push(INPUT_FILE_NAME);
    return working_dir.to_str().expect("Must have a path!").into();
}

fn read_input(path: &str) -> Vec<u64> {
    let content = fs::read_to_string(path).expect("Read file");
    let mut intcode = Vec::new();
    for raw in content.split(",") {
        let integer = raw.parse::<u64>();
        if integer.is_ok() {
            intcode.push(integer.unwrap());
        }
    }
    let intcode = intcode;
    return intcode;
}
