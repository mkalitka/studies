fn reverse_words(str: &str) -> String {
    str.split(" ")
        .map(|word| word.chars().rev().collect::<String>())
        .collect::<Vec<String>>()
        .join(" ")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reverse_words_1() {
        assert_eq!(reverse_words("The quick brown fox jumps over the lazy dog."), "ehT kciuq nworb xof spmuj revo eht yzal .god");
    }

    #[test]
    fn test_reverse_words_2() {
        assert_eq!(reverse_words("apple"), "elppa");
    }

    #[test]
    fn test_reverse_words_3() {
        assert_eq!(reverse_words("a b c d"), "a b c d");
    }

    #[test]
    fn test_reverse_words_4() {
        assert_eq!(reverse_words("double  spaced  words"), "elbuod  decaps  sdrow");
    }

    #[test]
    fn test_reverse_words_5() {
        assert_eq!(reverse_words("stressed desserts"), "desserts stressed");
    }
}
