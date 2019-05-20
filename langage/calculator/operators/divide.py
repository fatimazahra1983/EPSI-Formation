from .operator import Operator

class Divide(Operator):
	def __init__(self):
		pass

	def compute(self, left, right):
		if right.value == 0:
			return 'Illegal operation : Division by zero'
		return left.value / right.value
		
	def __str__(self):
		return '/'

	def __repr__(self):
		return 'Division$(/)'
