use std::collections::HashMap;
use crate::parser::Command;

pub struct Turtle {
    pub x: f32,
    pub y: f32,
    pub angle: f32,
    pub pen_down: bool,
    pub color: String,
    pub label_height: f32,
    pub functions: HashMap<String, Vec<Command>>,
}

impl Turtle {
    pub fn new() -> Turtle {
        Turtle {
            x: 0.0,
            y: 0.0,
            angle: 0.0,
            pen_down: true,
            color: "black".to_string(),
            label_height: 10.0,
            functions: HashMap::new(),
        }
    }

    pub fn forward(&mut self, distance: f32) {
        let new_x = self.x + distance * self.angle.cos();
        let new_y = self.y + distance * self.angle.sin();

        if self.pen_down {
            println!("({}, {}) -> ({}, {}), color: {}", self.x, self.y, new_x, new_y, self.color);
        }

        self.x = new_x;
        self.y = new_y;
    }

    pub fn turn(&mut self, angle: f32) {
        self.angle += angle;
    }

    pub fn pen_up(&mut self) {
        self.pen_down = false;
    }

    pub fn pen_down(&mut self) {
        self.pen_down = true;
    }

    pub fn clear_screen(&mut self) {
        return;
    }

    pub fn set_color(&mut self, color: String) {
        self.color = color;
    }
    
    pub fn display_label(&mut self, label: String) {
        println!("({}, {}): {}, height: {}", self.x, self.y, self.label_height, label);
    }

    pub fn set_label_height(&mut self, height: f32) {
        self.label_height = height;
    }

    pub fn repeat(&mut self, times: f32, commands: &Command) {
        match commands {
            Command::List(commands) => {
                for _ in 0..times as i32 {
                    self.execute_vec(&commands);
                }
            }
            _ => panic!("Repeat command must have a list of commands"),
        }
    }

    // pub fn create_function(&mut self, name: String, commands: &Vec<Command>) {
    //     self.functions.insert(name, commands.clone());
    // }
    //
    // pub fn call_function(&mut self, name: String) {
    //     self.execute_vec(self.functions.get(&name).unwrap());
    // }

    pub fn execute(&mut self, command: &Command) {
        match command {
            Command::Forward(distance) => self.forward(distance.clone()),
            Command::Backward(distance) => self.forward(-distance.clone()),
            Command::Right(angle) => self.turn(angle.clone()),
            Command::Left(angle) => self.turn(-angle.clone()),
            Command::PenUp => self.pen_up(),
            Command::PenDown => self.pen_down(),
            Command::ClearScreen => self.clear_screen(),
            Command::SetColor(color) => self.set_color(color.clone()),
            Command::Label(label) => self.display_label(label.clone()),
            Command::SetLabelHeight(height) => self.set_label_height(height.clone()),
            Command::Window => return,
            Command::Repeat(times, commands) => self.repeat(times.clone(), commands),
            // Command::Function(name, commands) => self.create_function(name.clone(), commands),
            Command::Function(_name, _commands) => return,
            // Command::Call(name) => self.call_function(name.clone()),
            Command::Call(_name) => return,
            Command::HideTurtle => println!("Hiding turtle"),
            Command::ShowTurtle => println!("Showing turtle"),
            Command::List(_commands) => return,
        }
    }

    pub fn execute_vec(&mut self, commands: &Vec<Command>) {
        for command in commands {
            self.execute(command);
        }
    }
}
