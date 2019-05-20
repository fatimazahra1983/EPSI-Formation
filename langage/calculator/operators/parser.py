from .operator import Operator
from .add import Add

def parse_operator(op: str) -> Operator:
	if op == '+' or op == 'add':
		return Add()
	return None 
