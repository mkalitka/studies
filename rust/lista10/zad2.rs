fn dig_pow(n: i64, p: i32) -> i64 {
    let x: i64 = n.to_string()
        .chars()
        .map(|c| c.to_digit(10).unwrap() as i64)
        .enumerate()
        .map(|(i, x)| x.pow(i as u32 + p as u32))
        .sum();
    
    match x % n {
        0 => x / n,
        _ => -1,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn dotest(n: i64, p: i32, exp: i64) -> () {
        println!("n: {:?};", n);
        println!("p: {:?};", p);
        let ans = dig_pow(n, p);
        println!(" actual:\n{:?};", ans);
        println!("expect:\n{:?};", exp);
        println!("{};", ans == exp);
        assert_eq!(ans, exp);
        println!("{};", "-");
    }

    #[test]
    fn test_1() {
        dotest(89, 1, 1);
    }

    #[test]
    fn test_2() {
        dotest(92, 1, -1);
    }

    #[test]
    fn test_3() {
        dotest(46288, 3, 51);
    }

    #[test]
    fn test_4() {
        dotest(114, 3, 9)
    }

    #[test]
    fn test_5() {
        dotest(46288, 5, -1)
    }
}
