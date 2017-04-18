from Yaotecatl import *
from cuboSemantico import *

def runVirtualMachine( quadruplesList,):

	print ("Yaotecatl virtual machine RUNNING...")

contQuadruples = 0

while quadruplesList[contQuadruples]['OPERATOR'] != 'END' :
	quad = quadruplesList[contQuadruples]

	##Substaction
	if quad['OPERATOR'] == '-':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory
		
			op2Value = #activeMemory

		

		resultValue = op1Value - op2Value

		##add value to active activeMemory

	##addition	
	elif quad['OPERATOR'] == '-':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory

		resultValue = op1Value + op2Value

		##add value to active activeMemory

	#multiplication
	elif quad['OPERATOR'] == '*':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory



		resultValue = float(op1Value) + float(op2Value)

		##add value to active activeMemory

	#division	
	elif quad['OPERATOR'] == '/':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory



		resultValue = op1Value / op2Value

	#equals	
	elif quad['OPERATOR'] == '=':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			##check later

		##add value to active activeMemory

	#greaterthan
	elif quad['OPERATOR'] == '>':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory



		resultValue = op1Value > op2Value

		##add value to active activeMemory

	#lessthan
	elif quad['OPERATOR'] == '<':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory



		resultValue = op1Value < op2Value

		##add value to active activeMemory

	#greaterthanorequal	
	elif quad['OPERATOR'] == '>=':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory



		resultValue = op1Value >= op2Value

		##add value to active activeMemory

	#lessthanorequal
	elif quad['OPERATOR'] == '<=':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory



		resultValue = op1Value <= op2Value

		##add value to active activeMemory

	#	
	elif quad['OPERATOR'] == '==':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory



		resultValue = op1Value == op2Value

		##add value to active activeMemory

	#different
	elif quad['OPERATOR'] == '!=':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory



		resultValue = op1Value != op2Value

		##add value to active activeMemory

	#and
	elif quad['OPERATOR'] == '&&':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory



		resultValue = op1Value != op2Value

		##add value to active activeMemory

	#or
	elif quad['OPERATOR'] == '||':
		op1 = quad['OP1']
		op2 = quad['OP2']
		result = quad['RESULT']

			op1Value = #globalMemory

			op2Value = #activeMemory



		resultValue = op1Value != op2Value

		##add value to active activeMemory

	contQuadruples += 1

	#print
	@gotof
	#goto
	#read
	#memory

