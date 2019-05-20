from .operator import Operator
from .add import Add
from .sub import Sub
from .multiply import Multiply
from .divide import Divide

def parse_operator(op: str) -> Operator:
	if op == '+' or op == 'add':
		return Add()
	elif op == '-' or op == 'sub':
		return Sub()
	elif op == '*' or op == 'multiply':
		return Multiply()
	elif op == '/' or op == 'divide':
		return Divide()
	return None 
