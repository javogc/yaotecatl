
from cuboSemantico import *
from Yaotecatl import *
from Memory import *
import csv

def runVirtualMachine(quadruplesList,globalVarDir,localVarDir,constVarDir,tempVarDir,constantDict,localVarDict,globalVarDict):

	print ("Yaotecatl virtual machine RUNNING...")


	objMemoria = Memory('Memoria', globalVarDir, localVarDir, constVarDir, tempVarDir)
	objMemoria.SetConstants(constantDict)
	stackQuadBack = [] #arreglo que guardara el numero del quadruplo en el que regresara despues de la funcion
	quadCount = 0  #contador de quadruplos

	while quadruplesList[quadCount]['OPERATOR'] != "END":

		quad = quadruplesList[quadCount]
		operator = quad["OPERATOR"]
		op1 = quad['OP1']
		op2 = quad["OP2"]
		result = quad["RESULT"]

		print(operator, op1, op2, result)


		#Substaction
		if quad['OPERATOR'] == '-':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1) #saca el valor con la direccion dada
			
			op2Value = objMemoria.getVarValue(op2)

			

			lastResult = op1Value - op2Value #hace la operacion

			objMemoria.setVarValue(result, lastResult) #agrega el valor (lastresult) a la direccion (result)
			

		#addition	
		elif quad['OPERATOR'] == '+':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)

			op2Value = objMemoria.getVarValue(op2)

			lastResult = op1Value + op2Value

			objMemoria.setVarValue(result, lastResult)

		#multiplication
		elif quad['OPERATOR'] == '*':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)

			op2Value = objMemoria.getVarValue(op2)



			lastResult = op1Value * op2Value

			objMemoria.setVarValue(result, lastResult)

		#division	
		elif quad['OPERATOR'] == '/':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			print op1, "dir"
			op1Value = objMemoria.getVarValue(op1)
			print op1Value, "valor"

			op2Value = objMemoria.getVarValue(op2)


			lastResult = op1Value / op2Value

			objMemoria.setVarValue(result, lastResult)


		#equals	
		elif quad['OPERATOR'] == '=':
			op1 = quad['OP1'] #saca la direccion del valor que le asignaras a la variable
			result = quad['RESULT'] #saca la direccion de la variable
		
			op1Value = objMemoria.getVarValue(op1) #saca el valor que le asignaremos a la variable

			objMemoria.setVarValue(result, op1Value) #asigna el valor a la direccion de memoria de la variable


		#greaterthan
		elif quad['OPERATOR'] == '>':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)

			op2Value = objMemoria.getVarValue(op2)



			lastResult = op1Value > op2Value

			objMemoria.setVarValue(result, lastResult)

		#lessthan
		elif quad['OPERATOR'] == '<':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)

			op2Value = objMemoria.getVarValue(op2)



			lastResult = op1Value < op2Value

			objMemoria.setVarValue(result, lastResult)

		#greaterthanorequal	
		elif quad['OPERATOR'] == '>=':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)

			op2Value = objMemoria.getVarValue(op2)



			lastResult = op1Value >= op2Value

			objMemoria.setVarValue(result, lastResult)

		#lessthanorequal
		elif quad['OPERATOR'] == '<=':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)

			op2Value = objMemoria.getVarValue(op2)



			lastResult = op1Value <= op2Value

			objMemoria.setVarValue(result, lastResult)

		#	
		elif quad['OPERATOR'] == '==':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)

			op2Value = objMemoria.getVarValue(op2)



			lastResult = op1Value == op2Value

			objMemoria.setVarValue(result, lastResult)

		#different
		elif quad['OPERATOR'] == '!=':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)

			op2Value = objMemoria.getVarValue(op2)



			lastResult = op1Value != op2Value

			objMemoria.setVarValue(result, lastResult)

		#and
		elif quad['OPERATOR'] == '&&':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)

			op2Value = objMemoria.getVarValue(op2)



			lastResult = op1Value and op2Value

			objMemoria.setVarValue(result, lastResult)

		#or
		elif quad['OPERATOR'] == '||':
			op1 = quad['OP1']
			op2 = quad['OP2']
			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)

			op2Value = objMemoria.getVarValue(op2)



			lastResult = op1Value or op2Value

			objMemoria.setVarValue(result, lastResult)

		#print	
		elif quad['OPERATOR'] == 'PRINT':
			result = quad['RESULT']

			aux = objMemoria.getVarValue(result)

			print(aux)


		#read	
		#elif quad['OPERATOR'] == 'READ':
		#	result = quad['RESULT']

		#	op1Value = #objMemoria

			#readwithobjMemoria

		#era	
		elif quad['OPERATOR'] == 'ERA':
			result = quad['RESULT'] #saca la funcion a la cual ira

			objMemoria.newFunc(result) #la envia a la funcion para asignar la memoria correspondiente




		#param	
		elif quad['OPERATOR'] == 'PARAM':
			op1 = quad['OP1']
		
			result = quad['RESULT']

			

			op1Value = objMemoria.getVarValue(op1) #saca el valor de la direccion
			
			objMemoria.changeMemory() #cambia la memoria a la memoria de la funcion para asignar el valor de las dos lineas de codigo de abajo

			objMemoria.setVarValue(result, op1Value) #le asigna el valor al arreglo de la funcion

			objMemoria.changeBackMemory() #regresa a la memoria del main
			


		#gosub	
		elif quad['OPERATOR'] == 'GOSUB':
			result = quad['RESULT'] # es el numero del quadruplo al cual ira

			objMemoria.changeMemory() #cambia la memoria de main a la de la funcion

			stackQuadBack.append(quadCount + 1) #es el quadruplo al cual regresara despues de acabar la funcion haremos pop()

			quadCount = result - 1




		#return	
		elif quad['OPERATOR'] == 'RETURN':
			result = quad['RESULT']

			resultValue = objMemoria.getVarValue(result) #saca el valor de la direccion

			objMemoria.changeBackMemory()

			quadCount = stackQuadBack[-1]

			quad = quadruplesList[quadCount]

			resultAddress = quad['RESULT']

			objMemoria.setVarValue(resultAddress, resultValue)

		
		      


		#endproc
		elif quad['OPERATOR'] == 'ENDPROC':
			objMemoria.changeBackMemory()

			quadCount = stackQuadBack.pop() - 1
					



		#goto	
		elif quad['OPERATOR'] == 'GOTO':
			result = quad['RESULT']

			quadCount = result - 1


		#gotof	
		elif quad['OPERATOR'] == 'GOTOF':
			op1 = quad['OP1']

			result = quad['RESULT']

			op1Value = objMemoria.getVarValue(op1)


			if not op1Value:
				quadCount = result - 1



		#gotom	
		elif quad['OPERATOR'] == 'GOTOM':
			result = quad['RESULT']

			quadCount = result - 1

			#objMemoria
			


		#verify	
		#elif quad['OPERATOR'] == 'VERIFY':
		#	op1 = quad['OP1']
		#	result = quad['RESULT']

		#	op1Value = objMemoria.getVarValue(op1)
		#	resultValue = objMemoria.getVarValue(op1)
		#	print op1Value
		#	print resultValue
		#	if op1Value > resultValue:
		#		print("array index to big!")
		#		exit()



		quadCount += 1

