fn calka(n: u32) -> f32 {
    if n == 0 {
        ((2024.0/2023.0) as f32).ln()
    } else {
        1.0 / (n as f32) - 2023.0 * calka(n - 1)
    }
}

fn main() {
    for i in 1..21 {
        println!("calka({}) = {}", i, calka(i));
    }
}
