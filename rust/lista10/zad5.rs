fn print(n: i32) -> Option<String> {
    if n%2 == 0 || n < 1 {
        return None;
    }

    let mut result = String::new();

    for i in 0..n {
        let space = (n/2 - i).abs();
        let asterisk = n - (space * 2);
        
        for _ in 0..space {
            result.push(' ');
        }
        
        for _ in 0..asterisk {
            result.push('*');
        }
        result += "\n";
        
    }

    Some(result)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        assert_eq!(print(1), Some("*\n".to_string()));
    }

    #[test]
    fn test_3() {
        assert_eq!(print(3), Some(" *\n***\n *\n".to_string()));
    }

    #[test]
    fn test_5() {
        assert_eq!(print(5), Some("  *\n ***\n*****\n ***\n  *\n".to_string()));
    }

    #[test]
    fn test_7() {
        assert_eq!(print(7), Some("   *\n  ***\n *****\n*******\n *****\n  ***\n   *\n".to_string()));
    }

    #[test]
    fn test_2() {
        assert_eq!(print(2), None);
    }
}
