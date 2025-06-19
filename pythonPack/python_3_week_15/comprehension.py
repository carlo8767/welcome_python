# PART 1
line = input().split()
lower_words = []
for w in line:
    lower_words.append(w.lower())

print(" ".join(lower_words))

# PART 2
large_words = []
for w in lower_words:
    if len(w) > 6:
        large_words.append(w)
print(" ".join(large_words))

# PART 3
a_count = []
for w in large_words:
    if "a" in w:
        a_count.append(w.count("a"))
if a_count:
    avg = sum(a_count) / len(a_count)
    print(f"Average: {avg:.2f}")
else:
    print("No a!")


# PART 4
count_strings = []
for i in a_count:
    count_strings.append(str(i))
print(f"Count: {' '.join(count_strings)}")
