START = 'start'
ERROR = 'error'
NUMBER = 'number'
SYMBOL = 'symbol'
KEYWORD = 'keyword'
ID = 'id'
COMMENT = 'comment'
WHITESPACE = 'whitespace'

letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
digits = [chr(i) for i in range(48, 58)]
symbol = [';', ':', ',', '[', ']', '(', ')', '{', '}', '+', '-', '<']
equal_symbol = ['=']
slash_symbol = ['/']
star_symbol = ['*']
all_symbols = symbol + equal_symbol + slash_symbol + star_symbol
new_line = ['\n']
whitespace = [' ', '\n', '\r', '\t', '\v', '\f']
keywords = ['if', 'else', 'void', 'int', 'while', "break", 'switch', 'default', 'case', 'return', 'endif']
valid_chars = letters + digits + symbol + whitespace
