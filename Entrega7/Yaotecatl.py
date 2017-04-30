from cuboSemantico import *
from lex import *
import collections
from collections import OrderedDict
from collections import deque
from virtualMachine import *




#------------------------------Comienzo de Yacc --------------------------------------------

import ply.yacc as yacc


quadruplesList = [] #lista/arreglo que guardara un objeto diccionario que sera cada quadruplo

scopeVar = "global" #variable que cambiara entre local y global para crear las tablas

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

jumps = [] #pila de jumps
jumpsGoto = [] #pila de gotos final
callPointerDict = dict() #para saber en que parametro estas y comparar argumentos con parametros

isCall = False #var que dira si la asignacion a una variable es el resultado de una funcion          
counterCalls = 0 #cuantas funciones anidadas
newDir = 0 #guardara la direccion base del arreglo y despues le sumaremos + 1 para cada valor del arreglo
arrValues = [] #guardamos los valores del arreglo para comparar el tamano despues


globalVarDir = dict() #diccionario que tiene las direcciones de memoria globales
globalVarDir["bool"] = 10000
globalVarDir["int"] = 14000
globalVarDir["float"] = 18000
globalVarDir["string"] = 22000


localVarDir = dict() #diccionario que tiene las direcciones de memoria locales
localVarDir["bool"] = 26000
localVarDir["int"] = 30000
localVarDir["float"] = 34000
localVarDir["string"] = 38000


constVarDir = dict() #diccionario que tiene las direcciones de memoria constantes
constVarDir["bool"] = 42000
constVarDir["int"] = 46000
constVarDir["float"] = 50000
constVarDir["string"] = 54000


tempVarDir = dict() #diccionario que tiene las direcciones de memoria temporales
tempVarDir["bool"] = 58000
tempVarDir["int"] = 62000
tempVarDir["float"] = 66000
tempVarDir["string"] = 70000 











#-------------------------Reglas del compilador-----------------

def p_program(p):
    """program : PROGRAM ID LFTBRAC auxprogramvars codeGOTOMain auxprogramfunct main RGTBRAC"""

    #Pruebas de print para verificar que el codigo funcione bien
    #print("Table of Functions: %s" % funcDict)
    #print("------------------------------------")
    #print("------------------------------------")

    #print("Table of Global Variables: %s" % globalVarDict)
    #print("-------------------------------------")
    #print("------------------------------------")

    #print("Table of Local(main) Variables: %s" % localVarDict)
    #print("------------------------------------")
    #print("------------------------------------")
    addNewQuadruple("END", "", "", "")
    #para imprimir los cuadrulos uno por uno


    countQuadruples = 0 
    for p in quadruplesList:

        print "Quadruple:", countQuadruples
        
        print p
        print
        countQuadruples = countQuadruples + 1;

    
    #print(checkSemanticCube("int" ,"float" ,"+"))

#def p_auxprogram(p):
 #   """auxprogram : vars auxprogram 
  #  | function auxprogram 
   # | """

#cambiar esto de arriba por los 2 de abajo para poder declarar variables globales en medio

def p_auxprogramvars(p):
    """auxprogramvars : vars auxprogramvars 
    | empty """
def p_auxprogramfunct(p):
    """auxprogramfunct : function auxprogramfunct 
    | empty """      


def p_array(p):
    """array : ID codeAddOpenParen LFTBRACSQR exp RGTBRACSQR codeDeleteOpenParen"""

    global newDir

    findVar = dict() #buscara la variable

    if p[1] in globalVarDict.keys():
        findVar = globalVarDict[p[1]]
        findVar["scope"] = "global"
        

    elif p[1] in localVarDict.keys():
        findVar = localVarDict[p[1]]
        findVar["scope"] = "local"


    else:
        print("Variable not found!", p[1]) #imprime cual variable no fue declarada en ninguna de las tablas 
        exit()  




    indexArr = pilaO.pop()["dir"] #saca el tamano del arreglo

    addNewQuadruple("VERIFY", indexArr, "", findVar["arrSize"]) #verifica que el index sea menor que el max del arreglo

    auxDir = findVar["dir"]


    if not constantDict.has_key(str(auxDir)):
        constantDict[str(auxDir)] = {"val":auxDir, "type":0, "dir": constVarDir["int"] } #arreglo la direccion base del arreglo 
        constVarDir["int"] += 1


    specialDir = "(" + str(tempVarDir[listOfTypesReversed(findVar["type"])]) + ")" #direccion especial

    addNewQuadruple("+",indexArr, constantDict[str(auxDir)]["dir"], specialDir  ) # sumas la base por el index que buscas


    pilaO.append({"dir":specialDir, "type":findVar["type"]}) #metes la direccion especial a la pilaO

    
    tempVarDir[listOfTypesReversed(findVar["type"])] += 1

   
    p[0] = p[1]




