import sys
sys.path.insert(0, "../..")

#------------------------------Comienzo de Lex --------------------------------------------

import ply.lex as lex

reserved = {
    'priomh' : 'PRIOMH',
    'program' : 'PROGRAM',
    'function' : 'function',
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
    'write' : 'WRITE',
    'return' : 'RETURN',
    'array' : 'ARRAY',
    'char' : 'CHAR',
    'string' : 'string',
    'float' : 'FLOAT',
    'int' : 'INT',
    'void' : 'VOID'
}

tokens = ['LFTBRAC', 'RGTBRAC', 'LFTPAREN','RGTPAREN', 'LFTBRACSQR', 'RGTBRACSQR', 'AND', 'DOUBEQUAL',
          'NOT','OR','SEMICOLON', 'EQUAL', 'LESSTHANEQUAL', 'GREATTHANEQUAL', 'GREATTHAN', 'LESSTHAN',  
          'PLUS', 'MINUS', 'MULTIPLICATION', 'DIVISION', 'INT', 'FLOAT', 'STRING', 'ID', 'COMMA', 'CHAR' ] + list(reserved.values())

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
t_SEMICOLON = r'\,'
t_COMMA = r'\;'
t_EQUAL = r'='
t_LESSTHANEQUAL = r'\<='
t_GREATTHANEQUAL = r'\>='
t_GREATTHAN = r'\>'
t_LESSTHAN = r'\<'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\/'
t_INT = r'[0-9]+'
t_FLOAT = r'[0-9]+\.[0-9]+'
t_CHAR = r'[a-zA-Z0-9]'
t_STRING = r'\".*\"'
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


#------------------------------Comienzo de Yacc --------------------------------------------

import ply.yacc as yacc


def p_program(p):
    '''program : PROGRAM ID LFTBRAC auxprogram main RGTBRAC'''
def p_auxprogram(p):
    '''auxprogram : vars auxprogram | function auxprogram | empty'''

def p_array(p):
    '''array : ID LFTBRACSQR exp RGTBRACSQR'''

def p_assignment(p):
    '''assignment : assignmentaux EQUAL expression SEMICOLON | assignmentaux EQUAL call SEMICOLON'''    
def p_assignmentaux(p):
    '''assignmentaux : ID | array'''  

def p_blockreturn(p):
    ''''''  






yacc.yacc()










