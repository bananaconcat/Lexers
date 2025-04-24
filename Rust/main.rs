use std::str;

#[derive(Debug)]
#[derive(Copy, Clone)]
enum TokenType
{
	Identifier,
	Symbol,
	DataType,
	Keyword
}



#[derive(Copy, Clone)]
pub struct Token<'a>
{
	token_type: TokenType,
	literal: &'a str
}

pub fn tokenize(source_code: &str) -> Vec<Token>
{
	let mut token_sets: Vec<Token> = Vec::new();
	let mut tokens: Vec<Token> = Vec::new();

	token_sets.push(Token{token_type: TokenType::Symbol, literal: "("});
	token_sets.push(Token{token_type: TokenType::Symbol, literal: ")"});
	token_sets.push(Token{token_type: TokenType::Symbol, literal: "{"});
	token_sets.push(Token{token_type: TokenType::Symbol, literal: "}"});
	token_sets.push(Token{token_type: TokenType::Symbol, literal: ";"});
	token_sets.push(Token{token_type: TokenType::DataType, literal: "i8"});
	token_sets.push(Token{token_type: TokenType::DataType, literal: "i16"});
	token_sets.push(Token{token_type: TokenType::DataType, literal: "i32"});
	token_sets.push(Token{token_type: TokenType::DataType, literal: "i64"});
	token_sets.push(Token{token_type: TokenType::DataType, literal: "str"});
	token_sets.push(Token{token_type: TokenType::Keyword, literal: "return"});

	let mut i: usize = 0;
	let mut i_2: usize = 0;

	while i < source_code.len().try_into().expect("Failed to convert source code len from usize to i32.") {
		let mut current_byte: Vec<u8> = Vec::new();
		current_byte.push(source_code.as_bytes()[i]);
		let current_char = str::from_utf8(&current_byte).expect("Failed to convert byte to string.");

		println!("{}", current_char);

		while i_2 < token_sets.len()
		{
			if token_sets[i_2].literal == current_char
			{
				tokens.push(token_sets[i_2]);
			}

			i_2 += 1;
		}

		i_2 = 0;
		i += 1;
	}

	while i_2 < token_sets.len()
	{
		println!("{:?} {}", tokens[i_2].token_type, tokens[i_2].literal);

		i_2 += 1;
	}

	return tokens;
}
