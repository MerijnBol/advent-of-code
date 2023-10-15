use std::env;
use std::fs;

fn main() {
    let path: String = create_path_to_file("input.txt");

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

fn puzzle_two(intcode: Vec<u64>) {
    let start_address = intcode;
    let expected = 19690720;
    let mut noun = 0 as u64;
    let mut verb = 0 as u64;
    'noun_loop: loop {
        loop {
            let mut address = start_address.clone();
            address[1] = noun;
            address[2] = verb;
            let result = run_intcode(address);

            if result[0] == expected {
                break 'noun_loop;
            }

            verb += 1;

            if verb == 100 {
                verb = 0;
                break;
            }
        }
        noun += 1;

        if noun == 100 {
            break;
        }
    }

    println!("Expected result provided by code: '{}'", 100 * noun + verb)
}

fn run_intcode(intcode: Vec<u64>) -> Vec<u64> {
    let mut intcode = intcode;
    let mut pointer: usize = 0;
    loop {
        let instruction = intcode[pointer];
        if instruction == 1 {
            intcode = opcode_addition(pointer, intcode);
            pointer += 4;
        } else if instruction == 2 {
            intcode = opcode_multiplication(pointer, intcode);
            pointer += 4;
        } else if instruction == 99 {
            break;
        }
    }
    intcode
}

fn opcode_addition(index: usize, intcode: Vec<u64>) -> Vec<u64> {
    let mut intcode = intcode;

    let target_index_1 = intcode[index + 1] as usize;
    let target_index_2 = intcode[index + 2] as usize;
    let target_index_3 = intcode[index + 3] as usize;
    if target_index_1 >= intcode.len()
        || target_index_2 >= intcode.len()
        || target_index_3 >= intcode.len()
    {
        return intcode;
    }
    intcode[target_index_3] = intcode[target_index_1] + intcode[target_index_2];
    intcode
}
fn opcode_multiplication(index: usize, intcode: Vec<u64>) -> Vec<u64> {
    let mut intcode = intcode;

    let target_index_1 = intcode[index + 1] as usize;
    let target_index_2 = intcode[index + 2] as usize;
    let target_index_3 = intcode[index + 3] as usize;
    if target_index_1 >= intcode.len()
        || target_index_2 >= intcode.len()
        || target_index_3 >= intcode.len()
    {
        return intcode;
    }
    intcode[target_index_3] = intcode[target_index_1] * intcode[target_index_2];
    intcode
}

#[test]
fn it_handles_addition() {
    let intcode = vec![1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50];
    let expected = vec![1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50];
    assert_eq!(opcode_addition(0, intcode), expected);
}
#[test]
fn it_handles_multiplication() {
    let intcode = vec![1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50];
    let expected = vec![3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50];
    assert_eq!(opcode_multiplication(4, intcode), expected);
}

fn create_path_to_file(filename: &str) -> String {
    let mut working_dir = env::current_dir().expect("Get current dir");
    working_dir.push(filename);
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
