fn count_odd_pentafib(n: u16) -> u16 {
    (n + 4) / 6 + (n + 5) / 6 - if n >= 2 { 1 } else { 0 }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_0() {
        assert_eq!(count_odd_pentafib(0), 0);
    }

    #[test]
    fn test_10() {
        assert_eq!(count_odd_pentafib(10), 3);
    }

    #[test]
    fn test_15() {
        assert_eq!(count_odd_pentafib(15), 5);
    }

    #[test]
    fn test_20() {
        assert_eq!(count_odd_pentafib(20), 7);
    }

    #[test]
    fn test_68() {
        assert_eq!(count_odd_pentafib(68), 23);
    }
}
