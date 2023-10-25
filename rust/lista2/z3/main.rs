fn summy(strng: &str) -> i32 {
    strng.split_whitespace().map(|x| x.parse::<i32>().unwrap()).sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn returns_expected() {
        assert_eq!(summy("1 2 3"), 6);
        assert_eq!(summy("1 2 3 4"), 10);
        assert_eq!(summy("1 2 3 4 5"), 15);
        assert_eq!(summy("10 10"), 20);
        assert_eq!(summy("0 0"), 0);
    }
}
