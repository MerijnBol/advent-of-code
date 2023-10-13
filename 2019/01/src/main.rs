use std::env;
use std::fs;

fn main() {
    // let masses = [12, 14, 1969, 100756];
    // println!("Total fuel load: {} kg", calculate_fuel(masses))

    let path: String = create_path_to_file("test_input.txt");

    read_input(&path);
}

fn counter_upper(mass: u32) -> u32 {
    let mut float = mass as f64;
    float /= 3.0;
    float = float.floor() - 2.0;
    return float as u32;
}

fn calculate_fuel(masses: [u32; 4]) -> u32 {
    let mut total = 0;
    for mass in masses.iter() {
        total += counter_upper(*mass)
    }
    return total;
}

fn create_path_to_file(filename: &str) -> String {
    let mut working_dir = env::current_dir().expect("Get current dir");
    working_dir.push(filename);
    println!(
        "testing: {}",
        working_dir.to_str().expect("Must have a path!")
    );
    return working_dir.to_str().expect("Must have a path!").into();
}

fn read_input(path: &str) {
    let content = fs::read_to_string(path).expect("Read file");
    println!("Content is: \n\n{}", content);
}
