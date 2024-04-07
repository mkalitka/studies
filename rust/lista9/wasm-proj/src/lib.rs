mod fractal;

use wasm_bindgen::prelude::*;
use fractal::gen_image;

#[wasm_bindgen]
pub fn generate_fractal(width: usize, height: usize, xmin: f64, xmax: f64, ymin: f64, ymax: f64) -> Vec<u8> {
    let img = gen_image(width, height, xmin, xmax, ymin, ymax);

    img.into_raw()
}
