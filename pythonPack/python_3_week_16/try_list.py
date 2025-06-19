SIZE = 10

def read_numbers():
	numbers = []
	for _ in range(SIZE):
		try:
			value = int(input("Enter 10 number "))
			numbers.append(value)
		except ValueError:
			print("The string enter is not a number!!")
	return  numbers

l = read_numbers()
print(" ".join(str(i) for i in l))



