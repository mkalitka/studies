fn calc_function(x: f64) -> f64 {
    4046.0 / ((x.powf(14.0) + 1.0).sqrt() + 1.0)
}

fn main() {
    println!("{}", calc_function(0.001));
}
