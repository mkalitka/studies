struct Sudoku {
    data: Vec<Vec<u32>>,
}

impl Sudoku {
    fn is_valid(&self) -> bool {
        let n = self.data.len();
        let sqrt_n = (n as f64).sqrt() as usize;
        if sqrt_n * sqrt_n != n {
            return false;
        }

        let mut rows = vec![vec![false; n]; n];
        let mut cols = vec![vec![false; n]; n];
        let mut squares = vec![vec![false; n]; n];

        for i in 0..n {
            if self.data[i].len() != n {
                return false;
            }
            for j in 0..n {
                let val = self.data[i][j];
                if val == 0 || val > n as u32 {
                    return false;
                }
                let val = val - 1;

                if rows[i][val as usize] {
                    return false;
                }
                rows[i][val as usize] = true;

                if cols[j][val as usize] {
                    return false;
                }
                cols[j][val as usize] = true;

                let square = (i / sqrt_n) * sqrt_n + j / sqrt_n;
                if squares[square][val as usize] {
                    return false;
                }
                squares[square][val as usize] = true;
            }
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_1() {
        let sudoku = Sudoku {
            data: vec![
                vec![7,8,4, 1,5,9, 3,2,6],
                vec![5,3,9, 6,7,2, 8,4,1],
                vec![6,1,2, 4,3,8, 7,5,9],

                vec![9,2,8, 7,1,5, 4,6,3],
                vec![3,5,7, 8,4,6, 1,9,2],
                vec![4,6,1, 9,2,3, 5,8,7],

                vec![8,7,6, 3,9,4, 2,1,5],
                vec![2,4,3, 5,6,1, 9,7,8],
                vec![1,9,5, 2,8,7, 6,3,4],
            ],
        };
        assert!(sudoku.is_valid());
    }

    #[test]
    fn test_valid_2() {
        let sudoku = Sudoku {
            data: vec![
                vec![1,4, 2,3],
                vec![3,2, 4,1],

                vec![4,1, 3,2],
                vec![2,3, 1,4],
            ],
        };
        assert!(sudoku.is_valid());
    }

    #[test]
    fn test_valid_3() {
        let sudoku = Sudoku {
            data: vec![
                vec![1,2, 3,4],
                vec![3,4, 2,1],

                vec![4,3, 1,2],
                vec![2,1, 4,3],
            ],
        };
        assert!(sudoku.is_valid());
    }

    #[test]
    fn test_invalid_1() {
        let sudoku = Sudoku{
            data: vec![
                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],

                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],
                
                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],
                vec![1,2,3, 4,5,6, 7,8,9],
            ],
        };
        assert!(!sudoku.is_valid());
    }

    #[test]
    fn test_invalid_2() {
        let sudoku = Sudoku{
            data: vec![
                vec![1,2,3,4,5],
                vec![1,2,3,4],
                vec![1,2,3,4],
                vec![1],
            ],
        };
        assert!(!sudoku.is_valid());
    }
}

