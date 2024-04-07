use image::{RgbaImage, Rgba};
use std::ops;


#[derive(Copy, Clone)]
pub struct Complex{
    pub real: f64,
    pub imaginary: f64,
}


impl Complex{
    pub fn new(r: f64, i: f64) -> Complex{
        Complex{
            real: r,
            imaginary: i,
        }
    }
    pub fn norm(&self) -> f64{
        (self.real * self.real + self.imaginary * self.imaginary).sqrt()
    }
    
}

impl ops::Add<Complex> for Complex{
    type Output = Complex;
    fn add(self, other: Complex) -> Complex{
        Complex{
            real: self.real + other.real,
            imaginary: self.imaginary + other.imaginary,
        }
    }
}

impl ops::Sub<Complex> for Complex{
    type Output = Complex;
    fn sub(self, other: Complex) -> Complex{
        Complex{
            real: self.real - other.real,
            imaginary: self.imaginary - other.imaginary,
        }
    }
}

impl ops::Mul<Complex> for Complex{
    type Output = Complex;
    fn mul(self, other: Complex) -> Complex{
        Complex{
            real: self.real * other.real - self.imaginary * other.imaginary,
            imaginary: self.real * other.imaginary + self.imaginary * other.real,
        }
    }
}   

impl ops::Div<Complex> for Complex{
    type Output = Complex;
    fn div(self, other: Complex) -> Complex{
        Complex{
            real: (self.real * other.real + self.imaginary * other.imaginary)/(other.real * other.real + other.imaginary * other.imaginary),
            imaginary: (self.imaginary * other.real - self.real * other.imaginary)/(other.real * other.real + other.imaginary * other.imaginary),
        }
    }
}


fn mandelbrot(z: &Complex, max_iter: u64) -> u64 {
    let mut c = Complex::new(0.0, 0.0);
    let mut n = 0;

    while n < max_iter {
        c = c * c + *z;

        if c.norm() > 4.0 {
            break;
        }
        n += 1;
    }

    n
}


pub fn gen_image(width: usize, height: usize, xmin: f64, xmax: f64, ymin: f64, ymax: f64) -> RgbaImage {
    let max_iter = 256;
    let mut imgbuf = RgbaImage::new(width as u32, height as u32);
    for y in 0..height {
        for x in 0..width {
            let real = xmin + (x as f64 / width as f64) * (xmax - xmin) ;
            let imaginary = ymin + (y as f64 / height as f64) * (ymax - ymin);
            
            let z = Complex::new(real, imaginary);
            let color = mandelbrot(&z, max_iter);
    
            let r = (color * 8 % 255) as u8;
            let g = (color * 4 % 255) as u8;
            let b = (color * 16 % 255) as u8;
            let a = 255; 
    
            let pixel = imgbuf.get_pixel_mut(x as u32, y as u32);
            *pixel = Rgba([r, g, b, a]);
        }
    }

    imgbuf
}
