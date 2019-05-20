import sys

from calculator.operands.parser import parse_operand
from calculator.operators.parser import parse_operator

if __name__ == '__main__':
	if (len(sys.argv) < 4):
		print('usage: calculator.py <operand> <operator> <operand>')
		sys.exit(1)
	leftOp = parse_operand(sys.argv[1])
	rightOp = parse_operand(sys.argv[3])
	operator = parse_operator(sys.argv[2])
	print(operator.compute(leftOp, rightOp))
