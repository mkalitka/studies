fn expanded_form(n: u64) -> String {
    let mut result = String::new();
    let mut n = n;
    let mut i = 1;
    while n > 0 {
        if n % 10 != 0 {
            if result.len() > 0 {
                result.insert_str(0, " + ");
            }
            result.insert_str(0, &format!("{}", n % 10 * i));
        }
        n /= 10;
        i *= 10;
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(expanded_form(12), "10 + 2");
    }

    #[test]
    fn test_2() {
        assert_eq!(expanded_form(42), "40 + 2");
    }

    #[test]
    fn test_3() {
        assert_eq!(expanded_form(70304), "70000 + 300 + 4");
    }

    #[test]
    fn test_4() {
        assert_eq!(expanded_form(9000000), "9000000");
    }

    #[test]
    fn test_5() {
        assert_eq!(expanded_form(9000001), "9000000 + 1");
    }
}
