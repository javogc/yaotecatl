from Yaotecatl import *
from virtualMachine import *
from cuboSemantico import *

#las direcciones iniciales de cada variable y scope
inicialGlobalVarDirBool = 10000
inicialGlobalVarDirInt = 14000
inicialGlobalVarDirFloat = 18000
inicialGlobalVarDirString = 22000


initialLocalVarDirBool  = 26000
initialLocalVarDirInt  = 30000
initialLocalVarDirFloat  = 34000
initialLocalVarDirString = 38000


initialConstVarDirBool = 42000
initialConstVarDirInt = 46000
initialConstVarDirFloat  = 50000
initialConstVarDirString = 54000


initialTempVarDirBool = 58000
initialTempVarDirInt = 62000
initialTempVarDirFloat = 66000
initialTempVarDirString = 70000 

class Memory:

	def __init__(self, name, globalVarDir, localVarDir, constVarDir, tempVarDir):
		self.name = name
		
		
		#para tener mejor eficiencia creamos arreglo con la cantidad de memoria necesitada
		self.finalGlobalVarDirBool = range(globalVarDir["bool"] - inicialGlobalVarDirBool) 
		self.finalGlobalVarDirInt  = range(globalVarDir["int"] - inicialGlobalVarDirInt)
		self.finalGlobalVarDirFloat = range(globalVarDir["float"] - inicialGlobalVarDirFloat)
		self.finalGlobalVarDirString = range(globalVarDir["string"] - inicialGlobalVarDirString)

		self.finalLocalVarDirBool = range(localVarDir["bool"] - initialLocalVarDirBool)
		self.finalLocalVarDirInt = range(localVarDir["int"] - initialLocalVarDirInt)
		self.finalLocalVarDirFloat = range(localVarDir["float"] - initialLocalVarDirFloat)
		self.finalLocalVarDirString = range(localVarDir["string"] - initialLocalVarDirString)

		self.finalConstVarDirBool = range(constVarDir["bool"] - initialConstVarDirBool)
		self.finalConstVarDirInt = range(constVarDir["int"] - initialConstVarDirInt)
		self.finalConstVarDirFloat = range(constVarDir["float"] - initialConstVarDirFloat)
		self.finalConstVarDirString = range(constVarDir["string"] - initialConstVarDirString)

		self.finalTempVarDirBool = range(tempVarDir["bool"] - initialTempVarDirBool)
		self.finalTempVarDirInt = range(tempVarDir["int"] - initialTempVarDirInt)
		self.finalTempVarDirFloat = range(tempVarDir["float"] - initialTempVarDirFloat)
		self.finalTempVarDirString = range(tempVarDir["string"] - initialTempVarDirString)     


		self.memoriesStack = []

	#sacamos de la tabla de constantes unicamente los valores y se lo agregamos al arreglo de valores de constantes en la posicion correspondiente
	def SetConstants(self, constantDict):
		for key, val in constantDict.items():
			if val['type'] == 0:
				self.finalConstVarDirInt[val['dir'] - initialConstVarDirInt] = val['val']
			elif val['type'] == 1:
				self.finalConstVarDirFloat[val['dir'] - initialConstVarDirFloat] = val['val']
			elif val['type'] == 2:
				self.finalConstVarDirString[val['dir'] - initialConstVarDirString] = val['val']
			elif val['type'] == 3:
				self.finalConstVarDirBool[val['dir'] - initialConstVarDirBool] = val['val']	
						
			
	#Saca el valor 			
	def getVarValue(self, dirVar):
			if type(dirVar) is str:
				dirVar = dirVar.replace("(", "")
				dirVar = dirVar.replace(")", "") 
				dirVar = self.getVarValue(int(dirVar))
				dirVar = self.getVarValue(dirVar)
				return dirVar



			scope = getVarScope(dirVar)
			typeOfVarAux = getVarType(dirVar)

			if scope == "global":

				if typeOfVarAux == "bool":
					answer = self.finalGlobalVarDirBool[dirVar - inicialGlobalVarDirBool] #resta la direccion con la direccion inicial para sacar el valor correcto

				elif typeOfVarAux == "int":
					answer = self.finalGlobalVarDirInt[dirVar - inicialGlobalVarDirInt]

				elif typeOfVarAux == "float":
					answer = self.finalGlobalVarDirFloat[dirVar - inicialGlobalVarDirFloat]

				elif typeOfVarAux == "string":
					answer = self.finalGlobalVarDirString[dirVar - inicialGlobalVarDirString]
			
		 
			elif scope == "local":

				if typeOfVarAux == "bool":
					answer = self.finalLocalVarDirBool[dirVar - initialLocalVarDirBool] #resta la direccion con la direccion inicial para sacar el valor correcto

				elif typeOfVarAux == "int":
					answer = self.finalLocalVarDirInt[dirVar - initialLocalVarDirInt]

				elif typeOfVarAux == "float":
					answer = self.finalLocalVarDirFloat[dirVar - initialLocalVarDirFloat]

				elif typeOfVarAux == "string":
					answer = self.finalLocalVarDirString[dirVar - initialLocalVarDirString]       
	

			elif scope == "constant":

				if typeOfVarAux == "bool":
					answer = self.finalConstVarDirBool[dirVar - initialConstVarDirBool] #resta la direccion con la direccion inicial para sacar el valor correcto

				elif typeOfVarAux == "int":
					answer = self.finalConstVarDirInt[dirVar - initialConstVarDirInt]

				elif typeOfVarAux == "float":
					answer = self.finalConstVarDirFloat[dirVar - initialConstVarDirFloat]

				elif typeOfVarAux == "string":
					answer = self.finalConstVarDirString[dirVar - initialConstVarDirString]     


			elif scope == "temporal":

				if typeOfVarAux == "bool":
						answer = self.finalTempVarDirBool[dirVar - initialTempVarDirBool] #resta la direccion con la direccion inicial para sacar el valor correcto

				elif typeOfVarAux == "int":
					answer = self.finalTempVarDirInt[dirVar - initialTempVarDirInt]

				elif typeOfVarAux == "float":
					answer = self.finalTempVarDirFloat[dirVar - initialTempVarDirFloat]

				elif typeOfVarAux == "string":
					print dirVar
					answer = self.finalTempVarDirString[dirVar - initialTempVarDirString]     


			#print(answer,"hola", dirVar);		
			return answer
	


	#Asignamos el valor a la direccion en el arreglo de memoria correspondiente		
	def setVarValue(self, dirVar, answer):

			if type(dirVar) is str:

				dirVar = dirVar.replace("(", "")
				dirVar = dirVar.replace(")", "") 

				dirVar = self.getVarValue(int(dirVar))

				

			scope = getVarScope(dirVar)
			typeOfVarAux = getVarType(dirVar)

			if scope == "global":

				if typeOfVarAux == "bool":
						self.finalGlobalVarDirBool[dirVar - inicialGlobalVarDirBool] = answer

				elif typeOfVarAux == "int":
						self.finalGlobalVarDirInt[dirVar - inicialGlobalVarDirInt] = answer

				elif typeOfVarAux == "float":
						self.finalGlobalVarDirFloat[dirVar - inicialGlobalVarDirFloat] = answer

				elif typeOfVarAux == "string":
						self.finalGlobalVarDirString[dirVar - inicialGlobalVarDirString] = answer
			
		 
			elif scope == "local":

				if typeOfVarAux == "bool":
					self.finalLocalVarDirBool[dirVar - initialLocalVarDirBool] = answer

				elif typeOfVarAux == "int":
					self.finalLocalVarDirInt[dirVar - initialLocalVarDirInt] = answer

				elif typeOfVarAux == "float":
					self.finalLocalVarDirFloat[dirVar - initialLocalVarDirFloat] = answer

				elif typeOfVarAux == "string":
					self.finalLocalVarDirString[dirVar - initialLocalVarDirString] = answer     
	

			elif scope == "constant":

				if typeOfVarAux == "bool":
					self.finalConstVarDirBool[dirVar - initialConstVarDirBool] = answer

				elif typeOfVarAux == "int":
					self.finalConstVarDirInt[dirVar - initialConstVarDirInt] = answer

				elif typeOfVarAux == "float":
					self.finalConstVarDirFloat[dirVar - initialConstVarDirFloat] = answer

				elif typeOfVarAux == "string":
					self.finalConstVarDirString[dirVar - initialConstVarDirString] = answer     


			elif scope == "temporal":

				if typeOfVarAux == "bool":
					#print("hola", len(self.finalTempVarDirBool))
					self.finalTempVarDirBool[dirVar - initialTempVarDirBool] = answer

				elif typeOfVarAux == "int":
					self.finalTempVarDirInt[dirVar - initialTempVarDirInt] = answer

				elif typeOfVarAux == "float":
					self.finalTempVarDirFloat[dirVar - initialTempVarDirFloat] = answer

				elif typeOfVarAux == "string":
				
					self.finalTempVarDirString[dirVar - initialTempVarDirString] = answer     




	#SEGUNDO
	def changeMemory(self):
		#asigna la memoria de la funcion a las variables principales de memoria y guarda la memoria anterior en un arreglo el cual meteremos en un stack para usarlo despues
		#solo local y temporal
		arrLastMemory = [self.finalLocalVarDirBool, self.finalLocalVarDirInt, self.finalLocalVarDirFloat, self.finalLocalVarDirString, self.finalTempVarDirBool, self.finalTempVarDirInt, self.finalTempVarDirFloat, self.finalTempVarDirString ]

		self.memoriesStack.append(arrLastMemory)

		self.finalLocalVarDirBool = self.functionLocalVarDirBool
		self.finalLocalVarDirInt = self.functionLocalVarDirInt
		self.finalLocalVarDirFloat = self.functionLocalVarDirFloat
		self.finalLocalVarDirString = self.functionLocalVarDirString
		self.finalTempVarDirBool = self.functionTempVarDirBool
		self.finalTempVarDirInt = self.functionTempVarDirInt
		self.finalTempVarDirFloat = self.functionTempVarDirFloat
		self.finalTempVarDirString = self.functionTempVarDirString

	#TERCERO
	def changeBackMemory(self):
		arrLastMemoryOut = self.memoriesStack.pop()

		self.finalLocalVarDirBool = arrLastMemoryOut[0]
		self.finalLocalVarDirInt = arrLastMemoryOut[1]
		self.finalLocalVarDirFloat = arrLastMemoryOut[2]
		self.finalLocalVarDirString = arrLastMemoryOut[3]
		self.finalTempVarDirBool = arrLastMemoryOut[4]
		self.finalTempVarDirInt = arrLastMemoryOut[5]
		self.finalTempVarDirFloat = arrLastMemoryOut[6]
		self.finalTempVarDirString = arrLastMemoryOut[7]	

	#PRIMERO
	def newFunc(self, func):
		#asigna la memoria correspondiente de la funcion
		self.functionLocalVarDirBool = range(func["localBool"] - initialLocalVarDirBool)
		self.functionLocalVarDirInt = range(func["localInt"] - initialLocalVarDirInt)
		self.functionLocalVarDirFloat = range(func["localFloat"] - initialLocalVarDirFloat)
		self.functionLocalVarDirString = range(func["localString"] - initialLocalVarDirString)

		self.functionTempVarDirBool = range(func["tempBool"] - initialTempVarDirBool)
		self.functionTempVarDirInt = range(func["tempInt"] - initialTempVarDirInt)
		self.functionTempVarDirFloat = range(func["tempFloat"] - initialTempVarDirFloat)
		self.functionTempVarDirString = range(func["tempString"] - initialTempVarDirString) 



	def getVarTypeHelper(self, dirVar):
		getVarAux = getVarType(dirVar)

		return getVarAux



