fn last_digit(str1: &str, str2: &str) -> i32 {
    if str2 == "0" {
        return 1;
    }
    let mut base = str1.chars().last().unwrap().to_digit(10).unwrap();
    let mut exp = str2.chars().rev().collect::<String>().parse::<u32>().unwrap();
    let mut result = 1;
    while exp > 0 {
        if exp % 2 == 1 {
            result = (result * base) % 10;
        }
        exp >>= 1;
        base = (base * base) % 10;
    }
    result as i32
}

fn main() {
    println!("{}", last_digit("4", "1"));
    println!("{}", last_digit("4", "2"));
    println!("{}", last_digit("9", "7"));
}
