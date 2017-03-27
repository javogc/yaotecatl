from cuboSemantico import *
from lex import *
import collections
from collections import OrderedDict



#------------------------------Comienzo de Yacc --------------------------------------------

import ply.yacc as yacc


quadruplesList = [] #lista/arreglo que guardara un objeto diccionario que sera cada quadruplo

scopeVar = 'global' #variable que cambiara entre local y global para crear las tablas

globalVarDict = dict()  #diccionario que tendra las variables globales
localVarDict = dict() #diccionario que tendra las variables locales
constantDict = dict() #dicionario que tendra las constantes
funcDict = dict() #diccionario que tendra las funciones del programa con sus parametros 

funcParameters = [] #arreglo en donde se guardaran los parametros y despues meterlos al diccionario del funciones.
codeTypeVoid = False #variable que cambiara dependiendo si la funcion es void o no
funcIndicator = False #variable que cambiara dependiendo si estas en una funcion o variable para colocar el tipo

nameOfFunct = "" #variable que guardara el nombre de la funccion y despues la metera al diccionario de funciones
typeOfFunct = "" #variable que guardara el tipo de la funccion y despues la metera al diccionario de funciones

nameOfVar = "" #variable que guardara el nombre del ID que encontro y despues la metera al diccionario ya sea global o local
typeOfVar = "" #variable que guardara el tipo del ID que encontro y despues la metera al diccionario ya sea global o local

popper = [] #pila que tendra los operadores hasta ser sacados

pilaO = [] #pila que tendra los operandos y despues los operador cuando se haga pop en el popper

isInt = False #variable para saber si la constante es int o no

jumps = []

#-------------------------Reglas del compilador-----------------

def p_program(p):
    '''program : PROGRAM ID LFTBRAC auxprogram main RGTBRAC'''

    #Pruebas de print para verificar que el codigo funcione bien
    #print('Table of Functions: %s' % funcDict)
    #print('------------------------------------')
    #print('------------------------------------')

    #print('Table of Global Variables: %s' % globalVarDict)
    #print('-------------------------------------')
    #print('------------------------------------')

   # print('Table of Local(main) Variables: %s' % localVarDict)
    #print('------------------------------------')
    #print('------------------------------------')

    #para imprimir los cuadrulos uno por uno
    countQuadruples = 0 
    for p in quadruplesList:

        print "Quadruple:", countQuadruples
        
        print p
        print
        countQuadruples = countQuadruples + 1;

    
    #print(checkSemanticCube("int" ,"float" ,"+"))

def p_auxprogram(p):
    '''auxprogram : vars auxprogram 
    | function auxprogram 
    | '''

def p_array(p):
    '''array : ID LFTBRACSQR exp RGTBRACSQR'''

def p_arrayvals(p):
    '''arrayvals : LFTBRACSQR arrayvalsaux RGTBRACSQR '''
def p_arrayvalsaux(p):
    '''arrayvalsaux : constant  
    | constant COMMA arrayvalsaux '''        

def p_assignment(p):
    '''assignment : assignmentaux EQUAL expression SEMICOLON '''    
def p_assignmentaux(p):
    '''assignmentaux : ID 
    | array'''  

def p_blockreturn(p):
    '''blockreturn : LFTBRAC blockneutral RGTBRAC 
    | LFTBRAC blockneutral RETURN exp SEMICOLON RGTBRAC ''' 
def p_blockneutral(p):
    '''blockneutral : statement blockneutral 
    | vars blockneutral
    | empty ''' 
def p_block(p):
    '''block : LFTBRAC blockneutral RGTBRAC'''       

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

    p[0] = p[1]

 

def p_cteN(p):
    '''cteN : FLOAT codeAddConst
    | INT codeAddConst'''

    p[0] = p[1]

def p_cteS(p):
    '''cteS : STRING'''
    p[0] = p[1]

def p_exp(p):
    '''exp : term
    | term PLUS codeAddOperator exp
    | term MINUS codeAddOperator exp  '''   

def p_factoraux(p):
    '''factoraux : constant
    | PLUS constant
    | MINUS constant ''' 

    global pilaO

    if len(p) == 2: #si la longitud de la regla es de 2 entonces busca el operando en todas las tablas que esta en la posicion p[1]
        pilaO.append(searchForOperand(p[1]))
 
    else:   #si la longitud de la regla es de 2 entonces busca el operando en todas las tablas que esta en la posicion p[2]
        pilaO.append(searchForOperand(p[2]))
    
    
    

