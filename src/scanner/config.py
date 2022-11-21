START = 'START'
ERROR = 'ERROR'
NUMBER = 'NUM'
SYMBOL = 'SYMBOL'
KEYWORD = 'KEYWORD'
ID = 'ID'
COMMENT = 'COMMENT'
WHITESPACE = 'WHITESPACE'
EOF = 'EOF'

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
valid_chars = letters + digits + all_symbols + whitespace + ['']
invalid_chars = [chr(i) for i in range(256) if chr(i) not in valid_chars]
