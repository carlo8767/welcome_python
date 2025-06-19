from mpl_toolkits.mplot3d.proj3d import transform

if __name__ == '__main__':

 l = ["aa", "a", "b", "c", "ab", "cd", "ef"]
 print(list(sorted(l)))
 print(list(reversed(l)))


 l = ["a", "b", "c", "ab", "cd", "ef"]
 l += "ff"
 for e in reversed(l[::2]):
     print(e)
 print(reversed(l))
 print(list(sorted(l[:1])))
 result = 10 / 4
 print(result   )
 numbers =  [99,21,3]
 numbers.sort()


 setOrDictionary  = {"fa"}
 print(type(setOrDictionary))
 hello = {"n":1}


 result = hello.get("p")
 print(result)

 city_map = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 11)],
    'E': [('D', 4)],
    'F': []}

 print(city_map['D'])

