from . import operand
from . import number

def parse_operand(arg: str) -> operand.Operand:
	try:
		v = int(arg)
		return number.Number(v)
	except ValueError:
		return None
