fn likes(names: &[&str]) -> String {
    match names.len() {
        0 => "no one likes this".to_string(),
        1 => format!("{} likes this", names[0]),
        2 => format!("{} and {} like this", names[0], names[1]),
        3 => format!("{}, {} and {} like this", names[0], names[1], names[2]),
        _ => format!("{}, {} and {} others like this", names[0], names[1], names.len() - 2),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_1() {
        assert_eq!(likes(&[]), "no one likes this");
    }

    #[test]
    fn test_basic_2() {
        assert_eq!(likes(&["Alex", "Jacob", "Mark", "Max"]), "Alex, Jacob and 2 others like this");
    }

    #[test]
    fn test_basic_3() {
        assert_eq!(likes(&["Alex", "Jacob", "Mark"]), "Alex, Jacob and Mark like this");
    }

    #[test]
    fn test_basic_4() {
        assert_eq!(likes(&["Alex", "Jacob"]), "Alex and Jacob like this");
    }

    #[test]
    fn test_basic_5() {
        assert_eq!(likes(&["Alex"]), "Alex likes this");
    }
}
