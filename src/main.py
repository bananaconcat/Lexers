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

TOKENS = {
	0: "TOKEN_ILLEGAL",
	1: "TOKEN_IDENT",
	2: "TOKEN_L_PAREN",
	3: "TOKEN_R_PAREN",
	4: "TOKEN_L_SQUIRLY",
	5: "TOKEN_R_SQUIRLY",
	6: "TOKEN_INT",
	7: "TOKEN_EQUAL",
	8: "TOKEN_SEMICOLON",
	9: "TOKEN_MULT",
	10: "TOKEN_MINUS",
	11: "TOKEN_DIVIDE",
	12: "TOKEN_PLUS",
	13: "TOKEN_COMMA",
	14: "TOKEN_DOT",
	15: "TOKEN_BANG",
	16: "TOKEN_EQUAL_EQUAL",
	17: "TOKEN_BANG_EQUAL",
	18: "TOKEN_LESS",
	19: "TOKEN_LESS_EQUAL",
	20: "TOKEN_GREATER",
	21: "TOKEN_GREATER_EQUAL",
	22: "TOKEN_AND",
	23: "TOKEN_STRING"
}

MAX_LEN = 256

class Token:
	def __init__(self, _type, _literal):
		self.type = _type
		self.literal = _literal

	def __str__(self):
		return TOKENS.get(self.type)

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
			nc = 0

			if (i + 1) < self.sourceLength:
				nc = self.source[i + 1]

			if c == "(":
				self.tokens.append(Token(TOKEN_L_PAREN, None))
			elif c == ")":
				self.tokens.append(Token(TOKEN_R_PAREN, None))
			elif c == "{":
				self.tokens.append(Token(TOKEN_L_SQUIRLY, None))
			elif c == "}":
				self.tokens.append(Token(TOKEN_R_SQUIRLY, None))
			elif c == "=" and nc == "=":
				self.tokens.append(Token(TOKEN_EQUAL_EQUAL, None))
				i += 1
			elif c == "=":
				self.tokens.append(Token(TOKEN_EQUAL, None))
			elif c == ";":
				self.tokens.append(Token(TOKEN_SEMICOLON, None))
			elif c == "+":
				self.tokens.append(Token(TOKEN_PLUS, None))
			elif c == "-":
				self.tokens.append(Token(TOKEN_MINUS, None))
			elif c == "*":
				self.tokens.append(Token(TOKEN_MULT, None))
			elif c == "/":
				self.tokens.append(Token(TOKEN_DIVIDE, None))
			elif c == ",":
				self.tokens.append(Token(TOKEN_COMMA, None))
			elif c == ".":
				self.tokens.append(Token(TOKEN_DOT, None))
			elif c == "!":
				self.tokens.append(Token(TOKEN_BANG, None))
			elif c == "!" and nc == "=":
				self.tokens.append(Token(TOKEN_BANG_EQUAL, None))
				i += 1
			elif c == "<":
				self.tokens.append(Token(TOKEN_LESS, None))
				i += 1
			elif c == "<" and nc == "=":
				self.tokens.append(Token(TOKEN_LESS_EQUAL, None))
				i += 1
			elif c == ">":
				self.tokens.append(Token(TOKEN_GREATER, None))
				i += 1
			elif c == ">" and nc == "=":
				self.tokens.append(Token(TOKEN_GREATER_EQUAL, None))
				i += 1
			elif c == "&" and nc == "&":
				self.tokens.append(Token(TOKEN_AND, None))
				i += 1
			elif c == "\n":
				pass
			elif c == "\t":
				pass
			elif c == " ":
				pass
			elif c == "\"":
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
			else:
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
	print(f"Type: {token.__str__()}, Literal: {token.literal}")
