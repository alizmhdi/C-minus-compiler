START = 'start'
NUMBER = 'number'
SYMBOL = 'symbol'
KEYWORD = 'keyword'
ID = 'id'
COMMENT = 'comment'
WHITESPACE = 'whitespace'

letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
digits = [chr(i) for i in range(48, 58)]
symbol = [';', ':', ',', '[', ']', '(', ')', '{', '}', '+', '-', '*', '=', '<', '/']
whitespace = [' ', '\n', '\r', '\t', '\v', '\f']
keywords = ['if', 'else', 'void', 'int', 'while', "break", 'switch', 'default', 'case', 'return', 'endif']
valid_chars = letters + digits + symbol + whitespace
