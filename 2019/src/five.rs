use std::{env, fs};

pub fn main() {
    // let content = read_input("five.txt");
    let content = "1002,4,3,4,33".to_string();
    let intcode = get_intcode(&content);
    dbg!(&intcode);
    run_intcode_v2(intcode);
}

fn run_intcode_v2(intcode: Vec<i64>) {
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
        } else if instruction == 3 {
        } else if instruction == 4 {
        }
    }
    dbg!(intcode);
}

fn decode_instruction(instruction: &str) -> (i64, Vec<i64>) {
    // Find opcode, and return the modes for required numbered of arguments.
    let mut modes = Vec::new();
    let length = instruction.len();
    let opcode: i64 = instruction[length - 2..length].parse().unwrap();
    let argument_count: i64 = match opcode {
        99 => 0,
        3 => 1,
        4 => 1,
        _ => 3,
    };
    for arg_num in 0..argument_count {
        let index: i64 = length as i64 - 3 - arg_num;
        modes.push({
            if index >= 0 {
                let index = index as usize;
                instruction[index..index + 1].parse::<i64>().unwrap()
            } else {
                0
            }
        });
    }
    (opcode, modes)
}
#[test]
fn it_decodes_instruction_one() {
    assert_eq!(decode_instruction("11001"), (1, vec![0, 1, 1]));
}
#[test]
fn it_decodes_instruction_two() {
    assert_eq!(decode_instruction("1002"), (2, vec![0, 1, 0]));
}
#[test]
fn it_decodes_instruction_three() {
    assert_eq!(decode_instruction("03"), (3, vec![0]));
}
#[test]
fn it_decodes_instruction_four() {
    assert_eq!(decode_instruction("104"), (4, vec![1]));
}
#[test]
fn it_decodes_ending_instruction() {
    assert_eq!(decode_instruction("99"), (99, Vec::new()));
}

fn read_input(filename: &str) -> String {
    let mut working_dir = env::current_dir().expect("Get current dir");
    working_dir.push("inputs");
    working_dir.push(filename);
    let path: &str = working_dir.to_str().expect("Must have a path!").into();
    let content = fs::read_to_string(path).expect("Read file");
    content
}

fn get_intcode(content: &String) -> Vec<i64> {
    let mut intcode: Vec<i64> = Vec::new();
    for code in content.split(",") {
        if code == "" {
            continue;
        }
        intcode.push(code.parse::<i64>().unwrap())
    }
    intcode
}
