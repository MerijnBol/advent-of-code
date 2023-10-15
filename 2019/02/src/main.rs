use std::env;
use std::fs;

fn main() {
    // let path: String = create_path_to_file("input.txt");
    // let ints = read_input(&path);

    let intcode = vec![1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50];
    puzzle_one(intcode);
}

fn puzzle_one(intcode: Vec<u32>) {
    let mut intcode = intcode;
    intcode = handle_opcode(1, intcode);
    dbg!(intcode);
}

fn handle_opcode(index: usize, intcode: Vec<u32>) -> Vec<u32> {
    let mut intcode = intcode;

    let target_index_1 = intcode[index + 1] as usize;
    let target_index_2 = intcode[index + 2] as usize;
    let target_index_3 = intcode[index + 3] as usize;
    if intcode[index] == 1 {
        intcode[target_index_3] = intcode[target_index_1] + intcode[target_index_2];
    } else if intcode[index] == 2 {
        intcode[target_index_3] = intcode[target_index_1] * intcode[target_index_2];
    }
    intcode
}

#[test]
fn it_handles_addition() {
    let intcode = vec![1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50];
    let expected = vec![1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50];
    assert_eq!(handle_opcode(0, intcode), expected);
}
#[test]
fn it_handles_multiplication() {
    let intcode = vec![1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50];
    let expected = vec![3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50];
    assert_eq!(handle_opcode(4, intcode), expected);
}

fn create_path_to_file(filename: &str) -> String {
    let mut working_dir = env::current_dir().expect("Get current dir");
    working_dir.push(filename);
    return working_dir.to_str().expect("Must have a path!").into();
}

fn read_input(path: &str) -> Vec<u32> {
    let content = fs::read_to_string(path).expect("Read file");
    let mut intcode = Vec::new();
    for raw in content.split(",") {
        let integer = raw.parse::<u32>();
        if integer.is_ok() {
            intcode.push(integer.unwrap());
        }
    }
    let intcode = intcode;
    return intcode;
}
