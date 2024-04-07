use std::fs;

fn elf_game(s: &str) -> u32 {
    let v: Vec<&str> = s.split_whitespace().map(|x| x.trim()).collect();
    for i in 2..(v.len() - 1) {
        let count: u32 = v[i].parse().unwrap_or(0);
        if count == 0 {
            continue;
        }
        if v[i + 1].contains("red") && count > 12 {
            return 0;
        }
        if v[i + 1].contains("green") && count > 13 {
            return 0;
        }
        if v[i + 1].contains("blue") && count > 14 {
            return 0;
        }
    }
    v[1][..v[1].len() - 1].parse().unwrap_or(0)
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Error reading file");
    let result = input.lines().map(|x| elf_game(x)).sum::<u32>();
    println!("{}", result);
}
