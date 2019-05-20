import sys

if __name__ == '__main__':
	if (len(sys.argv) < 4):
		print('usage: calculator.py <operand> <operator> <operand>')
		sys.exit(1)