def p_arrayvals(p):
    """arrayvals : LFTBRACSQR arrayvalsaux RGTBRACSQR """

def p_arrayvalsaux(p):
    """arrayvalsaux : cteNcteS codeAddValueArray 
    | cteNcteS codeAddValueArray COMMA arrayvalsaux """        

def p_cteNcteS(p):
    """cteNcteS : cteN  
    | cteS"""   

    p[0] = p[1]




def p_assignment(p):
    """assignment : assignmentaux EQUAL expression SEMICOLON"""    

    if p[3] == 4:
        print("can't use a void function for an assignment!")
        exit()

    # va a buscar que la variable que quieres cambiarle el valor si exista
    findVar = dict()

    if p[1] in globalVarDict.keys():
        findVar = globalVarDict[p[1]]
        

    elif p[1] in localVarDict.keys():
        findVar = localVarDict[p[1]]
        
    else:
       
        print("Variable not found!", p[1]) #imprime cual variable no fue declarada en ninguna de las tablas 
        exit()
        
    assignVar = pilaO.pop() #saca la variable que tiene la respuesta final para ser asignada despues 

    newType = checkSemanticCube( findVar["type"] ,assignVar["type"] ,"=") #checar si los 2 operandos que sacaste son compatibles con el operador
  
    if newType < 10: # si si son compatibles los argrega al quadruplo
        if findVar["type"] < 20:
            addNewQuadruple("=", assignVar["dir"], "", findVar["dir"])
        else:
            addNewQuadruple("=", assignVar["dir"], "", pilaO.pop()["dir"])   

    else: #Si no son compatibles marca error
            print("You cant evaluate those operands with that operator!" + findVar["val"] )
            exit()



def p_assignmentaux(p):
    """assignmentaux : ID 
    | array"""  
    p[0] = p [1]



def p_blockreturn(p):
    """blockreturn : LFTBRAC blockneutral RGTBRAC 
    | LFTBRAC blockneutral RETURN exp codeReturnQuad SEMICOLON RGTBRAC """ 
def p_blockneutral(p):
    """blockneutral : statement blockneutral 
    | vars blockneutral
    | empty """ 
def p_block(p):
    """block : LFTBRAC blockneutral RGTBRAC"""       

def p_condition(p):
    """condition : IF conditionaux codeEndIf
    | IF conditionaux ELSE codeElse block  codeEndIf""" 
def p_conditionaux(p):
    """conditionaux : LFTPAREN expression RGTPAREN codeGOTOF block codeGotoElseIf conditionaux2 """      
def p_conditionaux2(p):
    """conditionaux2 : codeNextIf ELSEIF conditionaux
    | empty """ 


def p_constant(p):
    """constant : ID 
    | array 
    | cteN
    | cteS
    | TRUE codeAddConstBool
    | FALSE codeAddConstBool
    | call codeIsCalll """

    
    p[0] = p[1]    

 

def p_cteN(p):
    """cteN : FLOAT codeAddConstNumber
    | INT codeAddConstNumber"""

    p[0] = p[1]

def p_cteS(p):
    """cteS : STRING codeAddConstString"""
    p[0] = p[1]


def p_exp(p):
    """exp : term
    | term PLUS codeAddOperator exp
    | term MINUS codeAddOperator exp  """   

def p_factoraux(p):
    """factoraux : constant
    | PLUS constant
    | MINUS constant """ 

    global pilaO
    global isCall



    if not isCall:
        if len(p) == 2: #si la longitud de la regla es de 2 entonces busca el operando en todas las tablas que esta en la posicion p[1]
            aux = searchForOperand(p[1]) 
            
            if aux["type"] < 20:
                pilaO.append(aux)
        
          
 
        else:   #si la longitud de la regla es de 2 entonces busca el operando en todas las tablas que esta en la posicion p[2]
            aux = searchForOperand(p[1]) 
            
            if aux["type"] < 20:
                pilaO.append(aux)

             
    
        
    else: 
        isCall = False
  
       
       
          
    
    
    

def p_factor(p):
    """factor : LFTPAREN codeAddOpenParen expression RGTPAREN codeDeleteOpenParen codeAskFactor
    | factoraux codeAskFactor""" 

