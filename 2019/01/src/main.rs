use std::env;
use std::fs;

fn main() {
    let path: String = create_path_to_file("input.txt");
    let masses = read_input(&path);
    println!("{}", calculate_fuel(masses));
}

fn counter_upper(mass: u32) -> u32 {
    let mut float = mass as f64;
    float /= 3.0;
    float = float.floor() - 2.0;
    return float as u32;
}

fn calculate_fuel(masses: Vec<u32>) -> u32 {
    let mut total = 0;
    for mass in masses.iter() {
        total += counter_upper(*mass)
    }
    return total;
}

fn create_path_to_file(filename: &str) -> String {
    let mut working_dir = env::current_dir().expect("Get current dir");
    working_dir.push(filename);
    return working_dir.to_str().expect("Must have a path!").into();
}

fn read_input(path: &str) -> Vec<u32> {
    let content = fs::read_to_string(path).expect("Read file");
    let mut mass_array = Vec::new();
    for raw in content.split("\n") {
        let mass = raw.parse::<u32>();
        if mass.is_ok() {
            mass_array.push(raw.parse::<u32>().unwrap())
        }
    }
    return mass_array;
}
