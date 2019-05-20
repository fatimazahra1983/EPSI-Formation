import abc
from abc import abstractmethod

class Operand(abc.ABC):
	def __init__(self):
		pass

	@abstractmethod
	def value(self):
		pass
