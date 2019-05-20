from .operator import Operator

class Add(Operator):
	def __init__(self):
		pass

	def compute(self, left, right):
		return left.value + right.value

	def __str__(self):
		return '+'

	def __repr__(self):
		return 'Addition(+)'
