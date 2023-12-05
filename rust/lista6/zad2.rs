mod solution {
    pub fn range_extraction(a: &[i32]) -> String {
        a.iter()
            .fold(Vec::new(), |mut acc, &x| {
                if acc.is_empty() {
                    acc.push(vec![x]);
                } else {
                    let last = acc.last_mut().unwrap();
                    if last.last().unwrap() + 1 == x {
                        last.push(x);
                    } else {
                        acc.push(vec![x]);
                    }
                }
                acc
            })
            .iter()
            .map(|x| match x.len() {
                1 => x[0].to_string(),
                2 => format!("{},{}", x[0], x[1]),
                _ => format!("{}-{}", x[0], x.last().unwrap()),
            })
            .collect::<Vec<String>>()
            .join(",")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_range_extraction_1() {
        assert_eq!(solution::range_extraction(&[-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9]), "-6,-3-1,3-5,7-9");
    }

    #[test]
    fn test_range_extraction_2() {
        assert_eq!(solution::range_extraction(&[-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]), "-3--1,2,10,15,16,18-20");
    }

    #[test]
    fn test_range_extraction_3() {
        assert_eq!(solution::range_extraction(&[1, 2, 3, 4, 5]), "1-5");
    }

    #[test]
    fn test_range_extraction_4() {
        assert_eq!(solution::range_extraction(&[1, 2]), "1,2");
    }

    #[test]
    fn test_range_extraction_5() {
        assert_eq!(solution::range_extraction(&[1]), "1");
    }
}
