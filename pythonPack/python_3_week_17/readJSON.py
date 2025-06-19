import json
from pathlib import Path


with Path("users.json").open("r") as r:
    read = json.load(r)
    for n in read:
        print(n)
