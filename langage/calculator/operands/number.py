from . import operand

class Number(operand.Operand):
	def __init__(self, v):
		self._val = v
	
	@property
	def value(self):
		return self._val

	def __str__(self):
		return str(self._val)

	def __repr__(self):
		return 'Number(_val={})'.format(self._val)
