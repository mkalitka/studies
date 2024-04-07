use std::fs;

fn combine_first_and_last_digit(s: &str) -> u32 {
    let digits: Vec<u32> = s.chars().filter_map(|c| c.to_digit(10)).collect();
    digits.first().unwrap_or(&0) * 10 + digits.last().unwrap_or(&0)
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Error reading file");
    let sum: u32 = contents
        .lines()
        .map(|line| combine_first_and_last_digit(line))
        .sum();
    println!("{}", sum);
}
