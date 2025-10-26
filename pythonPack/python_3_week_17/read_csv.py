import csv
from pathlib import Path

with Path("grades.csv").open("r") as f:
    rows = csv.reader(f)
    # rows = f.readlines() # TODO Replace with csv reader
    for i in rows :
        # print(row)
        for i, v in enumerate(i) :
            print(float(v))



