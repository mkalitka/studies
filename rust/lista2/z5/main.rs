fn gimme_the_letters(sp: &str) -> String {
    let mut chars = sp.chars();
    let start = chars.next().unwrap();
    let end = chars.last().unwrap();
    (start..=end).collect().to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_gimme_the_letters() {
        assert_eq!(gimme_the_letters("a-z"), "abcdefghijklmnopqrstuvwxyz");
        assert_eq!(gimme_the_letters("h-o"), "hijklmno");
        assert_eq!(gimme_the_letters("Q-Z"), "QRSTUVWXYZ");
        assert_eq!(gimme_the_letters("J-J"), "J");
        assert_eq!(gimme_the_letters("a-b"), "ab");
    }
}
