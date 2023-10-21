use std::env;
use std::fs;

const INPUT_FILE_NAME: &str = "one.txt";

pub fn main() {
    let path: String = create_path_to_file();
    let masses = read_input(&path);
    println!("Fuel load puzzle 1: {} kg", calculate_fuel(&masses));

    // puzzle 2
    println!(
        "Fuel load puzzle 2: {} kg",
        calculate_recursive_fuel(&masses)
    );
}

fn counter_upper(mass: u32) -> u32 {
    let mut float = mass as f64;
    float /= 3.0;
    float = float.floor() - 2.0;
    return float as u32;
}

fn calculate_fuel(masses: &Vec<u32>) -> u32 {
    let mut total = 0;
    for mass in masses.iter() {
        total += counter_upper(*mass)
    }
    return total;
}

fn calculate_recursive_fuel(masses: &Vec<u32>) -> u32 {
    let mut total = 0;
    for mass in masses.iter() {
        let mut fuel: u32 = counter_upper(*mass);
        total += fuel;
        while fuel > 0 {
            fuel = counter_upper(fuel);
            total += fuel
        }
    }
    return total;
}

fn create_path_to_file() -> String {
    let mut working_dir = env::current_dir().expect("Get current dir");
    working_dir.push("inputs");
    working_dir.push(INPUT_FILE_NAME);
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
