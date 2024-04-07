use std::fs;

fn elf_game(s: &str) -> u32 {
    let v: Vec<&str> = s.split_whitespace().map(|x| x.trim()).collect();
    let mut red_max = 0;
    let mut green_max = 0;
    let mut blue_max = 0;
    for i in 2..(v.len() - 1) {
        let count: u32 = v[i].parse().unwrap_or(0);
        if count == 0 {
            continue;
        }
        if v[i + 1].contains("red") {
            red_max = red_max.max(count);
        } else if v[i + 1].contains("green") {
            green_max = green_max.max(count);
        } else if v[i + 1].contains("blue") {
            blue_max = blue_max.max(count);
        }
    }
    red_max * green_max * blue_max
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Error reading file");
    let result = input.lines().map(|x| elf_game(x)).sum::<u32>();
    println!("{}", result);
}
