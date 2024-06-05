# COLLECTION TUPLE IT IS NOT POSSIBLE TO CHANGE

tuple_data = ("test", "test")
print(tuple_data)

# SET DO NOT ALLOW DUPLICATE
set_value = {1,2,2}

set_number = set()
count = 0
while count < 5:
    count+=1
    set_number.add(1)

print(set_number)



# SPLIT FUNCTION

name = "1,2,3,4,5"
split_name = name.split(",")
print(type(split_name))
print(split_name)

split_limit = name.split(",", 2)
print(split_limit)


# FILE OPERATIONS

# WRITE A FILE
file = open('helloFile.txt', 'w')
file.write('I want eat pizza')
file.close()
# READ A FILE
file = open('helloFile.txt', 'r')
content = file.read()
print(content)
file.close()

# APPEND A FILE


file = open("helloFile.txt", "a")
file.write("\nI want more pizza")
file.close

with open("helloFile.txt", "a") as file_object:
    file_object.write("This is append")



#  CONVERT A NUMBER TO BINARY HEXADECIMAL

value_number = 10
# YOU CAN CONVERT USING OR BIN OR FORMAT
binary_value = bin(value_number)
binary_value_format = format(value_number, 'b')
print(binary_value_format)

# YOU CAN CONVERT USING OR HEX OR FORMAT
value_number_hexa = hex(value_number)
value_number_hexa_format = format(value_number, 'x')
print(value_number_hexa_format)


# FROM HEX TO DECIMAL  WITH INT YOU HAVE TO SPECIFY WHAT TYPE OF BYTE
convert_hexa = bin(int(value_number_hexa_format, 16))
original_value = int(convert_hexa, 2)
print(original_value)


# CONVERSION STRING
string_name = "Carlo"
string_name_hexa = string_name.encode('utf-8').hex()
print(string_name_hexa)
decode_name = bytes.fromhex(string_name_hexa).decode('utf-8')
print(decode_name)


# CONDITINIAL STATEMENT

number_verify = 10
if number_verify == 10:
    print("ok")
else:
    print("no")


















