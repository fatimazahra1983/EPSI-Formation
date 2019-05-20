import sys

from calculator.operands.parser import parse_operand

if __name__ == '__main__':
	if (len(sys.argv) < 4):
		print('usage: calculator.py <operand> <operator> <operand>')
		sys.exit(1)
	leftOp = parse_operand(sys.argv[1])
	rightOp = parse_operand(sys.argv[3])

	print('Left Operand is {}'.format(leftOp.value()))
	print('Right Operand is {}'.format(rightOp.value()))