def p_factor(p):
    '''factor : LFTPAREN codeAddOpenParen expression RGTPAREN codeDeleteOpenParen codeAskFactor
    | factoraux codeAskFactor''' 

def p_expression(p):
    '''expression : exp 
    | exp expressionaux codeAddOperator exp codeAskExpression''' 
def p_expressionaux(p):
    '''expressionaux : AND 
    | DOUBEQUAL 
    | NOT 
    | OR 
    | LESSTHANEQUAL 
    | GREATTHANEQUAL 
    | GREATTHAN 
    | LESSTHAN '''   

    p[0] = p[1]                      

def p_loop(p):
    '''loop : WHILE codeWhileCondition LFTPAREN expression RGTPAREN codeGOTOF block codeGOTO ''' 

def p_write(p):
    '''write : PRINT LFTPAREN constant RGTPAREN SEMICOLON ''' 

def p_parameter(p):
    '''parameter : type codeCheckType ID codeAddParameters
    | type codeCheckType ID codeAddParameters COMMA parameter 
    | empty  '''   

def p_term(p):
    '''term : factor MULTIPLICATION codeAddOperator term
    | factor DIVISION codeAddOperator term 
    | factor codeAskTerm ''' 

     

def p_statement(p):
    '''statement : assignment 
    | condition 
    | loop 
    | write 
    | read 
    | call  ''' 

def p_type(p):
    '''type : INT  
    | FLOAT 
    | CHAR 
    | BOOL 
    | STRING   ''' 

    p[0] = p[1]

def p_main(p):
    '''main : PRIOMH codeScope block  ''' 


def p_function(p):
    '''function : FUNCTION codeScope functionaux ID codeNameOfFunct LFTPAREN parameter RGTPAREN blockreturn codeScope  '''
    
    global nameOfFunct
    global typeOfFunct
    global funcParameters
    global localVarDict  

    addFunctDict(nameOfFunct, typeOfFunct, funcParameters) #agrega el nombre, tipo y parametros al diccionario de funciones

    #print('Table of Local(funct) Variables: %s' % localVarDict)
    
    localVarDict.clear() #limpia el diccionario de variables locales para usarlo en otra funcion

    funcParameters = [] #limpia el arreglo de parametros para usarlo en otra funcion
  

def p_functionaux(p):
    '''functionaux : VOID codeTypeVoid codeCheckType 
    | codeFuncIndicator type codeCheckType '''  

def p_vars(p):
    '''vars : type codeCheckType varsaux     ''' 
def p_varsaux(p):
    '''varsaux : ID codeAddVar EQUAL expression SEMICOLON
    | ID codeAddVar EQUAL expression COMMA varsaux 
    | ID  codeAddVarArreglo LFTBRACSQR INT RGTBRACSQR EQUAL arrayvals SEMICOLON
    | ID codeAddVarArreglo LFTBRACSQR INT RGTBRACSQR  EQUAL arrayvals COMMA varsaux '''


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




#-------------------------------------------------- VAR TABLE RULES -------------------------------------

def p_codeGOTO(p):
    '''codeGOTO : '''
    quadruplesList[jumps.pop()]["RESULT"] = len(quadruplesList) + 1
    addNewQuadruple('GOTO', "", "", jumps.pop())
    



def p_codeGOTOF(p):
    '''codeGOTOF : '''
    respGotof = pilaO.pop()

    if respGotof['type'] == 3:

        addNewQuadruple("GOTOF", respGotof, "", "")
        jumps.append(len(quadruplesList)-1)


    else:
        print("Can't compare result, answer is not 'BOOL' type!")
        exit(1)

def p_codeWhileCondition(p):
    '''codeWhileCondition : '''

    jumps.append(len(quadruplesList))


def p_codeScope(p):
    '''codeScope : '''

    global scopeVar

    if scopeVar == 'global': #cambia el scope de global a local o viceversa
        scopeVar = 'local'
    else:
        scopeVar = 'global'   


def p_codeCheckType(p):
    '''codeCheckType : '''

    global typeOfFunct
    global typeOfVar
    global funcIndicator
    global codeTypeVoid
    
    #IFs para verificar si el tipo se le pone a una funcion o a una variable o si la funcion es void o no.

    if funcIndicator == True: #el type es de una funcion y no variable
        typeOfFunct = listOfTypes(p[-1])
        funcIndicator = False

    elif codeTypeVoid == True:
        typeOfFunct = 4
        codeTypeVoid = False

    else:
        typeOfVar = listOfTypes(p[-1])
           