def p_expression(p):
    """expression : exp 
    | exp expressionaux codeAddOperator exp codeAskExpression""" 
def p_expressionaux(p):
    """expressionaux : AND 
    | DOUBEQUAL 
    | NOT 
    | OR 
    | LESSTHANEQUAL 
    | GREATTHANEQUAL 
    | GREATTHAN 
    | LESSTHAN """   

    p[0] = p[1]                       

def p_loop(p):
    """loop : WHILE codeWhileCondition LFTPAREN expression RGTPAREN codeGOTOF block codeGOTOWhile """ 

def p_write(p):
    """write : PRINT LFTPAREN constant RGTPAREN SEMICOLON """ 
    
    findVar = dict() #variable que recibira la Var al ser encontrada en las tablas

    if p[3] in globalVarDict.keys():
        findVar = globalVarDict[p[3]]
        if findVar["type"] < 20:
            addNewQuadruple("PRINT", "", "", findVar["dir"]) 
        else:
            addNewQuadruple("PRINT", "", "", pilaO.pop()["dir"]) 
        

    elif p[3] in localVarDict.keys():
        findVar = localVarDict[p[3]]
        if findVar["type"] < 20:
            addNewQuadruple("PRINT", "", "", findVar["dir"]) 
        else:
            addNewQuadruple("PRINT", "", "", pilaO.pop()["dir"]) 

    elif p[3] in constantDict.keys():
        findVar = constantDict[p[3]]
        if findVar["type"] < 20:
            addNewQuadruple("PRINT", "", "", findVar["dir"]) 
        else:
            addNewQuadruple("PRINT", "", "", pilaO.pop()["dir"])    
    
    else:
        print("Variable not found!", p[3]) #imprime cual variable no fue declarada en ninguna de las tablas 
        exit()
    
    

def p_parameter(p):
    """parameter : type codeCheckType ID codeAddParameters
    | type codeCheckType ID codeAddParameters COMMA parameter 
    | empty  """   

def p_term(p):
    """term : factor MULTIPLICATION codeAddOperator term
    | factor DIVISION codeAddOperator term 
    | factor codeAskTerm """ 

     

def p_statement(p):
    """statement : assignment 
    | condition 
    | loop 
    | write 
    | read 
    | call SEMICOLON """ 

def p_type(p):
    """type : INT  
    | FLOAT 
    | CHAR 
    | BOOL 
    | STRING   """ 

    p[0] = p[1]

def p_main(p):
    """main : codeLocationMain PRIOMH codeScope block  """ 


def p_function(p):
    """function : FUNCTION codeScope functionaux ID codeNameOfFunct LFTPAREN parameter RGTPAREN codeAddFunctQuad blockreturn codeScope  """

    #print("Table of Local(funct) Variables: %s" % localVarDict)
    #print("Table of Local(function) Variables: %s" % localVarDict)

    global localVarDir
    global tempVarDir
    global functParameters
    global funcDict

    #metemos la cantidad de variables a la tabla de funciones
    funcDict[nameOfFunct]["localBool"] = localVarDir["bool"]
    funcDict[nameOfFunct]["localInt"] = localVarDir["int"]
    funcDict[nameOfFunct]["localFloat"] = localVarDir["float"]
    funcDict[nameOfFunct]["localString"] = localVarDir["string"]

    funcDict[nameOfFunct]["tempBool"] = tempVarDir["bool"]
    funcDict[nameOfFunct]["tempInt"] = tempVarDir["int"]
    funcDict[nameOfFunct]["tempFloat"] = tempVarDir["float"]
    funcDict[nameOfFunct]["tempString"] = tempVarDir["string"]

    

    localVarDict.clear() #limpia el diccionario de variables locales para usarlo en otra funcion


    funcParameters = [] #limpia el arreglo de parametros para usarlo en otra funcion

    #reseteamos la direccion inicial
    localVarDir["bool"] = 26000
    localVarDir["int"] = 30000
    localVarDir["float"] = 34000
    localVarDir["string"] = 38000

    tempVarDir["bool"] = 58000
    tempVarDir["int"] = 62000
    tempVarDir["float"] = 66000
    tempVarDir["string"] = 70000 
    
    addNewQuadruple("ENDPROC", "", "", "")

def p_functionaux(p):
    """functionaux : VOID codeTypeVoid codeCheckType 
    | codeFuncIndicator type codeCheckType """  

