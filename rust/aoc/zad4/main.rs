use std::convert::TryInto;
use std::fs;

fn parse_lottery(s: &str) -> i32 {
    let s = s.split(": ").nth(1).unwrap();
    let v: Vec<&str> = s.split(" | ").collect();
    let my_numbers: Vec<i32> = v[0].split_whitespace().map(|n| n.trim().parse().unwrap()).collect();
    let winning_numbers: Vec<i32> = v[1].split_whitespace().map(|n| n.trim().parse().unwrap()).collect();
    let mut matches: i32 = -1;
    for my_number in my_numbers {
        if winning_numbers.contains(&my_number) {
            matches += 1;
        }
    }
    if matches == -1 {
        return 0;
    } else {
        2_i32.pow(matches.try_into().unwrap())
    }
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Error reading file");
    let mut total: i32 = 0;
    for line in contents.lines() {
        let matches = parse_lottery(line);
        total += matches;
    }
    println!("Total matches: {}", total);
}
