use std::env;
use std::fs;

fn main() {
    let path: String = create_path_to_file("input.txt");
    let ints = read_input(&path);

    dbg!(ints);
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
    return intcode;
}