def p_vars(p):
    """vars : type codeCheckType varsaux     """ 

def p_varsaux2(p):
    """varsaux2 : COMMA varsaux 
    |  SEMICOLON  """ 

def p_varsaux(p):
    """varsaux : ID codeAddVar EQUAL expression varsaux2 
    | ID  codeAddVarArreglo LFTBRACSQR INT RGTBRACSQR EQUAL arrayvals varsaux2 """

    global globalVarDict

    global scopeVar

    global localVarDict


    if p[4] == 4: # el 4 es expression y si la expression es call y es una funcion void saldra error
            print("can't use a void function for an assignment!")
            exit()


    findVar = dict() #buscara la variable

    if p[1] in globalVarDict.keys():
        findVar = globalVarDict[p[1]]
        findVar["scope"] = "global"
        

    elif p[1] in localVarDict.keys():
        findVar = localVarDict[p[1]]
        findVar["scope"] = "local"


    else:
        print("Variable not found!", p[1]) #imprime cual variable no fue declarada en ninguna de las tablas 
        exit()  


    if len(p) > 7: # si la regla es el arreglo
        arrSize = int(p[4])

        if scopeVar == "global":
            globalVarDir[listOfTypesReversed(globalVarDict[nameOfVar]["type"])] += arrSize - 1 #le sumara el size del arreglo a la memoria global

            globalVarDict[nameOfVar]["arrSize"] = arrSize

        else:
            localVarDir[listOfTypesReversed(localVarDict[nameOfVar]["type"])] += arrSize - 1 #le sumara el size del arreglo a la memoria local


            localVarDict[nameOfVar]["arrSize"] = arrSize


        
        if findVar["arrSize"] == len(arrValues):   # que el size del arreglo sea igual a la de sus asignaciones [1,2,3]
            savedDir = findVar["dir"] #guarda la direccion actual del arreglo a la que le asignaremos valores para ir sumandole uno a la direccion por cada valor

            for i in range(0, findVar["arrSize"]):
                arrValAux = arrValues.pop(0)
       
                checktype = checkSemanticCube( findVar["type"] ,constantDict[arrValAux]["type"] ,"=") #checar si los 2 operandos que sacaste son compatibles con el operador
                
                if checktype >= 10:
                    print("array value types don't match!")
                    exit()

            
                addNewQuadruple("=", constantDict[arrValAux]["dir"], "", savedDir) #se le asigna el valor a la direccion actual del arreglo
                
                savedDir += 1 #le suma 1 a la direccion para asiganrle el siguiente valor
        else:
            print("Error: Array size doesn't match!")  
            print(findVar["arrSize"], len(arrValues)) 
            exit()     

    else:          

        assignVar = pilaO.pop() #saca la variable que tiene la respuesta final para ser asignada despues 

        newType = checkSemanticCube( findVar["type"] ,assignVar["type"] ,"=") #checar si los 2 operandos que sacaste son compatibles con el operador
      
        if newType < 10: # si si son compatibles los argrega al quadruplo
            

            addNewQuadruple("=", assignVar["dir"], "", findVar["dir"])

        else: #Si no son compatibles marca error
                print("You cant evaluate those operands with that operator!" + findVar["val"] )
                exit()    


def p_callaux(p):
    """callaux : codeMovePointer COMMA exp codeAddArguments callaux
    | empty """ 

def p_call(p):
    """call : ID codeVerifyFunct LFTPAREN codeAddOpenParen codeEraQuad exp codeAddArguments callaux codeDeleteOpenParen RGTPAREN codeVerifyNull codeGOSUB codeTempReturn  """ 
    p[0] = funcDict[p[1]]["type"]




def p_read(p):
    """read : READ LFTPAREN readaux RGTPAREN SEMICOLON """   

    findVar = dict() #variable que recibira la Var al ser encontrada en las tablas

    if p[3] in globalVarDict.keys():
        findVar = globalVarDict[p[3]]
        addNewQuadruple("READ", "", "", findVar["dir"]) 

    elif p[3] in localVarDict.keys():
        findVar = localVarDict[p[3]]
        addNewQuadruple("READ", "", "", findVar["dir"]) 

    elif p[3] in constantDict.keys():
        findVar = constantDict[p[3]]
        addNewQuadruple("READ", "", "", findVar["dir"])    
    
    else:
        print("Variable not found!", p[3]) #imprime cual variable no fue declarada en ninguna de las tablas 
        exit()



def p_readaux(p):
    """readaux : ID
    | array """    

    p[0] = p[1]                              

