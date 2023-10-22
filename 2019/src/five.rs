use std::{env, fs};

pub fn main() {
    // let content = read_input("five.txt");
    let content = "1002,4,3,4,33".to_string();
    let intcode = get_intcode(&content);
    run_intcode_v2(&intcode);
}

// fn run_intcode_v2(intcode: &Vec<&str>) -> Vec<&str> {
fn run_intcode_v2(intcode_source: &Vec<String>) {
    let mut intcode = intcode_source.clone();
    let mut pointer: usize = 0;
    loop {
        let (opcode, modes) = decode_instruction(&intcode[pointer]);
        let mut arguments: Vec<i64> = Vec::new();
        for index in 0..modes.len() {
            arguments.push(intcode[pointer + 1 + index].parse().unwrap())
        }

        if opcode == 99 {
            break;
        } else if opcode == 1 {
            intcode = intcode_operation(intcode, &arguments, &modes, "add");
        } else if opcode == 2 {
            intcode = intcode_operation(intcode, &arguments, &modes, "mul");
        } else if opcode == 3 {
        } else if opcode == 4 {
        };
        pointer += arguments.len() + 1;
    }
}

fn intcode_operation(
    mut code: Vec<String>,
    args: &Vec<i64>,
    modes: &Vec<i64>,
    operation: &str,
) -> Vec<String> {
    // intcode_r[target_index_3] = intcode_r[target_index_1] + intcode_r[target_index_2];
    let val_1: i64 = if modes[0] == 0 {
        let index = args[0] as usize;
        code[index].parse().unwrap()
    } else {
        args[0]
    };
    let val_2: i64 = if modes[1] == 0 {
        let index = args[1] as usize;
        code[index].parse().unwrap()
    } else {
        args[1]
    };
    let index = args[2] as usize;
    if operation == "add" {
        code[index] = (val_1 + val_2).to_string();
    } else {
        code[index] = (val_1 * val_2).to_string();
    }
    code
}

fn decode_instruction(instruction: &String) -> (i64, Vec<i64>) {
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
    assert_eq!(decode_instruction(&"11001".to_string()), (1, vec![0, 1, 1]));
}
#[test]
fn it_decodes_instruction_two() {
    assert_eq!(decode_instruction(&"1002".to_string()), (2, vec![0, 1, 0]));
}
#[test]
fn it_decodes_instruction_three() {
    assert_eq!(decode_instruction(&"03".to_string()), (3, vec![0]));
}
#[test]
fn it_decodes_instruction_four() {
    assert_eq!(decode_instruction(&"104".to_string()), (4, vec![1]));
}
#[test]
fn it_decodes_ending_instruction() {
    assert_eq!(decode_instruction(&"99".to_string()), (99, Vec::new()));
}

fn read_input(filename: &str) -> String {
    let mut working_dir = env::current_dir().expect("Get current dir");
    working_dir.push("inputs");
    working_dir.push(filename);
    let path: &str = working_dir.to_str().expect("Must have a path!").into();
    let content = fs::read_to_string(path).expect("Read file");
    content
}

fn get_intcode(content: &String) -> Vec<String> {
    let mut intcode: Vec<String> = Vec::new();
    for code in content.split(",") {
        if code == "" {
            continue;
        }
        intcode.push(code.to_string());
    }
    intcode
}
