import pathlib
import sys


description = "Ray is, late! Another time"
ls  = ",".join(description)
separation = description.split(",")

print(separation[0])
names =  "fasdf"
fasd = [x for x in names]
l = ["a", "b", "c", "ab", "cd", "ef"]
l.reverse()
numbers = [1,2,3]
numbers.sort( key=lambda x: x<3 )
print(numbers)

# Change this to "text" for the full book
file_name = "text.txt"
# Do not modify this part
with pathlib.Path(file_name).open("rt", encoding="utf-8") as f:
    text = f.readlines()


listWord = [word for line in text for word in line.split()]
testDictionary = {k:0 for word in listWord for k in word.lower()}

# Find all words that appear
words = dict()

for line in text:
    for w in line.split():
        words[w.lower()]  =0
for line in text:
    for w in line.split():
       words[w.lower()]+=1

print(words["i"])

