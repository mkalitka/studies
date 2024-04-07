fn encode(msg: String, n: i32) -> Vec<i32> {
    let mut result: Vec<i32> = Vec::new();
    let n = n.to_string().chars().map(|c| c.to_digit(10).unwrap() as i32).collect::<Vec<i32>>();
    let msg = msg.chars().map(|c| c.to_digit(36).unwrap() as i32 - 9).collect::<Vec<i32>>();
    let mut i = 0;
    while i < msg.len() {
        result.push(msg[i] + n[i % n.len()]);
        i += 1;
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(encode("scout".to_string(), 1939), vec![20, 12, 18, 30, 21]);
    }

    #[test]
    fn test_2() {
        assert_eq!(encode("masterpiece".to_string(), 1939), vec![14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]);
    }

    #[test]
    fn test_3() {
        assert_eq!(encode("nomoretears".to_string(), 12), vec![15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20]);
    }

    #[test]
    fn test_4() {
        assert_eq!(encode("super".to_string(), 31), vec![22, 22, 19, 6, 21]);
    }

    #[test]
    fn test_5() {
        assert_eq!(encode("hello".to_string(), 15), vec![9, 10, 13, 17, 16]);
    }
}
