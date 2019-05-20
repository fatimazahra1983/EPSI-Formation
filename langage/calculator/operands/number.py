from . import operand

class Number(operand.Operand):
	def __init__(self, v):
		pass
		self._val = v
	
	def value(self):
		return self._val
