fn descending_order(x: u64) -> u64 {
    let mut digits: Vec<char> = x.to_string().chars().collect();
    digits.sort();
    digits.into_iter().rev().collect::<String>().parse().unwrap()
}

fn main() {
    println!("{}", descending_order(123456789));
}
