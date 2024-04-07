fn comp(a: Vec<i64>, b: Vec<i64>) -> bool {
    if a.len() != b.len() {
        return false;
    }
    let mut a = a;
    let mut b = b;
    a.sort();
    b.sort();
    for i in 0..a.len() {
        if a[i] * a[i] != b[i] {
            return false;
        }
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert!(comp(vec![121, 144, 19, 161, 19, 144, 19, 11], vec![121, 14641, 20736, 361, 25921, 361, 20736, 361]));
    }

    #[test]
    fn test_2() {
        assert!(comp(vec![1, 2, 3, 4], vec![1, 4, 9, 16]));
    }

    #[test]
    fn test_3() {
        assert!(!comp(vec![1, 2, 3, 4], vec![1, 4, 9]));
    }

    #[test]
    fn test_4() {
        assert!(comp(vec![1, 2, 5, 4], vec![1, 4, 16, 25]));
    }

    #[test]
    fn test_5() {
        assert!(comp(vec![3, 2, 5, 4], vec![9, 4, 16, 25]));
    }
}
