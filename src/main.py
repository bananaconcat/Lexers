TOKEN_ILLEGAL = 0
TOKEN_IDENT = 1
TOKEN_L_PAREN = 2
TOKEN_R_PAREN = 3
TOKEN_L_SQUIRLY = 4
TOKEN_R_SQUIRLY = 5
TOKEN_INT = 6
TOKEN_EQUAL = 7
TOKEN_SEMICOLON = 8
TOKEN_MULT = 9
TOKEN_MINUS = 10
TOKEN_DIVIDE = 11
TOKEN_PLUS = 12

TOKEN_COMMA = 13
TOKEN_DOT = 14
TOKEN_BANG = 15
TOKEN_EQUAL_EQUAL = 16
TOKEN_BANG_EQUAL = 17
TOKEN_LESS = 18
TOKEN_LESS_EQUAL = 19
TOKEN_GREATER = 20
TOKEN_GREATER_EQUAL = 21
TOKEN_AND = 22
TOKEN_STRING = 23

MAX_LEN = 256

class Token:
	def __init__(self, _type, _literal):
		self.type = _type
		self.literal = _literal

class Lexer:
	def __init__(self):
		self.tokens = []
		self.source = ""
		self.sourceLength = 0

		with open("main.junk", "r") as sf:
			self.source = sf.read()
			self.sourceLength = len(self.source)

		i = 0

		while i < self.sourceLength:
			c = self.source[i]

			match c:
				case "(":
					self.tokens.append(Token(TOKEN_L_PAREN, None))
				case ")":
					self.tokens.append(Token(TOKEN_R_PAREN, None))
				case "{":
					self.tokens.append(Token(TOKEN_L_SQUIRLY, None))
				case "}":
					self.tokens.append(Token(TOKEN_R_SQUIRLY, None))
				case "=":
					self.tokens.append(Token(TOKEN_EQUAL, None))
				case ";":
					self.tokens.append(Token(TOKEN_SEMICOLON, None))
				case "+":
					self.tokens.append(Token(TOKEN_PLUS, None))
				case "-":
					self.tokens.append(Token(TOKEN_MINUS, None))
				case "*":
					self.tokens.append(Token(TOKEN_MULT, None))
				case "/":
					self.tokens.append(Token(TOKEN_DIVIDE, None))
				case ",":
					self.tokens.append(Token(TOKEN_COMMA, None))
				case ".":
					self.tokens.append(Token(TOKEN_DOT, None))
				case "!":
					self.tokens.append(Token(TOKEN_BANG, None))
				case "==":
					self.tokens.append(Token(TOKEN_EQUAL_EQUAL, None))
				case "!=":
					self.tokens.append(Token(TOKEN_BANG_EQUAL, None))
				case "<":
					self.tokens.append(Token(TOKEN_LESS, None))
				case "<=":
					self.tokens.append(Token(TOKEN_LESS_EQUAL, None))
				case ">":
					self.tokens.append(Token(TOKEN_GREATER, None))
				case ">=":
					self.tokens.append(Token(TOKEN_GREATER_EQUAL, None))
				case "&&":
					self.tokens.append(Token(TOKEN_AND, None))
				case "\n":
					pass
				case "\t":
					pass
				case " ":
					pass
				case "\"":
					start = i + 1
					i += 1
					stringLit = ""

					while i < self.sourceLength and self.source[i] != "\"":
						stringLit += self.source[i]
						i += 1

					if i < self.sourceLength and self.source[i]== "\"":
						self.tokens.append(Token(TOKEN_STRING, stringLit))
					else:
						self.tokens.append(Token(TOKEN_ILLEGAL, None))
				case _:
					if c.isalpha():
						start = i

						while i < self.sourceLength and (self.source[i].isalpha() or self.source[i].isdigit()) and i - start < MAX_LEN:
							i += 1

						self.tokens.append(Token(TOKEN_IDENT, self.source[start:i]))
						continue
					elif c.isdigit():
						start = i

						while i < self.sourceLength and self.source[i].isdigit() and i - start < MAX_LEN:
							i += 1

						self.tokens.append(Token(TOKEN_INT, self.source[start:i]))
						continue
					else:
						self.tokens.append(Token(TOKEN_ILLEGAL, None))

			i += 1
	
	def addToken(self, tokenType: str, tokenValue: str):
		self.tokens.append(Token(tokenType, tokenValue))

lexer = Lexer()
for token in lexer.tokens:
	print(f"Type: {token.type}, Literal: {token.literal}")
