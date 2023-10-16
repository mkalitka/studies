fn convert_string_to_number(s: &str) -> i32 {
    s.parse().unwrap()
}

fn main() {
    println!("{}", convert_string_to_number("1234"));
    println!("{}", convert_string_to_number("605"));
    println!("{}", convert_string_to_number("1405"));
    println!("{}", convert_string_to_number("-7"));
    println!("{}", convert_string_to_number("42"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_convert_string_into_number() {
        assert_eq!(convert_string_to_number("1234"), 1234);
        assert_eq!(convert_string_to_number("605"), 605);
        assert_eq!(convert_string_to_number("1405"), 1405);
        assert_eq!(convert_string_to_number("-7"), -7);
        assert_eq!(convert_string_to_number("42"), 42);
    }
}