def p_codeAddVar(p):
    '''codeAddVar : '''

    global nameOfVar

    nameOfVar = p[-1] # p[-1] saca el ultimo valor que en este caso era el ID

    AddVarDict(nameOfVar, typeOfVar) #llama la funcion para agregar la variable al diccionario local o global

def p_codeAddVarArreglo(p):
    '''codeAddVarArreglo : '''

    global nameOfVar

    nameOfVar = p[-1]

    AddVarDict(nameOfVar, typeOfVar + 100)    #llama la funcion para agregar la variable al diccionario y le suma 100 al tipo ya que es un arreglo 


def p_codeAddParameters(p):
    '''codeAddParameters : '''

    global nameOfVar
    global typeOfVar
    global funcParameters

    nameOfVar = p[-1] #saca el ID
    
    AddVarDict(nameOfVar, typeOfVar) #agrega el ID y tipo al diccionary que sera local, puesto que todos los parametros van local

    #arreglo que contiene valores sacados del diccionario
    funcParameters.append(localVarDict[nameOfVar]) #saca del diccionario local con la key que es el nombre de la variable y la agrega al arreglo de parametros

def p_codeNameOfFunct(p):
    '''codeNameOfFunct : '''

    global nameOfFunct

    nameOfFunct = p[-1] #la guarda el ID de la funcion para alrato cuando acabe de declarar sus parametros guarde todo junto


def p_codeTypeVoid(p):
    '''codeTypeVoid : '''

    global codeTypeVoid
    codeTypeVoid = True #la variable se cambia a true porque el tipo sera para una funcion void
    

def p_codeFuncIndicator(p):
    '''codeFuncIndicator : '''

    global funcIndicator
    funcIndicator = True #la variable se cambia a true porque el tipo sera para una funcion no void


def p_codeDeleteOpenParen(p): # Se acabo de hacer lo de adentro del parentesis
    '''codeDeleteOpenParen : empty'''
    global popper
   
    popper.pop()




def p_codeAddOpenParen(p): #abre parentesis en una operacion
    '''codeAddOpenParen : empty'''
    global popper
    
    popper.append('(')



def p_codeAddConst(p): #agrega una constante ya sea int o double al diccionario de constantes
    '''codeAddConst : empty'''

    global constantDict

    if isInt(p[-1]):
        typeOfConst = 0
    else:
        typeOfConst = 1
    
    constantDict[str(p[-1])] = {'val':p[-1], 'type':typeOfConst}




def p_codeAddOperator(p): #agrega un operador al popper
    '''codeAddOperator : empty'''
    global popper

    popper.append(p[-1])



def p_codeAskTerm(p):
    '''codeAskTerm : empty'''
    global popper
    global pilaO

    if len(popper) > 0: #checa si el popper tiene algo dentro

        if popper[-1] == '-' or popper[-1] == '+': #si el siguiente character es un + o - hacer pop al popper y dos veces a la pilaO

            op2 = pilaO.pop()
            op1 = pilaO.pop()
            operator = popper.pop()

            newType = checkSemanticCube( op1['type'] ,op2['type'] ,operator) #checar si los 2 operandos que sacaste son compatibles con el operador
            
            if newType < 10: # si si son compatibles los argrega al quadruplo
                
                respAux = {'val':"T1", 'type':newType}

                addNewQuadruple(operator, op1, op2, respAux)

                pilaO.append(respAux) #la respuesta es agregada a la pilaO con su nuevo tipo

            else: #Si no son compatibles marca error
                print("You cant evaluate those operands with that operator!")
                exit(1)


def p_codeAskFactor(p):
    '''codeAskFactor : empty'''
    global popper
    global pilaO

    if len(popper) > 0: #checa si el popper tiene algo dentro

        if popper[-1] == '*' or popper[-1] == '/': #si el siguiente character es un + o - hacer pop al popper y dos veces a la pilaO

            op2 = pilaO.pop()
            op1 = pilaO.pop()
            operator = popper.pop()

            newType = checkSemanticCube( op1['type'] ,op2['type'] ,operator) #checar si los 2 operandos que sacaste son compatibles con el operador
            
            if newType < 10: # si si son compatibles los argrega al quadruplo
                respAux = {'val':"T1", 'type':newType}

                addNewQuadruple(operator, op1, op2, respAux)

                pilaO.append(respAux) #la respuesta es agregada a la pilaO con su nuevo tipo

            else: #Si no son compatibles marca error
                print("You cant evaluate those operands with that operator!")
                exit(1)




