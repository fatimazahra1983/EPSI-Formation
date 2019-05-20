import abc
from abc import abstractmethod
from ..operands.operand import Operand

class Operator(abc.ABC):
	def __init__(self):
		pass

	@abstractmethod
	def compute(self, left: Operand, right: Operand):
		pass
