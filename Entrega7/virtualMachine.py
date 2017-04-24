from Yaotecatl import *
from cuboSemantico import *

def runVirtualMachine( quadruplesList,globalVarDir,localVarDir,constVarDir,tempVarDir,constantDict,localVarDict,globalVarDict):

	print ("Yaotecatl virtual machine RUNNING...")

quadCount = 0  #contador de quadruplos

while quadruplesList[quadCount]['OPERATOR'] != "END":
	quad = quadruplesList[quadCount]

	##Substaction
	if quad['OPERATOR'] == '-':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory
		
		op2Value = #memory

		

		lastResult = op1Value - op2Value

		#memory

	##addition	
	elif quad['OPERATOR'] == '+':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory

		lastResult = op1Value + op2Value

		#memory

	#multiplication
	elif quad['OPERATOR'] == '*':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory



		lastResult = op1Value * op2Value

		#memory

	#division	
	elif quad['OPERATOR'] == '/':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory



		lastResult = op1Value / op2Value

		#memory


	#equals	
	elif quad['OPERATOR'] == '=':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			#memory


	#greaterthan
	elif quad['OPERATOR'] == '>':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory



		lastResult = op1Value > op2Value

		#memory

	#lessthan
	elif quad['OPERATOR'] == '<':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory



		lastResult = op1Value < op2Value

		#memory

	#greaterthanorequal	
	elif quad['OPERATOR'] == '>=':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory



		lastResult = op1Value >= op2Value

		#memory

	#lessthanorequal
	elif quad['OPERATOR'] == '<=':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory



		lastResult = op1Value <= op2Value

		#memory

	#	
	elif quad['OPERATOR'] == '==':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory



		lastResult = op1Value == op2Value

		#memory

	#different
	elif quad['OPERATOR'] == '!=':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory



		lastResult = op1Value != op2Value

		#memory

	#and
	elif quad['OPERATOR'] == '&&':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory



		lastResult = op1Value and op2Value

		#memory

	#or
	elif quad['OPERATOR'] == '||':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

		op1Value = #memory

		op2Value = #memory



		lastResult = op1Value or op2Value

		#memory

	#print	
	elif quad['OPERATOR'] == 'PRINT':
		result = quad['RESULT']

		op1Value = #memory

		#printwithmemory


	#read	
	elif quad['OPERATOR'] == 'READ':
		result = quad['RESULT']

		op1Value = #memory

		#readwithmemory

	#era	
	elif quad['OPERATOR'] == 'ERA':
		result = quad['RESULT']

		#memory



	#param	
	elif quad['OPERATOR'] == 'PARAM':
		op1 = quad['OP1']
	
		result = quad['RESULT']

		#memory	


	#gosub	
	elif quad['OPERATOR'] == 'GOSUB':
		result = quad['RESULT']

		quadCount = result - 1

		#memory		



	#return	
	elif quad['OPERATOR'] == 'RETURN':
		result = quad['RESULT']

		op1Value = #memory

		#memory		

	#endproc
	elif quad['OPERATOR'] == 'ENDPROC':
		
		#memory		



	#goto	
	elif quad['OPERATOR'] == 'GOTO':
		result = quad['RESULT']

		quadCount = result - 1


	#gotof	
	elif quad['OPERATOR'] == 'GOTOF':
		op1 = quad['OP1']

		result = quad['RESULT']

		quadCount = result - 1

		#memory



	#gotom	
	elif quad['OPERATOR'] == 'GOTOM':
		result = quad['RESULT']

		quadCount = result - 1

		#memory
		


	#verify	
	elif quad['OPERATOR'] == 'VERIFY':
		op1 = quad['OP1']

		#memory	



	quadCount += 1