def p_empty(p):
    """empty : """
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p)
        exit()
    else:
        print("Syntax error at EOF")
        exit()




#-------------------------------------------------- OTHER RULES -------------------------------------

#codigo para el brinco del else si un IF ya entro 
def p_codeGotoElseIf(p):
    """codeGotoElseIf : """
    addNewQuadruple("GOTO", "", "", "")
    jumpsGoto.append(len(quadruplesList)-1)


#codigo para agregar valor del arreglo al arreglo creado llamado arrayValues y despues usarlo para asignar a cada valor del array
def p_codeAddValueArray(p):
    '''codeAddValueArray : empty'''
    global arrValues

    arrValues.append(p[-1])



#codigo para asignar una variable temporal el return de la funcion
def p_codeTempReturn(p):
    '''codeTempReturn : empty'''
    global nameOfFunct
    nameOfFunct = p[-12]

    if funcDict[nameOfFunct]["type"] != 4:

        respAux = {"dir": tempVarDir[listOfTypesReversed(funcDict[nameOfFunct]["type"])], "type":funcDict[nameOfFunct]["type"]}

        addNewQuadruple("=", "" , "", respAux["dir"])

        pilaO.append(respAux)


        tempVarDir[listOfTypesReversed(funcDict[nameOfFunct]["type"])] += 1



#para saber que es una funcion
def p_codeIsCalll(p):
    '''codeIsCalll : empty'''
    global isCall
    isCall = True


def p_codeGOSUB(p):
    '''codeGOSUB : empty'''
    global counterCalls

    counterCalls -= 1
    addNewQuadruple("GOSUB", "", "", int(funcDict[p[-11]]["Quadruple"])) # saca donde esta ubicada la funcion 

#checa si es pusiste menos argumentos
def p_codeVerifyNull(p):
    '''codeVerifyNull : empty'''
    global callPointerDict
    global counterCalls
    if callPointerDict[counterCalls]["pointer"] + 1 != len(funcDict[callPointerDict[counterCalls]["func"]]["parameters"]):
        print("Number of parameters is incorrect")
        exit()
        
#checa si es pusiste de mas argumentos
def p_codeVerifyNull2(p):
    '''codeVerifyNull2 : empty'''
    global counterCalls
    global callPointerDict   
    if callPointerDict[counterCalls]["pointer"] == len(funcDict[callPointerDict[counterCalls]["func"]]["parameters"]):
        print("Number of parameters is incorrect")
        exit()
    
#mueve el pointer para comparar arg con param
def p_codeMovePointer(p):
    '''codeMovePointer : empty'''
    global counterCalls
    global callPointerDict
    callPointerDict[counterCalls]["pointer"] += 1 #le suma uno al counter de la funcion actual que es definida por el counterCalls

#Agrega quad PARAM
def p_codeAddArguments(p):
    '''codeAddArguments : empty'''
    global nameOfFunct
    global counterCalls
    global callPointerDict

    argument = pilaO.pop()

    p_codeVerifyNull2(p)

    newType = checkSemanticCube( argument["type"] ,funcDict[callPointerDict[counterCalls]["func"]]["parameters"][callPointerDict[counterCalls]["pointer"]]["type"] ,"=") #checar si los 2 operandos que sacaste son compatibles con el operador
            
    if newType < 10: # si si son compatibles los argrega al quadruplo
                
        addNewQuadruple("PARAM", argument["dir"], "", funcDict[callPointerDict[counterCalls]["func"]]["parameters"][callPointerDict[counterCalls]["pointer"]]["dir"]) #usando el pinter sacamos el parametro que recibira el argumento

    else: #Si no son compatibles marca error
    
        print("You cant evaluate those operands with that operator!" )
        exit()


#genera el quad de ERA
def p_codeEraQuad(p):
    '''codeEraQuad : empty'''
    global counterCalls
    global callPointerDict

    addNewQuadruple("ERA", "", "", funcDict[p[-4]])

    callPointerDict[counterCalls]["pointer"] = 0



#checa que exista la funcion
def p_codeVerifyFunct(p):
    '''codeVerifyFunct : empty'''
    global callPointerDict
    global nameOfFunct
    global counterCalls




    counterCalls += 1

    nameOfFunct = p[-1]
    if not p[-1] in funcDict.keys():
        print("That function you are trying to call doesnt't exist:", p[-1])
        exit()
    else:
        callPointerDict[counterCalls] = {"pointer":0, "func": p[-1]}

     
        

