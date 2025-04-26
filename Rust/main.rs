use std::str;

#[derive(Debug)]
#[derive(Copy, Clone)]
enum TokenType
{

}



#[derive(Copy, Clone)]
pub struct Token<'a>
{
	token_type: TokenType,
	literal: &'a str,

	c0: usize,
	l0: usize,

	l1: usize,
	c1: usize
}

pub struct Lexer<'a>
{
	tokens: Vec<Token<'a>>,
	cursor: i32
}

fn parse_next_token()
{

}

fn create_lexer()
{
	
}
