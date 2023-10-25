fn number(bus_stops:&[(i32, i32)]) -> i32 {
    bus_stops.iter().fold(0, |acc, (on, off)| acc + on - off)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn returns_expected() {
        assert_eq!(number(&[(10,0),(3,5),(5,8)]), 5);
        assert_eq!(number(&[(3,0),(9,1),(4,10),(12,2),(6,1),(7,10)]), 17);
        assert_eq!(number(&[(3,0),(9,1),(4,8),(12,2),(6,1),(7,8)]), 21);
        assert_eq!(number(&[(0,0)]), 0);
        assert_eq!(number(&[(21,0),(10,8),(9,4),(10,1)]), 37);
    }
}
