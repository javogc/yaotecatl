from cuboSemantico import *
from lex import *




#------------------------------Comienzo de Yacc --------------------------------------------

import ply.yacc as yacc


quadruples = []

scopeVar = 'global' #variable que cambiara entre local y global para crear las tablas

globalVarDict = dict()  #diccionario que tendra las variables globales

funcDict = dict() #diccionario que tendra las funciones del programa con sus parametros 
funcParameters = [] #arreglo en donde se guardaran los parametros y despues meterlos al diccionario del funciones.
codeTypeVoid = False #variable que cambiara dependiendo si la funcion es void o no
funcIndicator = False #variable que cambiara dependiendo si estas en una funcion o variable para colocar el tipo

localVarDict = dict() #diccionario que tendra las variables locales

nameOfFunct = "" #variable que guardara el nombre de la funccion y despues la metera al diccionario de funciones
typeOfFunct = "" #variable que guardara el tipo de la funccion y despues la metera al diccionario de funciones

nameOfVar = "" #variable que guardara el nombre del ID que encontro y despues la metera al diccionario ya sea global o local
typeOfVar = "" #variable que guardara el tipo del ID que encontro y despues la metera al diccionario ya sea global o local

popper = []

pilaO = []
typePila = []







constants = {'true':{'value':True, 'type':3}, 'false':{'value':False, 'type':3}}


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

    print("quadruples")
    print(quadruples)

    
    #print(checkSemanticCube("int" ,"float" ,"+"))

def p_auxprogram(p):
    '''auxprogram : vars auxprogram 
    | function auxprogram 
    | '''

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
    '''cteN : FLOAT addConstant
    | INT addConstant'''

    p[0] = p[1]

def p_cteS(p):
    '''cteS : STRING'''
    p[0] = p[1]

def p_exp(p):
    '''exp : term
    | term PLUS saveOperation exp
    | term MINUS saveOperation exp  '''   

def p_factoraux(p):
    '''factoraux : constant
    | PLUS constant
    | MINUS constant ''' 

    global pilaO
   
    operand = {}

    if len(p) == 2:
        operand = getOperand(p[1])
 
    else:
        operand = getOperand(p[2])
    
    pilaO.append(operand)
    typePila.append(typeOfVar)

def p_factor(p):
    '''factor : LFTPAREN addFakeBottom expression RGTPAREN removeFakeBottom factorEnded
    | factoraux factorEnded''' 

def p_expression(p):
    '''expression : exp 
    | exp expressionaux exp expressionEnded''' 
def p_expressionaux(p):
    '''expressionaux : AND saveOperation
    | DOUBEQUAL saveOperation
    | NOT saveOperation
    | OR saveOperation
    | LESSTHANEQUAL saveOperation
    | GREATTHANEQUAL saveOperation
    | GREATTHAN saveOperation
    | LESSTHAN saveOperation'''                         

def p_loop(p):
    '''loop : WHILE LFTPAREN expression RGTPAREN block ''' 

def p_write(p):
    '''write : PRINT LFTPAREN constant RGTPAREN SEMICOLON ''' 

def p_parameter(p):
    '''parameter : type ID codeAddParameters
    | type ID codeAddParameters COMMA parameter 
    | empty  '''   

def p_term(p):
    '''term : factor MULTIPLICATION saveOperation term
    | factor DIVISION saveOperation term 
    | factor termEnded ''' 

     

def p_statement(p):
    '''statement : assignment 
    | condition 
    | loop 
    | write 
    | read 
    | call  ''' 

def p_type(p):
    '''type : INT checkType 
    | FLOAT checkType
    | CHAR checkType
    | BOOL checkType
    | STRING checkType  ''' 

def p_main(p):
    '''main : PRIOMH codeScope block  ''' 


def p_function(p):
    '''function : FUNCTION codeScope functionaux ID codeNameOfFunct LFTPAREN parameter RGTPAREN blockreturn codeScope  '''
    
    global nameOfFunct
    global typeOfFunct
    global funcParameters
    global localVarDict  

    addFunctDict(nameOfFunct, typeOfFunct, funcParameters) #agrega el nombre, tipo y parametros al diccionario de funciones

    
    localVarDict.clear() #limpia el diccionario de variables locales para usarlo en otra funcion

    funcParameters = [] #limpia el arreglo de parametros para usarlo en otra funcion
  

