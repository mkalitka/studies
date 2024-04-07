fn part_list(arr: Vec<&str>) -> String {
    let mut result = String::new();
    for i in 1..arr.len() {
        result.push_str(&format!("({}, {})", arr[..i].join(" "), arr[i..].join(" ")));
    }
    result
}

#[cfg(test)]
    mod tests {
    use super::*;

    fn dotest(arr: Vec<&str>, exp: &str) -> () {
        println!("arr: {:?}", arr);
        let ans = part_list(arr);
        println!("actual:\n{}", ans);
        println!("expect:\n{}", exp);
        println!("{}", ans == exp);
        assert_eq!(ans, exp);
        println!("{}", "-");
    }

    #[test]
    fn basis_tests() {
        dotest(vec!["I", "wish", "I", "hadn't", "come"],
                "(I, wish I hadn't come)(I wish, I hadn't come)(I wish I, hadn't come)(I wish I hadn't, come)");
        dotest(vec!["cdIw", "tzIy", "xDu", "rThG"], 
            "(cdIw, tzIy xDu rThG)(cdIw tzIy, xDu rThG)(cdIw tzIy xDu, rThG)");
        
    }

    #[test]
    fn test2() {
        dotest(vec!["I", "wish", "I", "hadn't", "come"],
                "(I, wish I hadn't come)(I wish, I hadn't come)(I wish I, hadn't come)(I wish I hadn't, come)");
    }

    #[test]
    fn test3() {
        dotest(vec!["vJQ", "anj", "mQDq", "sOZ"], 
            "(vJQ, anj mQDq sOZ)(vJQ anj, mQDq sOZ)(vJQ anj mQDq, sOZ)");
    }

    #[test]
    fn test4() {
        dotest(vec!["mkC", "WoiP", "pCHh", "mkv"], 
            "(mkC, WoiP pCHh mkv)(mkC WoiP, pCHh mkv)(mkC WoiP pCHh, mkv)");
    }

    #[test]
    fn test5() {
        dotest(vec!["vHW", "bPq", "pme", "jJr"], 
            "(vHW, bPq pme jJr)(vHW bPq, pme jJr)(vHW bPq pme, jJr)");
    }
}