def p_codeReturnQuad(p):
    """codeReturnQuad : """
    varRespuesta = pilaO.pop() #saca lo ultimo metido a la pila que fue lo que se regresara
    if varRespuesta["type"] != funcDict[nameOfFunct]["type"]: #si el tipo del return value NO es igual que el tipo de la funcion marca error
        print("Type of funct is not the same as the type of the return value!")
        exit()
    else:
        addNewQuadruple("RETURN", "", "", varRespuesta["dir"])
        
        
      
        
#agrega la funcion con el numero de quadruplo en que esta para poder regresar aqui en el GOSUB
def p_codeAddFunctQuad(p):
    """codeAddFunctQuad : """

    global nameOfFunct
    global typeOfFunct
    global funcParameters
    global localVarDict  
   
    addFunctDict(nameOfFunct, typeOfFunct, funcParameters, len(quadruplesList)) #agrega el nombre, tipo y parametros al diccionario de funciones
    funcParameters = []



#Es en donde el GOTOM brincara para empezar en el main
def p_codeLocationMain(p):
    """codeLocationMain : """
    quadruplesList[jumps.pop()]["RESULT"] = len(quadruplesList) 

#codigo que falta completar que hara el brinco hasta main
def p_codeGOTOMain(p):
    """codeGOTOMain : """
    addNewQuadruple("GOTOM", "", "", "")
    
    jumps.append(len(quadruplesList)-1)


#codigo para el brinco del else si un IF ya entro 
def p_codeElse(p):
    """codeElse : """
    quadruplesList[jumps.pop()]["RESULT"] = len(quadruplesList)
    jumps.append(len(quadruplesList)-1)

#codigo para 
def p_codeEndIf(p):
    """codeEndIf : """
    quadruplesList[jumps.pop()]["RESULT"] = len(quadruplesList)

    while len(jumpsGoto) != 0:
        quadruplesList[jumpsGoto.pop()]["RESULT"] = len(quadruplesList)

#codigo para completar el GOTOF cuando hay elseif 
def p_codeNextIf(p):
    """codeNextIf : """
    quadruplesList[jumps.pop()]["RESULT"] = len(quadruplesList)


#codigo para crear el GOTOF y meter a la pila de jumps para despues completarlos
def p_codeGOTOF(p):
    """codeGOTOF : """
    respGotof = pilaO.pop() #Saca el ultimo valor de la pilaO que es una variable BOOL (en teoria) 

    if respGotof["type"] == 3: #checa si el tipo de la variable es BOOL

        addNewQuadruple("GOTOF", respGotof["dir"], "", "")
        jumps.append(len(quadruplesList)-1)

    else:
        print("Cant compare result, answer is not 'BOOL' type!")
        exit()


#codigo del GOTO de while para regresar al principio del while
def p_codeGOTOWhile(p):
    """codeGOTOWhile : """
    quadruplesList[jumps.pop()]["RESULT"] = len(quadruplesList) + 1
    addNewQuadruple("GOTO", "", "", jumps.pop())
    

#meto a la pila de jumps el lugar donde va a regresar el GOTO de el while
def p_codeWhileCondition(p):
    """codeWhileCondition : """

    jumps.append(len(quadruplesList)) #inserta el numero de quadruplo que va para poder saber a donde regresar (hacer el loop)


def p_codeScope(p):
    """codeScope : """

    global scopeVar

    if scopeVar == "global": #cambia el scope de global a local o viceversa
        scopeVar = "local"
    else:
        scopeVar = "global"   


def p_codeCheckType(p):
    """codeCheckType : """

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
    """codeAddVar : """

    global nameOfVar

    nameOfVar = p[-1] # p[-1] saca el ultimo valor que en este caso era el ID

    AddVarDict(nameOfVar, typeOfVar) #llama la funcion para agregar la variable al diccionario local o global

def p_codeAddVarArreglo(p):
    """codeAddVarArreglo : """

    global nameOfVar

    nameOfVar = p[-1]
    
    AddVarDict(nameOfVar, (typeOfVar + 100))    #llama la funcion para agregar la variable al diccionario y le suma 100 al tipo ya que es un arreglo 


def p_codeAddParameters(p):
    """codeAddParameters : """

    global nameOfVar
    global typeOfVar
    global funcParameters

    nameOfVar = p[-1] #saca el ID
    
    AddVarDict(nameOfVar, typeOfVar) #agrega el ID y tipo al diccionary que sera local, puesto que todos los parametros van local

    #arreglo que contiene valores sacados del diccionario
    funcParameters.append(localVarDict[nameOfVar]) #saca del diccionario local con la key que es el nombre de la variable y la agrega al arreglo de parametros

