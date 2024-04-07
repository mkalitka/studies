extern crate nom;

use nom::{
    branch::alt,
    bytes::complete::{is_not, tag},
    character::complete::{alphanumeric1, multispace0, multispace1},
    multi::many0,
    number::complete::float,
    IResult,
};

#[derive(Debug, PartialEq, Clone)]
pub enum Command {
    Forward(f32),
    Backward(f32),
    Right(f32),
    Left(f32),
    PenUp,
    PenDown,
    ClearScreen,
    SetColor(String),
    Label(String),
    SetLabelHeight(f32),
    List(Vec<Command>),
    Repeat(f32, Box<Command>),
    Function(String, Vec<Command>),
    Call(String),
    Window,
    HideTurtle,
    ShowTurtle,
}

fn parse_number(input: &str) -> IResult<&str, f32> {
    float(input)
}

fn parse_forward(input: &str) -> IResult<&str, Command> {
    let (input, _) = alt((
        tag("fd"),
        tag("forward"),
    ))(input)?;
    let (input, _) = multispace1(input)?;
    let (input, number) = parse_number(input)?;
    Ok((input, Command::Forward(number)))
}

fn parse_backward(input: &str) -> IResult<&str, Command> {
    let (input, _) = alt((
        tag("bk"),
        tag("backward"),
    ))(input)?;
    let (input, _) = multispace1(input)?;
    let (input, number) = parse_number(input)?;
    Ok((input, Command::Backward(number)))
}

fn parse_right(input: &str) -> IResult<&str, Command> {
    let (input, _) = alt((
        tag("rt"),
        tag("right"),
    ))(input)?;
    let (input, _) = multispace1(input)?;
    let (input, number) = parse_number(input)?;
    Ok((input, Command::Right(number)))
}

fn parse_left(input: &str) -> IResult<&str, Command> {
    let (input, _) = alt((
        tag("lt"),
        tag("left"),
    ))(input)?;
    let (input, _) = multispace1(input)?;
    let (input, number) = parse_number(input)?;
    Ok((input, Command::Left(number)))
}

fn parse_penup(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("penup")(input)?;
    Ok((input, Command::PenUp))
}

fn parse_pendown(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("pendown")(input)?;
    Ok((input, Command::PenDown))
}

fn parse_clearscreen(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("clearscreen")(input)?;
    Ok((input, Command::ClearScreen))
}

