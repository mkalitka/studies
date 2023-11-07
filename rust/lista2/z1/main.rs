fn get_count(string: &str) -> usize {
    let mut vowels_count: usize = 0;
    let vowels: String = String::new("aeiou");
    for c in string.chars() {
        if vowels.contains(&c) {
            vowels_count += 1;
        }
    }
    vowels_count
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_count() {
        assert_eq!(get_count("abracadabra"), 5);
        assert_eq!(get_count("pear tree"), 4);
        assert_eq!(get_count("o a kak ushakov lil vo kashu kakao"), 13);
        assert_eq!(get_count("my pyx"), 0);
        assert_eq!(get_count("o"), 1);
    }
}
