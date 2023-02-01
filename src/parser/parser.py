import code_generator.program_block
from scanner.config import *
from scanner.scanner import Scanner
from anytree import Node, RenderTree
from writer.syntax_error_writer import SyntaxErrorWriter
from writer.parse_tree_writer import ParseTreeWriter
from code_generator.code_gen import CodeGenerator

grammar = {
    "terminals": [
        "$",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        "/",
        ":",
        ";",
        "<",
        "=",
        "[",
        "]",
        "{",
        "}",
        "NUM",
        "ID",
        "int",
        "void",
        "break",
        "if",
        "endif",
        "else",
        "while",
        "return",
        "switch",
        "case",
        "default",
        "=="
    ],
    "non_terminals": [
        "$accept",
        "program",
        "declaration_list",
        "declaration",
        "var_declaration",
        "type_specifier",
        "fun_declaration",
        "params",
        "param_list",
        "param",
        "compound_stmt",
        "local_declarations",
        "statement_list",
        "statement",
        "expression_stmt",
        "selection_stmt",
        "iteration_stmt",
        "return_stmt",
        "switch_stmt",
        "case_stmts",
        "case_stmt",
        "default_stmt",
        "expression",
        "var",
        "simple_expression",
        "relop",
        "additive_expression",
        "addop",
        "term",
        "mulop",
        "factor",
        "call",
        "args",
        "arg_list",
        "PID",
        "PTYPE",
        "PNUM",
        "P_OP",
        "BREAK_JP",
        "SAVE",
        "JPF_SAVE",
        "FUNC",
        "VAR_DEC",
        "ARRAY_DEC",
        "LABEL_WHILE",
        "LABEL_SWITCH"
    ],
    "first": {
        "$accept": [
            "int",
            "void"
        ],
        "program": [
            "int",
            "void"
        ],
        "declaration_list": [
            "int",
            "void"
        ],
        "declaration": [
            "int",
            "void"
        ],
        "var_declaration": [
            "int",
            "void"
        ],
        "type_specifier": [
            "int",
            "void"
        ],
        "fun_declaration": [
            "int",
            "void"
        ],
        "params": [
            "int",
            "void"
        ],
        "param_list": [
            "int",
            "void"
        ],
        "param": [
            "int",
            "void"
        ],
        "compound_stmt": [
            "{"
        ],
        "local_declarations": [
            "int",
            "void"
        ],
        "statement_list": [
            "if",
            "return",
            "switch",
            "NUM",
            "ID",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "statement": [
            "if",
            "return",
            "switch",
            "NUM",
            "ID",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "expression_stmt": [
            "break",
            "(",
            ";",
            "NUM",
            "ID"
        ],
        "selection_stmt": [
            "if"
        ],
        "iteration_stmt": [
            "while"
        ],
        "return_stmt": [
            "return"
        ],
        "switch_stmt": [
            "switch"
        ],
        "case_stmts": [
            "case"
        ],
        "case_stmt": [
            "case"
        ],
        "default_stmt": [
            "default"
        ],
        "expression": [
            "ID",
            "NUM",
            "("
        ],
        "var": [
            "ID"
        ],
        "simple_expression": [
            "(",
            "NUM",
            "ID"
        ],
        "relop": [
            "<",
            "=="
        ],
        "additive_expression": [
            "(",
            "NUM",
            "ID"
        ],
        "addop": [
            "-",
            "+"
        ],
        "term": [
            "(",
            "NUM",
            "ID"
        ],
        "mulop": [
            "/",
            "*"
        ],
        "factor": [
            "ID",
            "NUM",
            "("
        ],
        "call": [
            "ID"
        ],
        "args": [
            "ID",
            "NUM",
            "("
        ],
        "arg_list": [
            "ID",
            "NUM",
            "("
        ],
        "PID": [],
        "PTYPE": [],
        "PNUM": [],
        "P_OP": [],
        "BREAK_JP": [],
        "SAVE": [],
        "JPF_SAVE": [],
        "FUNC": [],
        "VAR_DEC": [],
        "ARRAY_DEC": [],
        "LABEL_WHILE": [],
        "LABEL_SWITCH": [],
        "$": [
            "$"
        ],
        "(": [
            "("
        ],
        ")": [
            ")"
        ],
        "*": [
            "*"
        ],
        "+": [
            "+"
        ],
        ",": [
            ","
        ],
        "-": [
            "-"
        ],
        "/": [
            "/"
        ],
        ":": [
            ":"
        ],
        ";": [
            ";"
        ],
        "<": [
            "<"
        ],
        "=": [
            "="
        ],
        "[": [
            "["
        ],
        "]": [
            "]"
        ],
        "{": [
            "{"
        ],
        "}": [
            "}"
        ],
        "NUM": [
            "NUM"
        ],
        "ID": [
            "ID"
        ],
        "int": [
            "int"
        ],
        "void": [
            "void"
        ],
        "break": [
            "break"
        ],
        "if": [
            "if"
        ],
        "endif": [
            "endif"
        ],
        "else": [
            "else"
        ],
        "while": [
            "while"
        ],
        "return": [
            "return"
        ],
        "switch": [
            "switch"
        ],
        "case": [
            "case"
        ],
        "default": [
            "default"
        ],
        "==": [
            "=="
        ]
    },
    "follow": {
        "$accept": [],
        "program": [
            "$"
        ],
        "declaration_list": [
            "void",
            "int",
            "$"
        ],
        "declaration": [
            "int",
            "$",
            "void"
        ],
        "var_declaration": [
            "if",
            "return",
            "}",
            "int",
            "$",
            "switch",
            "void",
            "NUM",
            "ID",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "type_specifier": [
            "ID"
        ],
        "fun_declaration": [
            "int",
            "$",
            "void"
        ],
        "params": [
            ")"
        ],
        "param_list": [
            ")",
            ","
        ],
        "param": [
            ")",
            ","
        ],
        "compound_stmt": [
            "if",
            "return",
            "else",
            "int",
            "}",
            "$",
            "switch",
            "endif",
            "void",
            "case",
            "ID",
            "NUM",
            "default",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "local_declarations": [
            "if",
            "return",
            "}",
            "int",
            "switch",
            "void",
            "NUM",
            "ID",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "statement_list": [
            "if",
            "return",
            "}",
            "switch",
            "case",
            "ID",
            "NUM",
            "default",
            "break",
            "while",
            ";",
            "{",
            "("
        ],
        "statement": [
            "if",
            "return",
            "else",
            "}",
            "switch",
            "endif",
            "case",
            "ID",
            "NUM",
            "default",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "expression_stmt": [
            "if",
            "return",
            "else",
            "}",
            "switch",
            "endif",
            "case",
            "ID",
            "NUM",
            "default",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "selection_stmt": [
            "if",
            "return",
            "else",
            "}",
            "switch",
            "endif",
            "case",
            "ID",
            "NUM",
            "default",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "iteration_stmt": [
            "if",
            "return",
            "else",
            "}",
            "switch",
            "endif",
            "case",
            "ID",
            "NUM",
            "default",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "return_stmt": [
            "if",
            "return",
            "else",
            "}",
            "switch",
            "endif",
            "case",
            "ID",
            "NUM",
            "default",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "switch_stmt": [
            "if",
            "return",
            "else",
            "}",
            "switch",
            "endif",
            "case",
            "ID",
            "NUM",
            "default",
            "break",
            "while",
            "(",
            "{",
            ";"
        ],
        "case_stmts": [
            "default",
            "}",
            "case"
        ],
        "case_stmt": [
            "default",
            "}",
            "case"
        ],
        "default_stmt": [
            "}"
        ],
        "expression": [
            ")",
            "]",
            ",",
            ";"
        ],
        "var": [
            "-",
            "*",
            ",",
            "+",
            "/",
            "==",
            "=",
            ")",
            "<",
            "]",
            ";"
        ],
        "simple_expression": [
            ")",
            "]",
            ",",
            ";"
        ],
        "relop": [
            "(",
            "NUM",
            "ID"
        ],
        "additive_expression": [
            "-",
            ",",
            "==",
            ")",
            "<",
            "]",
            ";",
            "+"
        ],
        "addop": [
            "(",
            "NUM",
            "ID"
        ],
        "term": [
            "-",
            "/",
            "*",
            ",",
            "==",
            ")",
            "<",
            "]",
            ";",
            "+"
        ],
        "mulop": [
            "(",
            "NUM",
            "ID"
        ],
        "factor": [
            "-",
            "/",
            "*",
            ",",
            "==",
            ")",
            "<",
            "]",
            ";",
            "+"
        ],
        "call": [
            "-",
            "/",
            "*",
            ",",
            "==",
            ")",
            "<",
            "]",
            ";",
            "+"
        ],
        "args": [
            ")"
        ],
        "arg_list": [
            ")",
            ","
        ],
        "PID": [
            "ID"
        ],
        "PTYPE": [
            "int"
        ],
        "PNUM": [
            "NUM"
        ],
        "P_OP": [
            "<",
            "-",
            "/",
            "*",
            "==",
            "+"
        ],
        "BREAK_JP": [
            ";"
        ],
        "SAVE": [
            "if",
            "return",
            "switch",
            "NUM",
            "ID",
            ":",
            "break",
            "while",
            ";",
            "{",
            "("
        ],
        "JPF_SAVE": [
            "else"
        ],
        "FUNC": [
            "("
        ],
        "VAR_DEC": [
            ";"
        ],
        "ARRAY_DEC": [
            ";"
        ],
        "LABEL_WHILE": [
            "("
        ],
        "LABEL_SWITCH": [
            "("
        ]
    },
    "grammar": {
        "0": [
            "$accept",
            "->",
            "program",
            "$"
        ],
        "1": [
            "program",
            "->",
            "declaration_list"
        ],
        "2": [
            "declaration_list",
            "->",
            "declaration_list",
            "declaration"
        ],
        "3": [
            "declaration_list",
            "->",
            "declaration"
        ],
        "4": [
            "declaration",
            "->",
            "var_declaration"
        ],
        "5": [
            "declaration",
            "->",
            "fun_declaration"
        ],
        "6": [
            "var_declaration",
            "->",
            "type_specifier",
            "PID",
            "ID",
            "VAR_DEC",
            ";"
        ],
        "7": [
            "var_declaration",
            "->",
            "type_specifier",
            "PID",
            "ID",
            "[",
            "PNUM",
            "NUM",
            "]",
            "ARRAY_DEC",
            ";"
        ],
        "8": [
            "type_specifier",
            "->",
            "PTYPE",
            "int"
        ],
        "9": [
            "type_specifier",
            "->",
            "void"
        ],
        "10": [
            "fun_declaration",
            "->",
            "type_specifier",
            "PID",
            "ID",
            "FUNC",
            "(",
            "params",
            ")",
            "compound_stmt"
        ],
        "11": [
            "params",
            "->",
            "param_list"
        ],
        "12": [
            "params",
            "->",
            "void"
        ],
        "13": [
            "param_list",
            "->",
            "param_list",
            ",",
            "param"
        ],
        "14": [
            "param_list",
            "->",
            "param"
        ],
        "15": [
            "param",
            "->",
            "type_specifier",
            "PID",
            "ID"
        ],
        "16": [
            "param",
            "->",
            "type_specifier",
            "PID",
            "ID",
            "[",
            "]"
        ],
        "17": [
            "compound_stmt",
            "->",
            "{",
            "local_declarations",
            "statement_list",
            "}"
        ],
        "18": [
            "local_declarations",
            "->",
            "local_declarations",
            "var_declaration"
        ],
        "19": [
            "local_declarations",
            "->",
            "epsilon"
        ],
        "20": [
            "statement_list",
            "->",
            "statement_list",
            "statement"
        ],
        "21": [
            "statement_list",
            "->",
            "epsilon"
        ],
        "22": [
            "statement",
            "->",
            "expression_stmt"
        ],
        "23": [
            "statement",
            "->",
            "compound_stmt"
        ],
        "24": [
            "statement",
            "->",
            "selection_stmt"
        ],
        "25": [
            "statement",
            "->",
            "iteration_stmt"
        ],
        "26": [
            "statement",
            "->",
            "return_stmt"
        ],
        "27": [
            "statement",
            "->",
            "switch_stmt"
        ],
        "28": [
            "expression_stmt",
            "->",
            "expression",
            ";"
        ],
        "29": [
            "expression_stmt",
            "->",
            "break",
            "BREAK_JP",
            ";"
        ],
        "30": [
            "expression_stmt",
            "->",
            ";"
        ],
        "31": [
            "selection_stmt",
            "->",
            "if",
            "(",
            "expression",
            ")",
            "SAVE",
            "statement",
            "endif"
        ],
        "32": [
            "selection_stmt",
            "->",
            "if",
            "(",
            "expression",
            ")",
            "SAVE",
            "statement",
            "JPF_SAVE",
            "else",
            "statement",
            "endif"
        ],
        "33": [
            "iteration_stmt",
            "->",
            "while",
            "LABEL_WHILE",
            "(",
            "expression",
            ")",
            "SAVE",
            "statement"
        ],
        "34": [
            "return_stmt",
            "->",
            "return",
            ";"
        ],
        "35": [
            "return_stmt",
            "->",
            "return",
            "expression",
            ";"
        ],
        "36": [
            "switch_stmt",
            "->",
            "switch",
            "LABEL_SWITCH",
            "(",
            "expression",
            ")",
            "{",
            "case_stmts",
            "default_stmt",
            "}"
        ],
        "37": [
            "case_stmts",
            "->",
            "case_stmts",
            "case_stmt"
        ],
        "38": [
            "case_stmts",
            "->",
            "epsilon"
        ],
        "39": [
            "case_stmt",
            "->",
            "case",
            "PNUM",
            "NUM",
            "SAVE",
            ":",
            "statement_list"
        ],
        "40": [
            "default_stmt",
            "->",
            "default",
            ":",
            "statement_list"
        ],
        "41": [
            "default_stmt",
            "->",
            "epsilon"
        ],
        "42": [
            "expression",
            "->",
            "var",
            "=",
            "expression"
        ],
        "43": [
            "expression",
            "->",
            "simple_expression"
        ],
        "44": [
            "var",
            "->",
            "PID",
            "ID"
        ],
        "45": [
            "var",
            "->",
            "PID",
            "ID",
            "[",
            "expression",
            "]"
        ],
        "46": [
            "simple_expression",
            "->",
            "additive_expression",
            "relop",
            "additive_expression"
        ],
        "47": [
            "simple_expression",
            "->",
            "additive_expression"
        ],
        "48": [
            "relop",
            "->",
            "P_OP",
            "<"
        ],
        "49": [
            "relop",
            "->",
            "P_OP",
            "=="
        ],
        "50": [
            "additive_expression",
            "->",
            "additive_expression",
            "addop",
            "term"
        ],
        "51": [
            "additive_expression",
            "->",
            "term"
        ],
        "52": [
            "addop",
            "->",
            "P_OP",
            "+"
        ],
        "53": [
            "addop",
            "->",
            "P_OP",
            "-"
        ],
        "54": [
            "term",
            "->",
            "term",
            "mulop",
            "factor"
        ],
        "55": [
            "term",
            "->",
            "factor"
        ],
        "56": [
            "mulop",
            "->",
            "P_OP",
            "*"
        ],
        "57": [
            "mulop",
            "->",
            "P_OP",
            "/"
        ],
        "58": [
            "factor",
            "->",
            "(",
            "expression",
            ")"
        ],
        "59": [
            "factor",
            "->",
            "var"
        ],
        "60": [
            "factor",
            "->",
            "call"
        ],
        "61": [
            "factor",
            "->",
            "PNUM",
            "NUM"
        ],
        "62": [
            "call",
            "->",
            "PID",
            "ID",
            "(",
            "args",
            ")"
        ],
        "63": [
            "args",
            "->",
            "arg_list"
        ],
        "64": [
            "args",
            "->",
            "epsilon"
        ],
        "65": [
            "arg_list",
            "->",
            "arg_list",
            ",",
            "expression"
        ],
        "66": [
            "arg_list",
            "->",
            "expression"
        ],
        "67": [
            "PID",
            "->",
            "epsilon"
        ],
        "68": [
            "PTYPE",
            "->",
            "epsilon"
        ],
        "69": [
            "PNUM",
            "->",
            "epsilon"
        ],
        "70": [
            "P_OP",
            "->",
            "epsilon"
        ],
        "71": [
            "BREAK_JP",
            "->",
            "epsilon"
        ],
        "72": [
            "SAVE",
            "->",
            "epsilon"
        ],
        "73": [
            "JPF_SAVE",
            "->",
            "epsilon"
        ],
        "74": [
            "FUNC",
            "->",
            "epsilon"
        ],
        "75": [
            "VAR_DEC",
            "->",
            "epsilon"
        ],
        "76": [
            "ARRAY_DEC",
            "->",
            "epsilon"
        ],
        "77": [
            "LABEL_WHILE",
            "->",
            "epsilon"
        ],
        "78": [
            "LABEL_SWITCH",
            "->",
            "epsilon"
        ]
    },
    "parse_table": {
        "0": {
            "void": "shift_1",
            "program": "goto_2",
            "declaration_list": "goto_3",
            "declaration": "goto_4",
            "var_declaration": "goto_5",
            "type_specifier": "goto_6",
            "fun_declaration": "goto_7",
            "PTYPE": "goto_8",
            "int": "reduce_68"
        },
        "1": {
            "ID": "reduce_9"
        },
        "2": {
            "$": "shift_9"
        },
        "3": {
            "void": "shift_1",
            "declaration": "goto_10",
            "var_declaration": "goto_5",
            "type_specifier": "goto_6",
            "fun_declaration": "goto_7",
            "PTYPE": "goto_8",
            "int": "reduce_68",
            "$": "reduce_1"
        },
        "4": {
            "void": "reduce_3",
            "int": "reduce_3",
            "$": "reduce_3"
        },
        "5": {
            "int": "reduce_4",
            "$": "reduce_4",
            "void": "reduce_4"
        },
        "6": {
            "PID": "goto_11",
            "ID": "reduce_67"
        },
        "7": {
            "int": "reduce_5",
            "$": "reduce_5",
            "void": "reduce_5"
        },
        "8": {
            "int": "shift_12"
        },
        "9": {
            "$": "accept"
        },
        "10": {
            "void": "reduce_2",
            "int": "reduce_2",
            "$": "reduce_2"
        },
        "11": {
            "ID": "shift_13"
        },
        "12": {
            "ID": "reduce_8"
        },
        "13": {
            "[": "shift_14",
            "FUNC": "goto_15",
            "VAR_DEC": "goto_16",
            ";": "reduce_75",
            "(": "reduce_74"
        },
        "14": {
            "PNUM": "goto_17",
            "NUM": "reduce_69"
        },
        "15": {
            "(": "shift_18"
        },
        "16": {
            ";": "shift_19"
        },
        "17": {
            "NUM": "shift_20"
        },
        "18": {
            "void": "shift_21",
            "type_specifier": "goto_22",
            "params": "goto_23",
            "param_list": "goto_24",
            "param": "goto_25",
            "PTYPE": "goto_8",
            "int": "reduce_68"
        },
        "19": {
            "if": "reduce_6",
            "return": "reduce_6",
            "}": "reduce_6",
            "int": "reduce_6",
            "$": "reduce_6",
            "switch": "reduce_6",
            "void": "reduce_6",
            "NUM": "reduce_6",
            "ID": "reduce_6",
            "break": "reduce_6",
            "while": "reduce_6",
            "(": "reduce_6",
            "{": "reduce_6",
            ";": "reduce_6"
        },
        "20": {
            "]": "shift_26"
        },
        "21": {
            ")": "reduce_12",
            "ID": "reduce_9"
        },
        "22": {
            "PID": "goto_27",
            "ID": "reduce_67"
        },
        "23": {
            ")": "shift_28"
        },
        "24": {
            ",": "shift_29",
            ")": "reduce_11"
        },
        "25": {
            ")": "reduce_14",
            ",": "reduce_14"
        },
        "26": {
            "ARRAY_DEC": "goto_30",
            ";": "reduce_76"
        },
        "27": {
            "ID": "shift_31"
        },
        "28": {
            "{": "shift_32",
            "compound_stmt": "goto_33"
        },
        "29": {
            "void": "shift_1",
            "type_specifier": "goto_22",
            "param": "goto_34",
            "PTYPE": "goto_8",
            "int": "reduce_68"
        },
        "30": {
            ";": "shift_35"
        },
        "31": {
            "[": "shift_36",
            ")": "reduce_15",
            ",": "reduce_15"
        },
        "32": {
            "local_declarations": "goto_37",
            "if": "reduce_19",
            "return": "reduce_19",
            "}": "reduce_19",
            "int": "reduce_19",
            "switch": "reduce_19",
            "void": "reduce_19",
            "NUM": "reduce_19",
            "ID": "reduce_19",
            "break": "reduce_19",
            "while": "reduce_19",
            "(": "reduce_19",
            "{": "reduce_19",
            ";": "reduce_19"
        },
        "33": {
            "int": "reduce_10",
            "$": "reduce_10",
            "void": "reduce_10"
        },
        "34": {
            ")": "reduce_13",
            ",": "reduce_13"
        },
        "35": {
            "if": "reduce_7",
            "return": "reduce_7",
            "}": "reduce_7",
            "int": "reduce_7",
            "$": "reduce_7",
            "switch": "reduce_7",
            "void": "reduce_7",
            "NUM": "reduce_7",
            "ID": "reduce_7",
            "break": "reduce_7",
            "while": "reduce_7",
            "(": "reduce_7",
            "{": "reduce_7",
            ";": "reduce_7"
        },
        "36": {
            "]": "shift_38"
        },
        "37": {
            "void": "shift_1",
            "var_declaration": "goto_39",
            "type_specifier": "goto_40",
            "statement_list": "goto_41",
            "PTYPE": "goto_8",
            "int": "reduce_68",
            "if": "reduce_21",
            "return": "reduce_21",
            "}": "reduce_21",
            "switch": "reduce_21",
            "case": "reduce_21",
            "ID": "reduce_21",
            "NUM": "reduce_21",
            "default": "reduce_21",
            "break": "reduce_21",
            "while": "reduce_21",
            ";": "reduce_21",
            "{": "reduce_21",
            "(": "reduce_21"
        },
        "38": {
            ")": "reduce_16",
            ",": "reduce_16"
        },
        "39": {
            "if": "reduce_18",
            "return": "reduce_18",
            "}": "reduce_18",
            "int": "reduce_18",
            "switch": "reduce_18",
            "void": "reduce_18",
            "NUM": "reduce_18",
            "ID": "reduce_18",
            "break": "reduce_18",
            "while": "reduce_18",
            "(": "reduce_18",
            "{": "reduce_18",
            ";": "reduce_18"
        },
        "40": {
            "PID": "goto_42",
            "ID": "reduce_67"
        },
        "41": {
            ";": "shift_43",
            "(": "shift_44",
            "{": "shift_32",
            "}": "shift_45",
            "break": "shift_46",
            "if": "shift_47",
            "while": "shift_48",
            "return": "shift_49",
            "switch": "shift_50",
            "compound_stmt": "goto_51",
            "statement": "goto_52",
            "expression_stmt": "goto_53",
            "selection_stmt": "goto_54",
            "iteration_stmt": "goto_55",
            "return_stmt": "goto_56",
            "switch_stmt": "goto_57",
            "expression": "goto_58",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "42": {
            "ID": "shift_67"
        },
        "43": {
            "if": "reduce_30",
            "return": "reduce_30",
            "else": "reduce_30",
            "}": "reduce_30",
            "switch": "reduce_30",
            "endif": "reduce_30",
            "case": "reduce_30",
            "ID": "reduce_30",
            "NUM": "reduce_30",
            "default": "reduce_30",
            "break": "reduce_30",
            "while": "reduce_30",
            "(": "reduce_30",
            "{": "reduce_30",
            ";": "reduce_30"
        },
        "44": {
            "(": "shift_44",
            "expression": "goto_68",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "45": {
            "if": "reduce_17",
            "return": "reduce_17",
            "else": "reduce_17",
            "int": "reduce_17",
            "}": "reduce_17",
            "$": "reduce_17",
            "switch": "reduce_17",
            "endif": "reduce_17",
            "void": "reduce_17",
            "case": "reduce_17",
            "ID": "reduce_17",
            "NUM": "reduce_17",
            "default": "reduce_17",
            "break": "reduce_17",
            "while": "reduce_17",
            "(": "reduce_17",
            "{": "reduce_17",
            ";": "reduce_17"
        },
        "46": {
            "BREAK_JP": "goto_69",
            ";": "reduce_71"
        },
        "47": {
            "(": "shift_70"
        },
        "48": {
            "LABEL_WHILE": "goto_71",
            "(": "reduce_77"
        },
        "49": {
            ";": "shift_72",
            "(": "shift_44",
            "expression": "goto_73",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "50": {
            "LABEL_SWITCH": "goto_74",
            "(": "reduce_78"
        },
        "51": {
            "if": "reduce_23",
            "return": "reduce_23",
            "else": "reduce_23",
            "}": "reduce_23",
            "switch": "reduce_23",
            "endif": "reduce_23",
            "case": "reduce_23",
            "ID": "reduce_23",
            "NUM": "reduce_23",
            "default": "reduce_23",
            "break": "reduce_23",
            "while": "reduce_23",
            "(": "reduce_23",
            "{": "reduce_23",
            ";": "reduce_23"
        },
        "52": {
            "if": "reduce_20",
            "return": "reduce_20",
            "}": "reduce_20",
            "switch": "reduce_20",
            "case": "reduce_20",
            "ID": "reduce_20",
            "NUM": "reduce_20",
            "default": "reduce_20",
            "break": "reduce_20",
            "while": "reduce_20",
            ";": "reduce_20",
            "{": "reduce_20",
            "(": "reduce_20"
        },
        "53": {
            "if": "reduce_22",
            "return": "reduce_22",
            "else": "reduce_22",
            "}": "reduce_22",
            "switch": "reduce_22",
            "endif": "reduce_22",
            "case": "reduce_22",
            "ID": "reduce_22",
            "NUM": "reduce_22",
            "default": "reduce_22",
            "break": "reduce_22",
            "while": "reduce_22",
            "(": "reduce_22",
            "{": "reduce_22",
            ";": "reduce_22"
        },
        "54": {
            "if": "reduce_24",
            "return": "reduce_24",
            "else": "reduce_24",
            "}": "reduce_24",
            "switch": "reduce_24",
            "endif": "reduce_24",
            "case": "reduce_24",
            "ID": "reduce_24",
            "NUM": "reduce_24",
            "default": "reduce_24",
            "break": "reduce_24",
            "while": "reduce_24",
            "(": "reduce_24",
            "{": "reduce_24",
            ";": "reduce_24"
        },
        "55": {
            "if": "reduce_25",
            "return": "reduce_25",
            "else": "reduce_25",
            "}": "reduce_25",
            "switch": "reduce_25",
            "endif": "reduce_25",
            "case": "reduce_25",
            "ID": "reduce_25",
            "NUM": "reduce_25",
            "default": "reduce_25",
            "break": "reduce_25",
            "while": "reduce_25",
            "(": "reduce_25",
            "{": "reduce_25",
            ";": "reduce_25"
        },
        "56": {
            "if": "reduce_26",
            "return": "reduce_26",
            "else": "reduce_26",
            "}": "reduce_26",
            "switch": "reduce_26",
            "endif": "reduce_26",
            "case": "reduce_26",
            "ID": "reduce_26",
            "NUM": "reduce_26",
            "default": "reduce_26",
            "break": "reduce_26",
            "while": "reduce_26",
            "(": "reduce_26",
            "{": "reduce_26",
            ";": "reduce_26"
        },
        "57": {
            "if": "reduce_27",
            "return": "reduce_27",
            "else": "reduce_27",
            "}": "reduce_27",
            "switch": "reduce_27",
            "endif": "reduce_27",
            "case": "reduce_27",
            "ID": "reduce_27",
            "NUM": "reduce_27",
            "default": "reduce_27",
            "break": "reduce_27",
            "while": "reduce_27",
            "(": "reduce_27",
            "{": "reduce_27",
            ";": "reduce_27"
        },
        "58": {
            ";": "shift_75"
        },
        "59": {
            "=": "shift_76",
            "-": "reduce_59",
            "/": "reduce_59",
            "*": "reduce_59",
            ",": "reduce_59",
            "==": "reduce_59",
            ")": "reduce_59",
            "<": "reduce_59",
            "]": "reduce_59",
            ";": "reduce_59",
            "+": "reduce_59"
        },
        "60": {
            ")": "reduce_43",
            "]": "reduce_43",
            ",": "reduce_43",
            ";": "reduce_43"
        },
        "61": {
            "relop": "goto_77",
            "addop": "goto_78",
            "P_OP": "goto_79",
            "<": "reduce_70",
            "-": "reduce_70",
            "/": "reduce_70",
            "*": "reduce_70",
            "==": "reduce_70",
            "+": "reduce_70",
            ")": "reduce_47",
            "]": "reduce_47",
            ",": "reduce_47",
            ";": "reduce_47"
        },
        "62": {
            "mulop": "goto_80",
            "P_OP": "goto_81",
            "<": "reduce_51",
            "-": "reduce_51",
            "/": "reduce_70",
            "*": "reduce_70",
            "==": "reduce_51",
            "+": "reduce_51",
            ",": "reduce_51",
            ")": "reduce_51",
            "]": "reduce_51",
            ";": "reduce_51"
        },
        "63": {
            "-": "reduce_55",
            "/": "reduce_55",
            "*": "reduce_55",
            ",": "reduce_55",
            "==": "reduce_55",
            ")": "reduce_55",
            "<": "reduce_55",
            "]": "reduce_55",
            ";": "reduce_55",
            "+": "reduce_55"
        },
        "64": {
            "-": "reduce_60",
            "/": "reduce_60",
            "*": "reduce_60",
            ",": "reduce_60",
            "==": "reduce_60",
            ")": "reduce_60",
            "<": "reduce_60",
            "]": "reduce_60",
            ";": "reduce_60",
            "+": "reduce_60"
        },
        "65": {
            "ID": "shift_82"
        },
        "66": {
            "NUM": "shift_83"
        },
        "67": {
            "[": "shift_14",
            "VAR_DEC": "goto_16",
            ";": "reduce_75"
        },
        "68": {
            ")": "shift_84"
        },
        "69": {
            ";": "shift_85"
        },
        "70": {
            "(": "shift_44",
            "expression": "goto_86",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "71": {
            "(": "shift_87"
        },
        "72": {
            "if": "reduce_34",
            "return": "reduce_34",
            "else": "reduce_34",
            "}": "reduce_34",
            "switch": "reduce_34",
            "endif": "reduce_34",
            "case": "reduce_34",
            "ID": "reduce_34",
            "NUM": "reduce_34",
            "default": "reduce_34",
            "break": "reduce_34",
            "while": "reduce_34",
            "(": "reduce_34",
            "{": "reduce_34",
            ";": "reduce_34"
        },
        "73": {
            ";": "shift_88"
        },
        "74": {
            "(": "shift_89"
        },
        "75": {
            "if": "reduce_28",
            "return": "reduce_28",
            "else": "reduce_28",
            "}": "reduce_28",
            "switch": "reduce_28",
            "endif": "reduce_28",
            "case": "reduce_28",
            "ID": "reduce_28",
            "NUM": "reduce_28",
            "default": "reduce_28",
            "break": "reduce_28",
            "while": "reduce_28",
            "(": "reduce_28",
            "{": "reduce_28",
            ";": "reduce_28"
        },
        "76": {
            "(": "shift_44",
            "expression": "goto_90",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "77": {
            "(": "shift_44",
            "var": "goto_91",
            "additive_expression": "goto_92",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "78": {
            "(": "shift_44",
            "var": "goto_91",
            "term": "goto_93",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "79": {
            "<": "shift_94",
            "==": "shift_95",
            "+": "shift_96",
            "-": "shift_97"
        },
        "80": {
            "(": "shift_44",
            "var": "goto_91",
            "factor": "goto_98",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "81": {
            "*": "shift_99",
            "/": "shift_100"
        },
        "82": {
            "[": "shift_101",
            "(": "shift_102",
            "-": "reduce_44",
            "*": "reduce_44",
            ",": "reduce_44",
            "+": "reduce_44",
            "/": "reduce_44",
            "==": "reduce_44",
            "=": "reduce_44",
            ")": "reduce_44",
            "<": "reduce_44",
            "]": "reduce_44",
            ";": "reduce_44"
        },
        "83": {
            "-": "reduce_61",
            "/": "reduce_61",
            "*": "reduce_61",
            ",": "reduce_61",
            "==": "reduce_61",
            ")": "reduce_61",
            "<": "reduce_61",
            "]": "reduce_61",
            ";": "reduce_61",
            "+": "reduce_61"
        },
        "84": {
            "-": "reduce_58",
            "/": "reduce_58",
            "*": "reduce_58",
            ",": "reduce_58",
            "==": "reduce_58",
            ")": "reduce_58",
            "<": "reduce_58",
            "]": "reduce_58",
            ";": "reduce_58",
            "+": "reduce_58"
        },
        "85": {
            "if": "reduce_29",
            "return": "reduce_29",
            "else": "reduce_29",
            "}": "reduce_29",
            "switch": "reduce_29",
            "endif": "reduce_29",
            "case": "reduce_29",
            "ID": "reduce_29",
            "NUM": "reduce_29",
            "default": "reduce_29",
            "break": "reduce_29",
            "while": "reduce_29",
            "(": "reduce_29",
            "{": "reduce_29",
            ";": "reduce_29"
        },
        "86": {
            ")": "shift_103"
        },
        "87": {
            "(": "shift_44",
            "expression": "goto_104",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "88": {
            "if": "reduce_35",
            "return": "reduce_35",
            "else": "reduce_35",
            "}": "reduce_35",
            "switch": "reduce_35",
            "endif": "reduce_35",
            "case": "reduce_35",
            "ID": "reduce_35",
            "NUM": "reduce_35",
            "default": "reduce_35",
            "break": "reduce_35",
            "while": "reduce_35",
            "(": "reduce_35",
            "{": "reduce_35",
            ";": "reduce_35"
        },
        "89": {
            "(": "shift_44",
            "expression": "goto_105",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "90": {
            ")": "reduce_42",
            "]": "reduce_42",
            ",": "reduce_42",
            ";": "reduce_42"
        },
        "91": {
            "-": "reduce_59",
            "/": "reduce_59",
            "*": "reduce_59",
            ",": "reduce_59",
            "==": "reduce_59",
            ")": "reduce_59",
            "<": "reduce_59",
            "]": "reduce_59",
            ";": "reduce_59",
            "+": "reduce_59"
        },
        "92": {
            "addop": "goto_78",
            "P_OP": "goto_106",
            "<": "reduce_70",
            "-": "reduce_70",
            "/": "reduce_70",
            "*": "reduce_70",
            "==": "reduce_70",
            "+": "reduce_70",
            ")": "reduce_46",
            "]": "reduce_46",
            ",": "reduce_46",
            ";": "reduce_46"
        },
        "93": {
            "mulop": "goto_80",
            "P_OP": "goto_81",
            "<": "reduce_50",
            "-": "reduce_50",
            "/": "reduce_70",
            "*": "reduce_70",
            "==": "reduce_50",
            "+": "reduce_50",
            ",": "reduce_50",
            ")": "reduce_50",
            "]": "reduce_50",
            ";": "reduce_50"
        },
        "94": {
            "(": "reduce_48",
            "NUM": "reduce_48",
            "ID": "reduce_48"
        },
        "95": {
            "(": "reduce_49",
            "NUM": "reduce_49",
            "ID": "reduce_49"
        },
        "96": {
            "(": "reduce_52",
            "NUM": "reduce_52",
            "ID": "reduce_52"
        },
        "97": {
            "(": "reduce_53",
            "NUM": "reduce_53",
            "ID": "reduce_53"
        },
        "98": {
            "-": "reduce_54",
            "/": "reduce_54",
            "*": "reduce_54",
            ",": "reduce_54",
            "==": "reduce_54",
            ")": "reduce_54",
            "<": "reduce_54",
            "]": "reduce_54",
            ";": "reduce_54",
            "+": "reduce_54"
        },
        "99": {
            "(": "reduce_56",
            "NUM": "reduce_56",
            "ID": "reduce_56"
        },
        "100": {
            "(": "reduce_57",
            "NUM": "reduce_57",
            "ID": "reduce_57"
        },
        "101": {
            "(": "shift_44",
            "expression": "goto_107",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "102": {
            "(": "shift_44",
            "expression": "goto_108",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "args": "goto_109",
            "arg_list": "goto_110",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67",
            ")": "reduce_64"
        },
        "103": {
            "SAVE": "goto_111",
            "if": "reduce_72",
            "return": "reduce_72",
            "switch": "reduce_72",
            "NUM": "reduce_72",
            "ID": "reduce_72",
            ":": "reduce_72",
            "break": "reduce_72",
            "while": "reduce_72",
            ";": "reduce_72",
            "{": "reduce_72",
            "(": "reduce_72"
        },
        "104": {
            ")": "shift_112"
        },
        "105": {
            ")": "shift_113"
        },
        "106": {
            "+": "shift_96",
            "-": "shift_97"
        },
        "107": {
            "]": "shift_114"
        },
        "108": {
            ")": "reduce_66",
            ",": "reduce_66"
        },
        "109": {
            ")": "shift_115"
        },
        "110": {
            ",": "shift_116",
            ")": "reduce_63"
        },
        "111": {
            ";": "shift_43",
            "(": "shift_44",
            "{": "shift_32",
            "break": "shift_46",
            "if": "shift_47",
            "while": "shift_48",
            "return": "shift_49",
            "switch": "shift_50",
            "compound_stmt": "goto_51",
            "statement": "goto_117",
            "expression_stmt": "goto_53",
            "selection_stmt": "goto_54",
            "iteration_stmt": "goto_55",
            "return_stmt": "goto_56",
            "switch_stmt": "goto_57",
            "expression": "goto_58",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "112": {
            "SAVE": "goto_118",
            "if": "reduce_72",
            "return": "reduce_72",
            "switch": "reduce_72",
            "NUM": "reduce_72",
            "ID": "reduce_72",
            ":": "reduce_72",
            "break": "reduce_72",
            "while": "reduce_72",
            ";": "reduce_72",
            "{": "reduce_72",
            "(": "reduce_72"
        },
        "113": {
            "{": "shift_119"
        },
        "114": {
            "-": "reduce_45",
            "*": "reduce_45",
            ",": "reduce_45",
            "+": "reduce_45",
            "/": "reduce_45",
            "==": "reduce_45",
            "=": "reduce_45",
            ")": "reduce_45",
            "<": "reduce_45",
            "]": "reduce_45",
            ";": "reduce_45"
        },
        "115": {
            "-": "reduce_62",
            "/": "reduce_62",
            "*": "reduce_62",
            ",": "reduce_62",
            "==": "reduce_62",
            ")": "reduce_62",
            "<": "reduce_62",
            "]": "reduce_62",
            ";": "reduce_62",
            "+": "reduce_62"
        },
        "116": {
            "(": "shift_44",
            "expression": "goto_120",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "117": {
            "endif": "shift_121",
            "JPF_SAVE": "goto_122",
            "else": "reduce_73"
        },
        "118": {
            ";": "shift_43",
            "(": "shift_44",
            "{": "shift_32",
            "break": "shift_46",
            "if": "shift_47",
            "while": "shift_48",
            "return": "shift_49",
            "switch": "shift_50",
            "compound_stmt": "goto_51",
            "statement": "goto_123",
            "expression_stmt": "goto_53",
            "selection_stmt": "goto_54",
            "iteration_stmt": "goto_55",
            "return_stmt": "goto_56",
            "switch_stmt": "goto_57",
            "expression": "goto_58",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "119": {
            "case_stmts": "goto_124",
            "default": "reduce_38",
            "}": "reduce_38",
            "case": "reduce_38"
        },
        "120": {
            ")": "reduce_65",
            ",": "reduce_65"
        },
        "121": {
            "if": "reduce_31",
            "return": "reduce_31",
            "else": "reduce_31",
            "}": "reduce_31",
            "switch": "reduce_31",
            "endif": "reduce_31",
            "case": "reduce_31",
            "ID": "reduce_31",
            "NUM": "reduce_31",
            "default": "reduce_31",
            "break": "reduce_31",
            "while": "reduce_31",
            "(": "reduce_31",
            "{": "reduce_31",
            ";": "reduce_31"
        },
        "122": {
            "else": "shift_125"
        },
        "123": {
            "if": "reduce_33",
            "return": "reduce_33",
            "else": "reduce_33",
            "}": "reduce_33",
            "switch": "reduce_33",
            "endif": "reduce_33",
            "case": "reduce_33",
            "ID": "reduce_33",
            "NUM": "reduce_33",
            "default": "reduce_33",
            "break": "reduce_33",
            "while": "reduce_33",
            "(": "reduce_33",
            "{": "reduce_33",
            ";": "reduce_33"
        },
        "124": {
            "case": "shift_126",
            "default": "shift_127",
            "case_stmt": "goto_128",
            "default_stmt": "goto_129",
            "}": "reduce_41"
        },
        "125": {
            ";": "shift_43",
            "(": "shift_44",
            "{": "shift_32",
            "break": "shift_46",
            "if": "shift_47",
            "while": "shift_48",
            "return": "shift_49",
            "switch": "shift_50",
            "compound_stmt": "goto_51",
            "statement": "goto_130",
            "expression_stmt": "goto_53",
            "selection_stmt": "goto_54",
            "iteration_stmt": "goto_55",
            "return_stmt": "goto_56",
            "switch_stmt": "goto_57",
            "expression": "goto_58",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67"
        },
        "126": {
            "PNUM": "goto_131",
            "NUM": "reduce_69"
        },
        "127": {
            ":": "shift_132"
        },
        "128": {
            "default": "reduce_37",
            "}": "reduce_37",
            "case": "reduce_37"
        },
        "129": {
            "}": "shift_133"
        },
        "130": {
            "endif": "shift_134"
        },
        "131": {
            "NUM": "shift_135"
        },
        "132": {
            "statement_list": "goto_136",
            "if": "reduce_21",
            "return": "reduce_21",
            "}": "reduce_21",
            "switch": "reduce_21",
            "case": "reduce_21",
            "ID": "reduce_21",
            "NUM": "reduce_21",
            "default": "reduce_21",
            "break": "reduce_21",
            "while": "reduce_21",
            ";": "reduce_21",
            "{": "reduce_21",
            "(": "reduce_21"
        },
        "133": {
            "if": "reduce_36",
            "return": "reduce_36",
            "else": "reduce_36",
            "}": "reduce_36",
            "switch": "reduce_36",
            "endif": "reduce_36",
            "case": "reduce_36",
            "ID": "reduce_36",
            "NUM": "reduce_36",
            "default": "reduce_36",
            "break": "reduce_36",
            "while": "reduce_36",
            "(": "reduce_36",
            "{": "reduce_36",
            ";": "reduce_36"
        },
        "134": {
            "if": "reduce_32",
            "return": "reduce_32",
            "else": "reduce_32",
            "}": "reduce_32",
            "switch": "reduce_32",
            "endif": "reduce_32",
            "case": "reduce_32",
            "ID": "reduce_32",
            "NUM": "reduce_32",
            "default": "reduce_32",
            "break": "reduce_32",
            "while": "reduce_32",
            "(": "reduce_32",
            "{": "reduce_32",
            ";": "reduce_32"
        },
        "135": {
            "SAVE": "goto_137",
            "if": "reduce_72",
            "return": "reduce_72",
            "switch": "reduce_72",
            "NUM": "reduce_72",
            "ID": "reduce_72",
            ":": "reduce_72",
            "break": "reduce_72",
            "while": "reduce_72",
            ";": "reduce_72",
            "{": "reduce_72",
            "(": "reduce_72"
        },
        "136": {
            ";": "shift_43",
            "(": "shift_44",
            "{": "shift_32",
            "break": "shift_46",
            "if": "shift_47",
            "while": "shift_48",
            "return": "shift_49",
            "switch": "shift_50",
            "compound_stmt": "goto_51",
            "statement": "goto_52",
            "expression_stmt": "goto_53",
            "selection_stmt": "goto_54",
            "iteration_stmt": "goto_55",
            "return_stmt": "goto_56",
            "switch_stmt": "goto_57",
            "expression": "goto_58",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67",
            "}": "reduce_40"
        },
        "137": {
            ":": "shift_138"
        },
        "138": {
            "statement_list": "goto_139",
            "if": "reduce_21",
            "return": "reduce_21",
            "}": "reduce_21",
            "switch": "reduce_21",
            "case": "reduce_21",
            "ID": "reduce_21",
            "NUM": "reduce_21",
            "default": "reduce_21",
            "break": "reduce_21",
            "while": "reduce_21",
            ";": "reduce_21",
            "{": "reduce_21",
            "(": "reduce_21"
        },
        "139": {
            ";": "shift_43",
            "(": "shift_44",
            "{": "shift_32",
            "break": "shift_46",
            "if": "shift_47",
            "while": "shift_48",
            "return": "shift_49",
            "switch": "shift_50",
            "compound_stmt": "goto_51",
            "statement": "goto_52",
            "expression_stmt": "goto_53",
            "selection_stmt": "goto_54",
            "iteration_stmt": "goto_55",
            "return_stmt": "goto_56",
            "switch_stmt": "goto_57",
            "expression": "goto_58",
            "var": "goto_59",
            "simple_expression": "goto_60",
            "additive_expression": "goto_61",
            "term": "goto_62",
            "factor": "goto_63",
            "call": "goto_64",
            "PID": "goto_65",
            "PNUM": "goto_66",
            "NUM": "reduce_69",
            "ID": "reduce_67",
            "default": "reduce_39",
            "}": "reduce_39",
            "case": "reduce_39"
        }
    }
}

semantic_actions = ["PID", "PNUM", "PTYPE", "FUNC", "VAR_DEC", "ARRAY_DEC", "BREAK_JP", "SAVE", "JPF", "JPF_SAVE", "JP",
                    "WHILE", "LABEL_WHILE", "LABEL_SWITCH", "ASSIGN", "ARRAY_CELL", "RELOP", "ADDOP", "MULTOP"]


class Parser:

    def __init__(self):
        self.scanner = Scanner("input.txt")
        self.terminal = grammar['terminals']
        self.non_terminal = grammar['non_terminals']
        self.first = grammar['first']
        self.follow = grammar['follow']
        self.grammar = grammar['grammar']
        self.parse_table = grammar['parse_table']
        self.stack = ['0']
        self.gotos = self.goto_states()
        self.errors = []
        self.syntax_error_writer = SyntaxErrorWriter('syntax_errors.txt')
        self.parse_tree_writer = ParseTreeWriter('parse_tree.txt')
        self.code_generator = CodeGenerator()

    def get_next_token(self):
        current_token = self.scanner.get_next_token()

        while current_token and (current_token[0] == WHITESPACE or current_token[0] == COMMENT):
            current_token = self.scanner.get_next_token()

        return current_token

    def parse(self):
        current_token = self.get_next_token()
        while True:
            last_index = self.stack[-1]
            try:
                next_move = self.parse_table[last_index][Parser.get_token_value(current_token)].split('_')
            except Exception:
                self.errors.append(f"#{current_token[2]} : syntax error , illegal {Parser.get_token_value(current_token)}")
                current_token = self.get_next_token()
                while self.stack[-1] not in self.gotos:
                    self.stack.pop()
                    removed = self.stack.pop()
                    if removed.name in self.non_terminal:
                        self.errors.append(f"syntax error , discarded {removed.name} from stack")
                    else:
                        self.errors.append(f"syntax error , discarded ({removed.name[0]}, {removed.name[1]}) from stack")
                while not self.is_in_follows(self.stack[-1], Parser.get_token_value(current_token)):
                    if Parser.get_token_value(current_token) == '$':
                        self.errors.append(f"#{current_token[2]} : syntax error , Unexpected EOF")
                        self.syntax_error_writer.write(self.errors)
                        return
                    self.errors.append(f"#{current_token[2]} : syntax error , discarded {current_token[1]} from input")
                    current_token = self.get_next_token()
                next_non_terminal = self.is_in_follows(self.stack[-1], Parser.get_token_value(current_token))
                next_state = self.parse_table[self.stack[-1]][next_non_terminal].split('_')[1]
                self.errors.append(f"#{current_token[2]} : syntax error , missing {next_non_terminal}")
                self.stack.append(Node(next_non_terminal))
                self.stack.append(next_state)

                continue
            if next_move[0] == "accept":
                Node('$', left_rule_node)
                self.parse_tree_writer.write(Parser.format_tree(left_rule_node))
                self.syntax_error_writer.write(self.errors)
                print(len(self.code_generator.program_block.instructions))
                print(self.code_generator.program_block)
                return
            elif next_move[0] == 'shift':
                if current_token:
                    node = Node((current_token[0], current_token[1]))
                else:
                    node = Node(current_token)
                self.stack.append(node)
                self.stack.append(next_move[1])
                current_token = self.get_next_token()
            elif next_move[0] == 'reduce':
                rule = self.grammar[next_move[1]]
                function = self.code_generator.function_dict.get(int(next_move[1]))
                if function:
                    if int(next_move[1]) in [67, 68, 69, 70]:
                        function(lexeme=current_token[1])
                    else:
                        function()
                left_rule, right_rule = rule[0], rule[2:]
                left_rule_node = Node(left_rule)
                if right_rule != ['epsilon']:
                    start_reduce_index = len(self.stack) - 2 * len(right_rule)
                    for i in range(2 * len(right_rule)):
                        item = self.stack.pop(start_reduce_index)
                        if i % 2 == 0:
                            item.parent = left_rule_node
                else:
                    Node('epsilon', left_rule_node)
                next_move = self.parse_table[self.stack[-1]][left_rule].split('_')
                self.stack.append(left_rule_node)
                if next_move[0] != 'goto':
                    raise Exception("goto error")
                self.stack.append(next_move[1])

    def goto_states(self) -> list:
        result = []

        for state in self.parse_table.keys():
            row = self.parse_table[state]
            for word in row.values():
                if word.startswith('goto'):
                    result.append(state)
                    break

        return result

    def get_gotos_alphabetically(self, state: str):
        result = []
        state_row = self.parse_table[state]
        for word in state_row.keys():
            if state_row[word].startswith('goto'):
                result.append(word)
        result.sort()
        return result

    def is_in_follows(self, state: str, token):
        gotos = self.get_gotos_alphabetically(state)
        for goto in gotos:
            if token in self.follow[goto]:
                return goto

        return None

    @staticmethod
    def format_tree(root: Node):
        result = ''
        for pre, fill, node in RenderTree(root):
            result += '%s%s' % (pre, Parser.format_node_name(node)) + '\n'
        return result

    @staticmethod
    def format_node_name(node):
        if type(node.name) == tuple:
            return f'({node.name[0]}, {node.name[1]})'
        return node.name

    @staticmethod
    def get_token_value(token):
        if token[0] == EOF:
            return '$'
        if token[0] == KEYWORD or token[0] == SYMBOL:
            return token[1]
        return token[0]
