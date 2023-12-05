fn capitalize(s: &str) -> Vec<String> {
    vec![
        s.chars().enumerate().map(|(i, c)| {
            if i % 2 == 0 {
                c.to_uppercase().to_string()
            } else {
                c.to_lowercase().to_string()
            }
        }).collect::<Vec<String>>().join(""),
        s.chars().enumerate().map(|(i, c)| {
            if i % 2 == 1 {
                c.to_uppercase().to_string()
            } else {
                c.to_lowercase().to_string()
            }
        }).collect::<Vec<String>>().join("")
    ]
}

fn main() {
    let s = "alamakota";
    let result = capitalize(s);
    println!("{:?}", result);
}