def p_functionaux(p):
    '''functionaux : VOID codeTypeVoid checkType 
    | funcIndicator type  '''  

def p_vars(p):
    '''vars : type  varsaux     ''' 
def p_varsaux(p):
    '''varsaux : ID codeAddVar EQUAL expression SEMICOLON
    | ID codeAddVar EQUAL expression COMMA varsaux 
    | ID  codeAddVarArreglo LFTBRACSQR INT RGTBRACSQR  EQUAL arrayvalues SEMICOLON
    | ID codeAddVarArreglo LFTBRACSQR INT RGTBRACSQR   EQUAL arrayvalues COMMA varsaux '''


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


def p_codeScope(p):
    '''codeScope : '''

    global scopeVar

    if scopeVar == 'global': #cambia el scope de global a local o viceversa
        scopeVar = 'local'
    else:
        scopeVar = 'global'   


def p_checkType(p):
    '''checkType : '''

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
    

def p_funcIndicator(p):
    '''funcIndicator : '''

    global funcIndicator
    funcIndicator = True #la variable se cambia a true porque el tipo sera para una funcion no void













def p_addConstant(p):
    '''addConstant : empty'''
    constType = -1
    cte = num(p[-1])
    if type(cte) is int:
        constType = 0
    else:
        constType = 2
    global constants
    if not str(cte) in constants.keys():
        constants[str(cte)] = {'value':cte, 'type':constType}




def p_saveOperation(p):
    '''saveOperation : empty'''
    global popper
    popper.append(p[-1])



def p_addFakeBottom(p):
    '''addFakeBottom : empty'''
    global popper
    popper.append('(')



def p_removeFakeBottom(p):
    '''removeFakeBottom : empty'''
    global popper
    print(popper)
    popper.pop()




def p_termEnded(p):
    '''termEnded : empty'''
    global popper
    global pilaO
    if len(popper) > 0:
        if popper[-1] == '+' or popper[-1] == '-' or popper[-1] == '||':
            operand2 = pilaO.pop()
            operation = popper.pop()
            operand1 = pilaO.pop()

            resultType = checkSemanticCube( operand1['type'] ,operand2['type'] ,operation) 
            
            if resultType < 10:
                addQuadruple(operation, operand1, operand2, 0)

                typePila.append(resultType)

                pilaO.append({'value':0, 'type':resultType})

            else:
                print('Error: Type mismatch')
                exit(1)


def p_factorEnded(p):
    '''factorEnded : empty'''
    global popper
    global pilaO
    if len(popper) > 0:
        if popper[-1] == '*' or popper[-1] == '/' or popper[-1] == '&&':
            operand1 = pilaO.pop()
            operation = popper.pop()
            operand2 = pilaO.pop()
            
            resultType = checkSemanticCube( operand1['type'] ,operand2['type'] ,operation) 
          
            if resultType < 10:

                addQuadruple(operation, operand1, operand2, 0)
                
                typePila.append(resultType)
                
                pilaO.append({'value':0, 'type':resultType})
            else:
                print('Error: Type mismatch')
                exit(1)




def p_expressionEnded(p):
    '''expressionEnded : empty'''
    global popper
    global pilaO
    if len(popper) > 0:

        if popper[-1] == '<' or popper[-1] == '>' or popper[-1] == '<=' or popper[-1] == '>=' or popper[-1] == '==' or popper[-1] == '!=':
            operand1 = pilaO.pop()
            operation = popper.pop()
            operand2 = pilaO.pop()
           
            resultType = checkSemanticCube( operand1['type'] ,operand2['type'] ,operation)
            
            if resultType < 10:
                addQuadruple(operation, operand1, operand2, 0)

                typePila.append(resultType)
                
                pilaO.append({'value':0, 'type':resultType})

            else:
                print('Type mismatch')






yacc.yacc()





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





def getOperand(key):
    if key in constants.keys():
        return constants[key]
    elif key in localVarDict.keys():
        return localVarDict[key]
    elif key in globalVarDict.keys():
        return globalVarDict[key]




def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)






def addQuadruple(operation, var1, var2, result):
    global quadruples
    quadruples.append({'op':operation, 'var1':var1, 'var2':var2, 'result':result})





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
   






