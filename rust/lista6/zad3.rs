// Write a function that computes the nth hamming number.

fn hamming(n: usize) -> u64 {
    let mut hamming_numbers = vec![1];
    let mut i2 = 0;
    let mut i3 = 0;
    let mut i5 = 0;
    for _ in 1..n {
        let next_hamming = std::cmp::min(
            hamming_numbers[i2] * 2,
            std::cmp::min(hamming_numbers[i3] * 3, hamming_numbers[i5] * 5),
        );
        hamming_numbers.push(next_hamming);
        if next_hamming == hamming_numbers[i2] * 2 {
            i2 += 1;
        }

        if next_hamming == hamming_numbers[i3] * 3 {
            i3 += 1;
        }

        if next_hamming == hamming_numbers[i5] * 5 {
            i5 += 1;
        }
    }
    hamming_numbers[n - 1]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_hamming_1() {
        assert_eq!(hamming(1), 1);
    }

    #[test]
    fn test_hamming_2() {
        assert_eq!(hamming(5), 5);
    }

    #[test]
    fn test_hamming_3() {
        assert_eq!(hamming(10), 12);
    }

    #[test]
    fn test_hamming_4() {
        assert_eq!(hamming(20), 36);
    }

    #[test]
    fn test_hamming_5() {
        assert_eq!(hamming(100), 1536);
    }
}
