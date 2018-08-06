from time import time

def IanTimeCalc(func):
	start = time()
	result = func()
	stop = time()
	run_time = str(stop - start)

	return run_time

@IanTimeCalc
def main():
	Ian_test = []
	for i in range(1, 999999):
		Ian_test.append(i)
	return Ian_test


if __name__ == '__main__':
	print(main)