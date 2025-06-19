import pathlib
import sys

# Change this to "text" for the full book
file_name = "text.txt"

# Do not modify this part
with pathlib.Path(file_name).open("rt", encoding="utf-8") as f:
    text = f.readlines()


# Find all words that appear
words = set()
for line in text:
    for w in line.split():
        words.add(w.lower())

# Count how often each appears
counts = []
for w in sorted(words):
    count = 0
    for line in text:
        for v in line.split():
            if w == v.lower():
                count += 1
    counts.append((count, w))

# Print out the counts
lines = []
for c, w in sorted(counts):
    # Filter out very uncommon ones
    if c > 4:
        lines.append(f"{c:7d}: {w}")
print("\n".join(lines))