def p_codeNameOfFunct(p):
    """codeNameOfFunct : """

    global nameOfFunct

    nameOfFunct = p[-1] #la guarda el ID de la funcion para alrato cuando acabe de declarar sus parametros guarde todo junto


def p_codeTypeVoid(p):
    """codeTypeVoid : """

    global codeTypeVoid
    codeTypeVoid = True #la variable se cambia a true porque el tipo sera para una funcion void
    

def p_codeFuncIndicator(p):
    """codeFuncIndicator : """

    global funcIndicator
    funcIndicator = True #la variable se cambia a true porque el tipo sera para una funcion no void


def p_codeDeleteOpenParen(p): # Se acabo de hacer lo de adentro del parentesis
    """codeDeleteOpenParen : empty"""
    global popper
   
    popper.pop()




def p_codeAddOpenParen(p): #abre parentesis en una operacion
    """codeAddOpenParen : empty"""
    global popper
    
    popper.append("(")


def p_codeAddConstBool(p): #agrega una constante bool al diccionario de constantes
    """codeAddConstBool : empty"""
    if not constantDict.has_key(p[-1]):
        constantDict[p[-1]] = {"val": p[-1], "type":3, "dir": constVarDir["bool"]  }

        constVarDir["bool"] += 1

def p_codeAddConstString(p): #agrega una constante string al diccionario de constantes
    """codeAddConstString : empty"""
    if not constantDict.has_key(p[-1]):
        constantDict[p[-1]] = {"val": p[-1], "type":2, "dir": constVarDir["string"] }

        constVarDir["string"] += 1

def p_codeAddConstNumber(p): #agrega una constante ya sea int o double al diccionario de constantes
    """codeAddConstNumber : empty"""

    global constantDict

    if isInt(p[-1]):
        typeOfConst = 0
        if not constantDict.has_key(str(p[-1])):
            constantDict[str(p[-1])] = {"val":int(p[-1]), "type":typeOfConst, "dir": constVarDir["int"] }
            constVarDir["int"] += 1
    else:
        typeOfConst = 1
        if not constantDict.has_key(str(p[-1])):
            constantDict[str(p[-1])] = {"val":float(p[-1]), "type":typeOfConst, "dir": constVarDir["float"] }
            constVarDir["float"] += 1
    
    




def p_codeAddOperator(p): #agrega un operador al popper
    """codeAddOperator : empty"""
    global popper

    popper.append(p[-1])



def p_codeAskTerm(p):
    """codeAskTerm : empty"""
    global popper
    global pilaO

    if len(popper) > 0: #checa si el popper tiene algo dentro

        if popper[-1] == "-" or popper[-1] == "+": #si el siguiente character es un + o - hacer pop al popper y dos veces a la pilaO

            op2 = pilaO.pop()
            op1 = pilaO.pop()
            operator = popper.pop()

            newType = checkSemanticCube( op1["type"] ,op2["type"] ,operator) #checar si los 2 operandos que sacaste son compatibles con el operador
            
            if newType < 10: # si si son compatibles los argrega al quadruplo
                
                respAux = {"dir":tempVarDir[listOfTypesReversed(newType)], "type":newType}

                addNewQuadruple(operator, op1["dir"], op2["dir"], respAux["dir"])
              
                pilaO.append(respAux) #la respuesta es agregada a la pilaO con su nuevo tipo
                tempVarDir[listOfTypesReversed(newType)] += 1

            else: #Si no son compatibles marca error
                print("You cant evaluate those operands with that operator!")
                exit()


def p_codeAskFactor(p):
    """codeAskFactor : empty"""
    global popper
    global pilaO

    if len(popper) > 0: #checa si el popper tiene algo dentro

        if popper[-1] == "*" or popper[-1] == "/": #si el siguiente character es un + o - hacer pop al popper y dos veces a la pilaO

            op2 = pilaO.pop()
            op1 = pilaO.pop()
            operator = popper.pop()

            newType = checkSemanticCube( op1["type"] ,op2["type"] ,operator) #checar si los 2 operandos que sacaste son compatibles con el operador
            
            if newType < 10: # si si son compatibles los argrega al quadruplo
                respAux = {"dir":tempVarDir[listOfTypesReversed(newType)], "type":newType}

                addNewQuadruple(operator, op1["dir"], op2["dir"], respAux["dir"])
              
                pilaO.append(respAux) #la respuesta es agregada a la pilaO con su nuevo tipo
                tempVarDir[listOfTypesReversed(newType)] += 1
            else: #Si no son compatibles marca error
                print("You cant evaluate those operands with that operator!")
                exit()




