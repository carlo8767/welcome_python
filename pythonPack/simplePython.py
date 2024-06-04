# CONCATENATION
name = "Carlo"
lastName = "Carraro"

print(f'{name} {lastName}')
print(name + " " + lastName)

# INPUT INTERACTION
recover_input = "Ok" # input("Recover input")

if recover_input == "Ok":
    print(recover_input)
if recover_input == "No":
    print("No")
else:
    print(recover_input)

# DATA TYPE CONVERSION
grades = "9"
convert_grades = int(grades)
print(type(convert_grades))
second_grades = 9
convert_second_grades = str(second_grades)
print(type(convert_second_grades))

# LIST
list_month = ["January", "February"]
print(list_month[-1])

# LOOP FOR WHILE
list_month = ["January", "February", "March", "May"]



for list_months in list_month:
    print(list_month)

for index, item in enumerate(list_month):
    print(index)
    print(item)

control_loop = True
number = 0
while control_loop:
    number += 1
    if number > 2:
        print("The loop is terminate")
        control_loop = False
    else:
        print(number)
        continue

# RANGE FUNCTION

for numbers in range(0,2):
    print(f'this is first {numbers}')

for numbers in range(10,0, -1):
    print(f'this is second {numbers}')

for numbers in range(0,10, 1):
    print(f'this is third {numbers}')

for numbers in range(0, 10, 2):
    print(f'this is fourth {numbers}')

    # the first parameter is inclusive
    # the second is esclusive
    # the third me  allow to control the iteraction