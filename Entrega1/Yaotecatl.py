import sys
sys.path.insert(0, "../..")

#------------------------------Comienzo de Lex --------------------------------------------

import ply.lex as lex

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

tokens = ['LFTBRAC', 'RGTBRAC', 'LFTPAREN','RGTPAREN', 'LFTBRACSQR', 'RGTBRACSQR', 'AND', 'DOUBEQUAL',
          'NOT','OR','SEMICOLON', 'EQUAL', 'LESSTHANEQUAL', 'GREATTHANEQUAL', 'GREATTHAN', 'LESSTHAN',  
          'PLUS', 'MINUS', 'MULTIPLICATION', 'DIVISION', 'ID', 'COMMA' ] + list(reserved.values())

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
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\/'
t_INT = r'[0-9]+'
t_FLOAT = r'[0-9]+\.[0-9]+'
#t_CHAR = r'[a-zA-Z0-9]'
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
    '''auxprogram : vars auxprogram 
    | function auxprogram 
    | empty'''

def p_array(p):
    '''array : ID LFTBRACSQR exp RGTBRACSQR'''

def p_arrayvalues(p):
    '''arrayvalues : LFTBRACSQR arrayvaluesaux RGTBRACSQR '''
def p_arrayvaluesaux(p):
    '''arrayvaluesaux : constant  
    | constant COMMA arrayvaluesaux '''        

def p_assignment(p):
    '''assignment : assignmentaux EQUAL expression SEMICOLON '''    
def p_assignmentaux(p):
    '''assignmentaux : ID 
    | array'''  

def p_blockreturn(p):
    '''blockreturn : LFTBRAC blockreturnaux RGTBRAC 
    | LFTBRAC blockreturnaux RETURN exp SEMICOLON RGTBRAC ''' 
def p_blockreturnaux(p):
    '''blockreturnaux : statement blockreturnaux 
    | empty ''' 

def p_block(p):
    '''block : LFTBRAC blockaux RGTBRAC'''   
def p_blockaux(p):
    '''blockaux : statement blockaux 
    | empty '''     

def p_condition(p):
    '''condition : IF conditionaux 
    | IF conditionaux ELSE block ''' 
def p_conditionaux(p):
    '''conditionaux : LFTPAREN expression RGTPAREN block conditionaux2 '''      
def p_conditionaux2(p):
    '''conditionaux2 : ELSEIF conditionaux 
    | empty ''' 


def p_constant(p):
    '''constant : ID 
    | array 
    | cteN
    | cteS
    | TRUE 
    | FALSE
    | call2 '''

def p_cteN(p):
    '''cteN : FLOAT 
    | INT'''

def p_cteS(p):
    '''cteS : STRING'''

def p_exp(p):
    '''exp : term expaux  '''   
def p_expaux(p):
    '''expaux : PLUS exp expaux 
    | MINUS exp expaux 
    | empty '''    

def p_factor(p):
    '''factor : LFTPAREN expression RGTPAREN
    | constant
    | MINUS constant
    | PLUS constant ''' 

def p_expression(p):
    '''expression : exp 
    | exp expressionaux exp ''' 
def p_expressionaux(p):
    '''expressionaux : AND 
    | DOUBEQUAL 
    | NOT 
    | OR 
    | LESSTHANEQUAL 
    | GREATTHANEQUAL 
    | GREATTHAN 
    | LESSTHAN '''                         

def p_loop(p):
    '''loop : WHILE LFTPAREN expression RGTPAREN block ''' 

def p_write(p):
    '''write : PRINT LFTPAREN constant RGTPAREN SEMICOLON ''' 

def p_parameter(p):
    '''parameter : type ID 
    | type ID COMMA parameter 
    | empty  '''   

def p_term(p):
    '''term : factor termaux  ''' 
def p_termaux(p):
    '''termaux : MULTIPLICATION term termaux 
    | DIVISION term termaux 
    | empty  ''' 

def p_statement(p):
    '''statement : assignment 
    | condition 
    | loop 
    | vars
    | write 
    | read 
    | call  ''' 

def p_type(p):
    '''type : INT 
    | FLOAT 
    | CHAR 
    | BOOL 
    | STRING  ''' 

def p_main(p):
    '''main : PRIOMH block  ''' 

def p_function(p):
    '''function : FUNCTION functionaux ID LFTPAREN parameter RGTPAREN blockreturn  '''
def p_functionaux(p):
    '''functionaux : VOID 
    | type  '''  

def p_vars(p):
    '''vars : type varsaux     ''' 
def p_varsaux(p):
    '''varsaux : ID EQUAL expression SEMICOLON
    | ID EQUAL expression COMMA varsaux 
    | ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues SEMICOLON
    | ID LFTBRACSQR INT RGTBRACSQR EQUAL arrayvalues COMMA varsaux '''

def p_call(p):
    '''call : ID LFTPAREN exp callaux RGTPAREN SEMICOLON  ''' 
def p_callaux(p):
    '''callaux : COMMA exp callaux
    | empty ''' 

def p_call2(p):
    '''call2 : ID LFTPAREN exp callaux RGTPAREN  ''' 

def p_read(p):
    '''read : READ LFTPAREN readaux RGTPAREN SEMICOLON '''   
def p_readaux(p):
    '''readaux : ID
    | array '''                                  

def p_empty(p):
    '''empty : '''
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p)
    else:
        print("Syntax error at EOF")



yacc.yacc()




if __name__ == '__main__':
    if (len(sys.argv) > 1):
        file = sys.argv[1]
        try:
            f = open(file, 'r')
            data = f.read()
            yacc.parse(data, tracking = True)
        except EOFError:
            print(EOFError)
   






