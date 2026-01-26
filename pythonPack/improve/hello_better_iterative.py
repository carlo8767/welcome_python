

"""
any
all
next
list_result = [x for x in data if condition]
for k, value in dictionary.items():
pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
zip
extend, join, copy
union_messages = verify_relation(relations, lambda a, b: a | b, "is UNION of")
map()
"""





if __name__ == '__main__':



    fruits = ['apple', 'banana', 'cherry' 'apple']

    points = (1, 4, 5, 9)

    fruits.extend(points)
    print(fruits)


    apples = list(filter(lambda fruit: fruit == 'apple', fruits))

    fruits = ['banana', 'apple', 'cherry']

    next_fruits = next(fruits == 'apple' for fruit in fruits)
    # ALL THE ITEM TRUE
    all_fruits = all(fruits == 'apple' for fruit in fruits)

    print(next_fruits)
    print(all_fruits)

    mylist = iter(["banana", "apple", "cherry"])
    # first iteration
    x = next(mylist, "orange")
    print(x)
    mytuple = (0, 1, False)
    x = any(mytuple)
    print(x)