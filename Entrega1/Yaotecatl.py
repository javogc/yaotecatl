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
    'write' : 'WRITE',
    'return' : 'RETURN',
    'array' : 'ARRAY',
    'char' : 'CHAR',
    'string' : 'STRING',
    'float' : 'FLOAT',
    'int' : 'INT',
    'void' : 'VOID'
}

tokens = ['LFTBRAC', 'RGTBRAC', 'LFTPAREN','RGTPAREN', 'LFTBRACSQR', 'RGTBRACSQR', 'AND', 'DOUBEQUAL',
          'NOT','OR','SEMICOLON', 'EQUAL', 'LESSTHANEQUAL', 'GREATTHANEQUAL', 'GREATTHAN', 'LESSTHAN',  
          'PLUS', 'MINUS', 'MULTIPLICATION', 'DIVISION', 'INT', 'FLOAT', 'STRING', 'ID', 'COMMA' ] + list(reserved.values())

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

def p_assignment(p):
    '''assignment : assignmentaux EQUAL expression SEMICOLON 
    | assignmentaux EQUAL call SEMICOLON'''    
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
    '''conditionaux : LFTPAREN expression RGTPAREN block ELSEIF conditionaux 
    | LFTPAREN expression RGTPAREN block '''              

def p_constant(p):
    '''constant : ID 
    | array 
    | cteN
    | cteS
    | TRUE 
    | FALSE '''

def p_cteN(p):
    '''cteN : FLOAT 
    | INT'''

def p_cteS(p):
    '''cteS : STRING'''

def p_exp(p):
    '''exp : term 
    | term expaux  '''   
def p_expaux(p):
    '''expaux : PLUS exp expaux 
    | MINUS exp expaux 
    | empty '''    

def p_factor(p):
    '''factor : factoraux constant 
    | LFTPAREN expression RGTPAREN ''' 
def p_factoraux(p):
    '''factoraux : PLUS 
    | MINUS ''' 

def p_expression(p):
    '''expression : exp 
    | expressionaux exp ''' 
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
    | vars 
    | loop 
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
    '''function : FUNCTION functionaux ID LFTPAREN functionaux2 RGTPAREN blockreturn  '''
def p_functionaux(p):
    '''functionaux : VOID 
    | type  '''  
def p_functionaux2(p):
    '''functionaux2 : parameter 
    | empty  ''' 

def p_vars(p):
    '''vars : type varsaux2 SEMICOLON    ''' 
def p_varsaux(p):
    '''varsaux : PLUS 
    | MINUS 
    | empty   '''   
def p_varsaux2(p):
    '''varsaux2 : ID EQUAL varsaux constant 
    | ID EQUAL varsaux constant COMMA varsaux2  '''

def p_call(p):
    '''call : ID LFTPAREN exp RGTPAREN SEMICOLON 
    | ID LFTPAREN exp COMMA call RGTPAREN SEMICOLON  ''' 

def p_read(p):
    '''read : READ LFTPAREN ID RGTPAREN SEMICOLON '''                              

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p)#p.value)
    else:
        print("Syntax error at EOF")



yacc.yacc()



# Main
if __name__ == '__main__':
    # Check for file
    if (len(sys.argv) > 1):
        file = sys.argv[1]
        # Open file
        try:
            f = open(file, 'r')
            data = f.read()
            f.close()
            # Parse the data
            if (yacc.parse(data, tracking = True) == 'OK'):
                print(dirProc);
        except EOFError:
            print(EOFError)
    else:
        print('File missing')
        while 1:
            try:
                s = raw_input('')
            except EOFError:
                break
            if not s:
                continue
            yacc.parse(s)






