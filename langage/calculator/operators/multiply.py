from .operator import Operator

class Multiply(Operator):
	def __init__(self):
		pass

	def compute(self, left, right):
		return left.value() * right.value()
