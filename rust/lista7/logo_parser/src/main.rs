mod turtle;
mod parser;

use parser::parse;
use turtle::Turtle;

fn main() {
    let mut turtle = Turtle::new();
    let commands = parse("fd 100 rt 90 fd 100 setcolor yellow showturtle hideturtle penup fd 100 pendown rt 20 fd 30 repeat 4 [fd 10 rt 90]").unwrap().1;
    turtle.execute_vec(&commands);
}
