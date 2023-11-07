fn double_f(x: f64) -> f64 {
    14.0 * (1.0 - (17.0 * x).cos()) / x.powf(2.0)
}

fn main() {
    for i in 11..21 {
        println!("10^-{}: {}", i, double_f(10.0_f64.powi(-i)));
    }
}
