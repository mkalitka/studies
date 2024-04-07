fn first_n_smallest(arr: &[i32], n: usize) -> Vec<i32> {
    if n == 0 {
        return Vec::new();
    }
    let nth = {
        let mut arr = arr.to_vec();
        arr.sort();
        arr[n-1]
    };
    let mut result = arr.to_vec();
    result.retain(|&x| x <= nth);
    while result.len() > n {
        result.pop();
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_1() {
        assert_eq!(first_n_smallest(&[1,2,3,4,5],3), [1,2,3]);
    }

    #[test]
    fn test_basic_2() {
        assert_eq!(first_n_smallest(&[5,4,3,2,1],3), [3,2,1]);
    }

    #[test]
    fn test_basic_3() {
        assert_eq!(first_n_smallest(&[1,2,3,1,2],3), [1,2,1]);
    }

    #[test]
    fn test_basic_4() {
        assert_eq!(first_n_smallest(&[1,2,3,-4,0],3), [1,-4,0]);
    }

    #[test]
    fn test_basic_5() {
        assert_eq!(first_n_smallest(&[1,2,3,4,5],0), []);
    }
}

