fn even_numbers(array: &Vec<i32>, number: usize) -> Vec<i32> {
    let even: Vec<i32> = array.iter().filter(|&x| x % 2 == 0).cloned().collect();
    even[even.len().saturating_sub(number)..].to_vec()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        assert_eq!(even_numbers(&vec![1, 2, 3, 4, 5, 6, 7, 8, 9], 3), vec![4, 6, 8]);
    }

    #[test]
    fn test2() {
        assert_eq!(even_numbers(&vec![1, 2, 3, 4, 5, 6, 7, 8, 9], 1), vec![8]);
    }

    #[test]
    fn test3() {
        assert_eq!(even_numbers(&vec![1, 2, 3, 4, 5, 6, 7, 8, 9], 0), vec![]);
    }

    #[test]
    fn test4() {
        assert_eq!(even_numbers(&vec![1, 2, 3, 4, 5, 6, 7, 8, 9], 9), vec![2, 4, 6, 8]);
    }

    #[test]
    fn test5() {
        assert_eq!(even_numbers(&vec![1, 2, 3, 4, 5, 6, 7, 8, 9], 10), vec![2, 4, 6, 8]);
    }
}
