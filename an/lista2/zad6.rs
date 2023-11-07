fn d(x: f64, y: f64) -> f64 {
    if y > x {
        let tmp = x;
        let x = y;
        let y = tmp;
    }
    x * (1.0 + (y.powi(2) / x.powi(2))).sqrt()
}
