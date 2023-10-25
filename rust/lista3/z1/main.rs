fn row_sum_odd_numbers(n: i64) -> i64 {
    n.pow(3)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn basic() {
        assert_eq!(row_sum_odd_numbers(1), 1);
        assert_eq!(row_sum_odd_numbers(2), 8);
        assert_eq!(row_sum_odd_numbers(13), 2197);
        assert_eq!(row_sum_odd_numbers(19), 6859);
        assert_eq!(row_sum_odd_numbers(41), 68921);
    }
}
