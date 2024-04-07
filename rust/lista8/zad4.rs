fn john_ann(n: i32) -> (Vec<i32>, Vec<i32>) {
    let mut john = vec![0; n as usize];
    let mut ann = vec![0; n as usize];
    john[0] = 0;
    ann[0] = 1;
    for i in 1..n as usize {
        john[i] = i as i32 - ann[john[i - 1] as usize];
        ann[i] = i as i32 - john[ann[i - 1] as usize];
    }
    (john, ann)
}

fn john(n: i32) -> Vec<i32> {
    john_ann(n).0
}

fn ann(n: i32) -> Vec<i32> {
    john_ann(n).1
}

fn sum_john(n: i32) -> i32 {
    john(n).iter().sum()
}

fn sum_ann(n: i32) -> i32 {
    ann(n).iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_john() {
        assert_eq!(john(11), vec![0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6]);
        assert_eq!(john(14), vec![0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8]);
    }
    #[test]
    fn test_ann() {
        assert_eq!(ann(6), vec![1, 1, 2, 2, 3, 3]);
        assert_eq!(ann(15), vec![1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9]);
    }
    #[test]
    fn test_sum_john() {
        assert_eq!(sum_john(75), 1720);
        assert_eq!(sum_john(78), 1861);
    }
    #[test]
    fn test_sum_ann() {
        assert_eq!(sum_ann(115), 4070);
        assert_eq!(sum_ann(150), 6930);
    }
    #[test]
    fn test_johnn() {
        assert_eq!(john(1), vec![0]);
    }
}