#sacamos el scope dependiendo de donde este ubicado la direccion				
def getVarScope(dirVar):

			if inicialGlobalVarDirBool <=  dirVar < initialLocalVarDirBool:
					return "global"
			elif initialLocalVarDirBool <=  dirVar < initialConstVarDirBool:
					return "local"
			elif initialConstVarDirBool <=  dirVar < initialTempVarDirBool:
					return "constant"
			else:
					return "temporal"
		



#verifica en que rango esta la la direccion para sacar el tipo de variable      
def getVarType(dirVar):

		scope = getVarScope(dirVar)
		

		if scope == "global":
				if  inicialGlobalVarDirBool <= dirVar < inicialGlobalVarDirInt:
					return "bool"
				elif inicialGlobalVarDirInt <= dirVar <  inicialGlobalVarDirFloat:
					return "int"
				elif inicialGlobalVarDirFloat <= dirVar <  inicialGlobalVarDirString:
					return "float"
				else:
					return "string"

		elif scope == "local":
				if initialLocalVarDirBool <= dirVar < initialLocalVarDirInt:
					return "bool"
				elif initialLocalVarDirInt <=   dirVar < initialLocalVarDirFloat:
					return "int"
				elif initialLocalVarDirFloat <=   dirVar < initialLocalVarDirString:
					return "float"
				else:
					return "string"

		elif scope == "constant":
				if initialConstVarDirBool <=   dirVar < initialConstVarDirInt:
					return "bool"
				elif initialConstVarDirInt <=   dirVar < initialConstVarDirFloat:
					return "int"
				elif initialConstVarDirFloat <=   dirVar < initialConstVarDirString:
					return "float"
				else:
					return "string"      

		elif scope == "temporal":
				if initialTempVarDirBool <=   dirVar < initialTempVarDirInt:
					return "bool"
				elif initialTempVarDirInt <=   dirVar < initialTempVarDirFloat:
					return "int"
				elif initialTempVarDirFloat <=   dirVar < initialTempVarDirString:
					return "float"
				else:
					return "string" 



















