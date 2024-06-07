import os


class decorator:
    #  with *args you can
    # pass an unspecified number of arguments

    def test_args_args(self, Firstargs, SecondArgs, ThirdArgs):
        print(Firstargs)
        print(SecondArgs)
        print(ThirdArgs)

    # with  you can  keyword variable length**
    # pass an unspecified number of arguments
    def test_args_kwargs(self, FirstArgs, SecondArgs, ThirdArgs):
        print("FirstArgs:",FirstArgs)
        print("SecondArgs:",SecondArgs)
        print("ThirdArgs:",ThirdArgs)


# ELSE RUNNED AFTER FOR LOOP
for numbers in range(0,11):
    print(numbers)
else:
    print("ok")


# LIST OPERATIONS
list_value = ["One", "Two", "Three"]
list_value = list_value[-3:-1]
print(list_value)




# DICTIONARY

dictionary_value = {"A":"Exceptional", "B": "Very Good", "C": "Good"}

del(dictionary_value["A"])


list("123")
# EXTRACT ALL THE KEY FROM A DICTIONARY
list_dictionary = dictionary_value.keys()
value_key = dictionary_value.get("A")
print(value_key)

# EXTRACT ALL THE VALUE FROM A DICTIONARY
list_dictionary = dictionary_value.keys()
value_key = dictionary_value.values()
print(value_key)

str = "carlo"

# MIN RETURN THE MINUM CHARACTER
ts = min(str)
ls_strip = str
print(ts)
# LSTRIP REMOVE WHITE SPACES
print(ls_strip.lstrip(ts))

# EVALUATION

evaluate = 33 == 33.1
print(evaluate)

# SWITCH TWO NUMBER WITHOUT A THIRD VARIABLE

a = 10
b = 20

a, b = b, a
print(a, b)

# PRINT TWO TIMES
tiny_list = ["one"]
print(tiny_list * 3)

# ARITHMETIC OPERATOR POWER
n = 20
p = 30
print(3 ** 2)


if n % 2 == 0 :
 print("ok")

# POSITIONAL ARGUMENT VS KEYBOARD ARGUMENTS
# NAME IS NOT IMPORTANCE THE ORDER
#  end="!", sep=",")
print(1, 2, 3, 4, end="!", sep= ",")

# IS INSTANCE RETURN IF A CLASS IS AN INSTANCE OF
# ANOTHER CLASS
# isinstance()

# INT YEAR

year_end = 2025
year_start = 1988

 # YOU CAN ONLY CONCATENATE STRING
# print("congratulation!!" + (year_end -year_start ))

# IS USED IF TWO CHECK TWO VARIABLE POINT AT THE SAME OBJECT

list_one = ["1","2","3"]
list_two = list_one
print(list_one is list_two)

a=11
b=4
# only division without decimal
print(a // b)
# module
print(a % b)
# division
print(a / b)

print(2**2)


# SLICE
# cut
# slice(start, end, step)

list_number = ["one","two","three","fourth"]
slice_value = slice(1,4)
print(list_number[slice_value])
print(list_number[:1])
# PRINT ONLY THE FIRST TWO
print(list_number[:-2])


# RETURN NONE
# file_name is a parameter
def get_first_line(filename):
        try:
            with open(filename, 'r') as file:
                if os.path.isfile(filename):
                    return file.readline()
                else:
                    raise FileNotFoundError
        except FileNotFoundError as e:
            return None
# we pass an argument
print(get_first_line("text.txt"))

# OPEN CLOSE THE FILE

# w+ (writing +reading delete old content and add a new content
# i can read after I read the file ps : remeber to add seek.0
# )
# r+(  ìt Opens a file for both reading and writing.


# ORDER OPERATIONS
# P - Parentheses, then.
# E - Exponents, then.
# MD - Multiplication and division, left to right, then.
# AS - Addition and subtraction, left to right.

# PAGE 55
# SLICE TWO

b = "Hello, World!"
# the first inclusive, the second esclusive
print(b[2:-2])

print(3*2)




list_subject = ["Italian", "Math", "History"]
print(list_subject[0:-1])

string_a  = "ts"
string_b = string_a
print(end="hello", sep="e")
evaluation = string_a == string_b
print(evaluation)


class Dog:

    def init(self,name):
        self.name=name

for n in range(5):
    print(n)

# dictionary_keys = {['ts']:1}

d = {'a': 1, 'b': 2};
d['c'] = 3;
print(len(d))
print(d)



if __name__ == '__main__':

    test = decorator()
    list_kwargs = [1,2,3]
    test.test_args_args(*list_kwargs)
    dictinary_kwargs = {"FirstArgs":1, "SecondArgs":2, "ThirdArgs":3}
    test.test_args_kwargs(**dictinary_kwargs)