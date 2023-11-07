fn f(x: f64) -> f64 {
    x - 0.49
}

fn main() {
    let mut a = 0.0;
    let mut b = 1.0;
    let mut c = (a + b) / 2.0;
    for i in 0..5 {
        if f(a) * f(c) < 0.0 {
            b = c;
        } else {
            a = c;
        }
        let e = (0.49 - c).abs();
        println!("{}: c = {}, e = {}", i, c, e);
        c = (a + b) / 2.0;
    }
}
