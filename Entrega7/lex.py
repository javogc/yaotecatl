import sys
import ply.lex as lex

#Palabras reservadas del programa
reserved = {
    'priomh' : 'PRIOMH',
    'program' : 'PROGRAM',
    'function' : 'FUNCTION',
    'if' : 'IF',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'priomh' : 'PRIOMH',
    'while' : 'WHILE',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'bool' : 'BOOL',
    'print' : 'PRINT',
    'read' : 'READ',
    'return' : 'RETURN',
    'char' : 'CHAR',
    'string' : 'STRING',
    'float' : 'FLOAT',
    'int' : 'INT',
    'void' : 'VOID'
}
#Los tokens que va a reconocer el programa
tokens = ['LFTBRAC', 'RGTBRAC', 'LFTPAREN','RGTPAREN', 'LFTBRACSQR', 'RGTBRACSQR', 'AND', 'DOUBEQUAL',
          'NOT','OR','SEMICOLON', 'EQUAL', 'LESSTHANEQUAL', 'GREATTHANEQUAL', 'GREATTHAN', 'LESSTHAN',  
          'PLUS', 'MINUS', 'MULTIPLICATION', 'DIVISION', 'ID', 'COMMA' ] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_LFTBRAC = r'\{'
t_RGTBRAC = r'\}'
t_LFTPAREN = r'\('
t_RGTPAREN = r'\)'
t_LFTBRACSQR = r'\['
t_RGTBRACSQR = r'\]'
t_AND = r'&&'
t_DOUBEQUAL = r'=='
t_NOT = r'!='
t_OR = r'\|\|'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_EQUAL = r'='
t_LESSTHANEQUAL = r'\<='
t_GREATTHANEQUAL = r'\>='
t_GREATTHAN = r'\>'
t_LESSTHAN = r'\<'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\/'
t_INT = r'[0-9]+'
t_FLOAT = r'[0-9]+\.[0-9]+'
#t_CHAR = r'\".\"'
t_STRING = r'\"([^\\\"]|\\.)*\"'
t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()