def p_codeAskExpression(p):
    """codeAskExpression : empty"""
    global popper
    global pilaO

    if len(popper) > 0:

        if popper[-1] == "<" or popper[-1] == ">" or popper[-1] == "<=" or popper[-1] == ">=" or popper[-1] == "==" or popper[-1] == "!=" or popper[-1] == "||" or popper[-1] == "&&":

            op2 = pilaO.pop()
            op1 = pilaO.pop()
            operator = popper.pop()

            newType = checkSemanticCube( op1["type"] ,op2["type"] ,operator) #checar si los 2 operandos que sacaste son compatibles con el operador
            
            if newType < 10: # si si son compatibles los argrega al quadruplo

                respAux = {"dir":tempVarDir[listOfTypesReversed(newType)], "type":newType}

                addNewQuadruple(operator, op1["dir"], op2["dir"], respAux["dir"])
              
                pilaO.append(respAux) #la respuesta es agregada a la pilaO con su nuevo tipo
                tempVarDir[listOfTypesReversed(newType)] += 1

            else: #Si no son compatibles marca error
                print("You cant evaluate those operands with that operator!")
                exit()






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
        return "int"
    elif auxType == 101:
        return "float" 
    elif auxType == 102:
        return "string"            
    elif auxType == 103:
        return "bool"





def addFunctDict(functName, functType, functParameters, numOfQuadruple):
    
    global funcDict

    if functName in funcDict.keys():   #verifica si la funcion ya existe en el diccionario
        print ("Error in function table, the function already exists! ")
        
    else:
        funcDict[functName] = {"val":functName, "type":functType, "parameters":functParameters, "Quadruple": numOfQuadruple } #guarda la funcion en el diccionario
        
        if functType != 4:
            funcDict[functName]["dir"] = globalVarDir[listOfTypesReversed(functType)]
            globalVarDir[listOfTypesReversed(functType)] += 1

def AddVarDict(varName, varType): 
    global scopeVar
    global globalVarDict
    global localVarDict

    if scopeVar == "global":    # verifica si es global el scope actual para saber si guardarla in el diccionario global o local
        if varName in globalVarDict.keys(): # si ya existe la variable en el diccionario mostrarle un error
            print("Error in global table, variable already exists!")

        else:
            globalVarDict[varName] = {"val":varName, "type":varType, "dir": globalVarDir[listOfTypesReversed(varType)] }  # si no existe agregarla al diccionario
            globalVarDir[listOfTypesReversed(varType)] += 1


    else:       #hacer lo mismo que en global pero en local
        if not varName in localVarDict.keys():
            localVarDict[varName] = {"val":varName, "type":varType, "dir": localVarDir[listOfTypesReversed(varType)] }
            localVarDir[listOfTypesReversed(varType)] += 1

        else:
            print("Error in local table, variable already exists!")
            exit()



#Busca la variable o constante de todas las tablas/diccionarios y regresa un objeto diccionario
def searchForOperand(key):
    if key in globalVarDict.keys():
        return globalVarDict[key]

    elif key in localVarDict.keys():
        return localVarDict[key]

    elif key in constantDict.keys():
        return constantDict[key]    
    
    else:
        #sale error aqui
        print("Variable not found!", key) #imprime cual variable no fue declarada en ninguna de las tablas 
        exit()








#crea un nuevo cuadruple utilizando un diccionario y lo agrega a la lista/arreglo de quadruples
def addNewQuadruple(operator, op1, op2, result):
    global quadruplesList
    notOrderDict = OrderedDict() #para orderar el quadruplo como lo escribo
    notOrderDict = {"OPERATOR":operator, "OP1":op1, "OP2":op2, "RESULT":result }
    orderDict = notOrderDict.copy()
    quadruplesList.append(orderDict)


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        file = sys.argv[1]
        try:
            f = open(file, "r")
            data = f.read()
            yacc.parse(data, tracking = True) 
            runVirtualMachine(quadruplesList, globalVarDir, localVarDir, constVarDir, tempVarDir, constantDict,localVarDict, globalVarDict)
        except EOFError:
            print(EOFError)
            exit()
   











