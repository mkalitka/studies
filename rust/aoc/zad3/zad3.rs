use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Error reading file");
    //let mut sum = 0;
    let mut lines = contents.split("\n").collect::<Vec<&str>>();
    for i in 0..(lines.len()) {

    }
}