fn parse_label(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("label")(input)?;
    let (input, _) = multispace1(input)?;
    let (input, _) = tag(r#"""#)(input)?;
    let (input, label) = is_not(r#"""#)(input)?;
    let (input, _) = tag(r#"""#)(input)?;
    Ok((input, Command::Label(label.to_string())))
}

fn parse_list(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("[")(input)?;
    let (input, command) = many0(parse_command)(input)?;
    let (input, _) = tag("]")(input)?;
    Ok((input, Command::List(command)))
}

fn parse_repeat(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("repeat")(input)?;
    let (input, _) = multispace1(input)?;
    let (input, number) = parse_number(input)?;
    let (input, _) = multispace1(input)?;
    let (input, command) = parse_list(input)?;
    Ok((input, Command::Repeat(number, Box::new(command))))
}

fn parse_setlabelheight(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("setlabelheight")(input)?;
    let (input, _) = multispace1(input)?;
    let (input, number) = parse_number(input)?;
    Ok((input, Command::SetLabelHeight(number)))
}

fn parse_setcolor(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("setcolor")(input)?;
    let (input, _) = multispace1(input)?;
    let (input, color) = alphanumeric1(input)?;
    Ok((input, Command::SetColor(color.to_string())))
}

fn parse_function(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("to")(input)?;
    let (input, _) = multispace1(input)?;
    let (input, name) = alphanumeric1(input)?;
    let (input, _) = multispace1(input)?;
    let (input, commands) = many0(parse_command)(input)?;
    let (input, _) = tag("end")(input)?;
    Ok((input, Command::Function(name.to_string(), commands)))
}

fn parse_call(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("call")(input)?;
    let (input, _) = multispace1(input)?;
    let (input, name) = alphanumeric1(input)?;
    Ok((input, Command::Call(name.to_string())))
}

fn parse_hide_turtle(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("hideturtle")(input)?;
    Ok((input, Command::HideTurtle))
}

fn parse_show_turtle(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("showturtle")(input)?;
    Ok((input, Command::ShowTurtle))
}

fn parse_window(input: &str) -> IResult<&str, Command> {
    let (input, _) = tag("window")(input)?;
    Ok((input, Command::Window))
}

fn parse_command(input: &str) -> IResult<&str, Command> {
    let (input, _) = multispace0(input)?;
    let (input, command) = alt((
        parse_forward,
        parse_backward,
        parse_right,
        parse_left,
        parse_penup,
        parse_pendown,
        parse_setcolor,
        parse_clearscreen,
        parse_label,
        parse_setlabelheight,
        parse_repeat,
        parse_function,
        parse_call,
        parse_window,
        parse_hide_turtle,
        parse_show_turtle,
    ))(input)?;
    let (input, _) = multispace0(input)?;
    Ok((input, command))
}

pub fn parse(input: &str) -> IResult<&str, Vec<Command>> {
    let (input, commands) = many0(parse_command)(input)?;
    if input.len() > 0 {
        panic!("Failed to parse: {}", input);
    }
    Ok((input, commands))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse() {
        let input = r#"
            forward 100
            bk 100
            rt 90
            lt 90
            penup
            pendown
            setcolor red
            clearscreen
            label "Hello World"
            setlabelheight 20
            repeat 4 [fd 100 rt 90]
            to square repeat 4 [fd 100 rt 90]
            hideturtle
            end
            call square
        "#;
        let result = parse(input).unwrap();
        let expected = vec![
            Command::Forward(100.0),
            Command::Backward(100.0),
            Command::Right(90.0),
            Command::Left(90.0),
            Command::PenUp,
            Command::PenDown,
            Command::SetColor("red".to_string()),
            Command::ClearScreen,
            Command::Label("Hello World".to_string()),
            Command::SetLabelHeight(20.0),
            Command::Repeat(
                4.0,
                Box::new(Command::List(vec![
                    Command::Forward(100.0),
                    Command::Right(90.0),
                ])),
            ),
            Command::Function(
                "square".to_string(),
                vec![Command::Repeat(
                    4.0,
                    Box::new(Command::List(vec![
                        Command::Forward(100.0),
                        Command::Right(90.0),
                    ])),
                ), Command::HideTurtle],
            ),
            Command::Call("square".to_string()),
        ];
        assert_eq!(result, ("", expected));
    }

    #[test]
    fn test_parse_2() {
        let input = r#"
            repeat 4 [fd 100 rt 90]
            to square repeat 4 [fd 100 rt 90]
            end
            call square
        "#;
        let result = parse(input).unwrap();
        let expected = vec![
            Command::Repeat(
                4.0,
                Box::new(Command::List(vec![
                    Command::Forward(100.0),
                    Command::Right(90.0),
                ])),
            ),
            Command::Function(
                "square".to_string(),
                vec![Command::Repeat(
                    4.0,
                    Box::new(Command::List(vec![
                        Command::Forward(100.0),
                        Command::Right(90.0),
                    ])),
                )],
            ),
            Command::Call("square".to_string()),
        ];
        assert_eq!(result, ("", expected));
    }

    #[test]
    fn test_parse_3() {
        let input = r#"
            hideturtle
            showturtle
            window
        "#;
        let result = parse(input).unwrap();
        let expected = vec![
            Command::HideTurtle,
            Command::ShowTurtle,
            Command::Window,
        ];
        assert_eq!(result, ("", expected));
    }

    #[test]
    fn test_parse_4() {
        let input = r#"
            fd 100
            rt 90
            repeat 2 [fd 100 rt 90]
            label "Hello World"
        "#;
        let result = parse(input).unwrap();
        let expected = vec![
            Command::Forward(100.0),
            Command::Right(90.0),
            Command::Repeat(
                2.0,
                Box::new(Command::List(vec![
                    Command::Forward(100.0),
                    Command::Right(90.0),
                ])),
            ),
            Command::Label("Hello World".to_string()),
        ];
        assert_eq!(result, ("", expected));
    }

    #[test]
    fn test_parse_5() {
        let input = r#"
            clearscreen
        "#;
        let result = parse(input).unwrap();
        let expected = vec![
            Command::ClearScreen,
        ];
        assert_eq!(result, ("", expected));
    }
}
