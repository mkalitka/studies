fn count_red_beads(n: u32) -> u32 {
    n.saturating_sub(1) * 2
}

fn main() {
    println!("{}", count_red_beads(0));
    println!("{}", count_red_beads(1));
    println!("{}", count_red_beads(3));
    println!("{}", count_red_beads(5));
    println!("{}", count_red_beads(6));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_count_red_beads() {
        assert_eq!(count_red_beads(0), 0);
        assert_eq!(count_red_beads(1), 0);
        assert_eq!(count_red_beads(3), 4);
        assert_eq!(count_red_beads(5), 8);
        assert_eq!(count_red_beads(6), 10);
    }
}
