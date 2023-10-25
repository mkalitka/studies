fn longest(a1: &str, a2: &str) -> String {
    let mut chars: Vec<char> = vec![];
    
    for c in a1.chars() {
        if !chars.contains(&c) {
            chars.push(c);
        }
    }
    
    for c in a2.chars() {
        if !chars.contains(&c) {
            chars.push(c);
        }
    }

    chars.sort();
    chars.into_iter().collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_longest() {
        assert_eq!(longest("aretheyhere", "yestheyarehere"), "aehrsty");
        assert_eq!(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu");
        assert_eq!(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy");
        assert_eq!(longest("lordsofthefallen", "gamekult"), "adefghklmnorstu");
        assert_eq!(longest("codewars", "codewars"), "acdeorsw");
    }
}
