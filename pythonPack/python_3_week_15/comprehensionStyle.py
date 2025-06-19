# PART 1

line = input().split()
lower_words = [ w for w in line]
print(" ".join(lower_words))

# PART 2
large_words = [w for w in lower_words if len(w)>6]
print(" ".join(large_words))

# PART 3
a_count = [w for w in large_words if "a" in w]
if a_count:
    avg = sum(a_count) / len(a_count)
    print(f"Average: {avg:.2f}")
else:
    print("No a!")

# PART 4
count_strings = [i for i in a_count]
print(f"Count: {' '.join(count_strings)}")
