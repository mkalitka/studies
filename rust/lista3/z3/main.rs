struct Cipher {
    map1: String,
    map2: String,
}

impl Cipher {
    fn new(map1: &str, map2: &str) -> Cipher {
        Cipher {
            map1: map1.to_string(),
            map2: map2.to_string(),
        }
    }

    fn encode(&self, string: &str) -> String {
        let mut result = String::new();
        for c in string.chars() {
            let index = self.map1.find(c);
            if index.is_none() {
                result.push(c);
            } else {
                result.push(self.map2.chars().nth(index.unwrap()).unwrap());
            }
        }
        result
    }

    fn decode(&self, string: &str) -> String {
        let mut result = String::new();
        for c in string.chars() {
            let index = self.map2.find(c);
            if index.is_none() {
                result.push(c);
            } else {
                result.push(self.map1.chars().nth(index.unwrap()).unwrap());
            }
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";
        let cipher = Cipher::new(map1, map2);
        assert_eq!(cipher.encode("abc"), "eta");
        assert_eq!(cipher.encode("xyz"), "qxz");
        assert_eq!(cipher.decode("eirfg"), "aeiou");
        assert_eq!(cipher.decode("erlang"), "aikcfu");
        assert_eq!(cipher.encode("git"), "srb");
    }
}
