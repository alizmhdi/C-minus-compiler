%token NUM
%token ID
%start program
%%
program: declaration_list
;
declaration_list: declaration_list declaration
| declaration
;
declaration: var_declaration
| fun_declaration
;
var_declaration: type_specifier PID ID VAR_DEC ';'
| type_specifier PID ID '[' PSIZE NUM ']' ARRAY_DEC ';'
;
type_specifier: PTYPE "int"
| "void"
;
fun_declaration: type_specifier PID ID FUNC '(' params ')' compound_stmt
;
params: param_list
| "void"
;
param_list: param_list ',' param
| param
;
param: type_specifier PID ID
| type_specifier PID ID '[' ']'
;
compound_stmt: '{' local_declarations statement_list '}'
;
local_declarations: local_declarations var_declaration
| /* epsilon */
;
statement_list: statement_list statement
| /* epsilon */
;
statement: expression_stmt
| compound_stmt
| selection_stmt
| iteration_stmt
| return_stmt
| switch_stmt
;
expression_stmt: expression ';'
| "break" BREAK_JP ';'
| ';'
;
selection_stmt: "if" '(' expression ')' SAVE statement "endif"
| "if" '(' expression ')' SAVE statement JPF_SAVE "else" statement "endif"
;
iteration_stmt: "while" LABEL_WHILE '(' expression ')' SAVE statement
;
return_stmt: "return" ';'
| "return" expression ';'
;
switch_stmt: "switch" LABEL_SWITCH '(' expression ')' '{' case_stmts default_stmt '}'
;
case_stmts: case_stmts case_stmt
| /* epsilon */
;
case_stmt: "case" PNUM NUM SAVE SAVE ':' statement_list
;
default_stmt: SAVE "default" ':' statement_list
| /* epsilon */
;
expression: var '=' expression
| simple_expression
;
var: PID ID
| PID ID '[' expression ']'
;
simple_expression: additive_expression relop additive_expression
| additive_expression
;
relop: P_OP '<'
| P_OP "=="
;
additive_expression: additive_expression addop term
| term
;
addop: P_OP '+'
| P_OP '-'
;
term: term mulop factor
| factor
;
mulop: P_OP '*'
| P_OP '/'
;
factor: '(' expression ')'
| var
| call
| PNUM NUM
| call_output
;
call: PID ID '(' args ')'
;
args: arg_list
| /* epsilon */
;
arg_list: arg_list ',' expression
| expression
;
PID: /* epsilon */
;
PTYPE: /* epsilon */
;
PNUM: /* epsilon */
;
P_OP: /* epsilon */
;
BREAK_JP: /* epsilon */
;
SAVE: /* epsilon */
;
JPF_SAVE: /* epsilon */
;
FUNC: /* epsilon */
;
VAR_DEC: /* epsilon */
;
ARRAY_DEC: /* epsilon */
;
LABEL_WHILE: /* epsilon */
;
LABEL_SWITCH: /* epsilon */
;
call_output: "output" '(' args ')'
;
PSIZE: /* epsilon */
;
%%
