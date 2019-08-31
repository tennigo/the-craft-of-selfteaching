def multi():
	print("乘法")
	for i in range(1, 10):
		for j in range(1, i+1):
			print("%d*%d=%d\t"%(i, j, i*j), end='')

		print("")
	print("=" * 50)


def plus():
	print("加法")
	for i in range(1, 10):
		for j in range(1, i+1):
			print("%d+%d=%d\t"%(i, j, i+j), end='')

		print("")
	print("=" * 50)


def minus():
	print("减法")
	for i in range(1,10):
		for j in range(1,i+1):
			print("%d-%d=%d\t"%(i, j, i-j), end='')

		print("")
	print("=" * 50)

def main():
	multi()
	plus()
	minus()

if __name__ == '__main__':
	main()

