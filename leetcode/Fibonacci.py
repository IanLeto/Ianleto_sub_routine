from itertools import *
# 生成器适合无限生成的情况


def fb():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


def main():
    Ian_Fibonacci = list(islice(fb(), 10))

    print(Ian_Fibonacci)


if __name__ == '__main__':
    main()
