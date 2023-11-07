fn f_double(x: f64) -> f64 {
    4046.0 * ((x.powf(14.0) + 1.0) - 1.0) / x.powf(14.0)
}

fn main() {
    println!("{}", f_double(0.001));
}