def p_codeAskExpression(p):
    '''codeAskExpression : empty'''
    global popper
    global pilaO

    if len(popper) > 0:

        if popper[-1] == '<' or popper[-1] == '>' or popper[-1] == '<=' or popper[-1] == '>=' or popper[-1] == '==' or popper[-1] == '!=' or popper[-1] == '||' or popper[-1] == '&&':

            op2 = pilaO.pop()
            op1 = pilaO.pop()
            operator = popper.pop()

            newType = checkSemanticCube( op1['type'] ,op2['type'] ,operator) #checar si los 2 operandos que sacaste son compatibles con el operador
            
            if newType < 10: # si si son compatibles los argrega al quadruplo
                respAux = {'val':"T1", 'type':newType}

                addNewQuadruple(operator, op1, op2, respAux)

                pilaO.append(respAux) #la respuesta es agregada a la pilaO con su nuevo tipo

            else: #Si no son compatibles marca error
                print("You cant evaluate those operands with that operator!")
                exit(1)






yacc.yacc()

#----------------------------Funciones externas-------------------------

#checa si es int o no 
def isInt(x):
  try:
    int(x)
    return True
  except:
    return False


# le llega como parametro el tipo de la funcion o variable y regresa el numero con lo que las identificaremos

def listOfTypes(auxType): 
    if auxType == "int":
        return 0
    elif auxType == "float":
        return 1    
    elif auxType == "string":
        return 2 
    elif auxType == "bool":
        return 3        
    elif auxType == "intArr":
        return 100 
    elif auxType == "floatArr":
        return 101  
    elif auxType == "stringArr":
        return 102            
    elif auxType == "boolArr":
        return 103
            

# le llega como parametro el tipo(numero) de la funcion o variable y regresa el tipo(nombre) con lo que las identificaremos
def listOfTypesReversed(auxType): 
    if auxType == 0:
        return "int"
    elif auxType == 1:
        return "float"    
    elif auxType == 2:
        return "string" 
    elif auxType == 3:
        return "bool"       
    elif auxType == 100:
        return "intArr"
    elif auxType == 101:
        return "floatArr" 
    elif auxType == 102:
        return "stringArr"            
    elif auxType == 103:
        return "boolArr"





def addFunctDict(functName, functType, functParameters):
    
    global funcDict

    if functName in funcDict.keys():   #verifica si la funcion ya existe en el diccionario
        print ("Error in function table, the function already exists! ")
        
    else:
        funcDict[functName] = {'ID':functName, 'type':functType, 'parameters':functParameters} #guarda la funcion en el diccionario


def AddVarDict(varName, varType): 
    global scopeVar
    global globalVarDict
    global localVarDict

    if scopeVar == 'global':    # verifica si es global el scope actual para saber si guardarla in el diccionario global o local
        if varName in globalVarDict.keys(): # si ya existe la variable en el diccionario mostrarle un error
            print("Error in global table, variable already exists!")

        else:
            globalVarDict[varName] = {'ID':varName, 'type':varType}  # si no existe agregarla al diccionario
            
    else:       #hacer lo mismo que en global pero en local
        if not varName in localVarDict.keys():
            localVarDict[varName] = {'ID':varName, 'type':varType}
        else:
            rint("Error in local table, variable already exists!")




#Busca la variable o constante de todas las tablas/diccionarios y regresa un objeto diccionario
def searchForOperand(key):
    if key in globalVarDict.keys():
        return globalVarDict[key]

    elif key in localVarDict.keys():
        return localVarDict[key]

    elif key in constantDict.keys():
        return constantDict[key]    
    
    else:
        print("Variable not found!", key) #imprime cual variable no fue declarada en ninguna de las tablas 
   








#crea un nuevo cuadruple utilizando un diccionario y lo agrega a la lista/arreglo de quadruples
def addNewQuadruple(operator, op1, op2, result):
    global quadruplesList
    notOrderDict = OrderedDict() #para orderar el quadruplo como lo escribo
    notOrderDict = {'OPERATOR':operator, 'OP1':op1, 'OP2':op2, 'RESULT':result }
    orderDict = notOrderDict.copy()
    quadruplesList.append(orderDict)





# para poder meter un test file y verificar en donde ocurren los errores
if __name__ == '__main__':
    if (len(sys.argv) > 1):
        file = sys.argv[1]
        try:
            f = open(file, 'r')
            data = f.read()
            yacc.parse(data, tracking = True) 
        except EOFError:
            print(EOFError)
   






