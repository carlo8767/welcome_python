import pathlib

# Change this to "text" for the full book
file_name = "text_excerpt.txt"

# Do not modify this part
with (pathlib.Path(__file__).parent / file_name).open("rt", encoding="utf-8") as f:
    text = f.read()

print(text)
