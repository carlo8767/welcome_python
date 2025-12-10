import sqlite3

conn = sqlite3.connect("../input2.db")
cur = conn.cursor()

def make_table(name, cols, rows):
    col_defs = ", ".join(f"{c} INTEGER" for c in cols)
    cur.execute(f"CREATE TABLE {name} ({col_defs});")
    q = ",".join("?" * len(cols))
    cur.executemany(f"INSERT INTO {name} VALUES ({q});", rows)

# ===== UNION =====
make_table("u1", ["a","b"], [(11,22),(33,44)])
make_table("u2", ["x","y"], [(33,44),(55,66)])
make_table("u3", ["u","v"], [(11,22),(33,44),(55,66)])

# ===== INTERSECTION =====
make_table("i1", ["m","n"], [(1,5),(2,6),(3,7)])
make_table("i2", ["p","q"], [(3,7),(4,8),(5,9)])
make_table("i3", ["r","s"], [(3,7)])

# ===== CARTESIAN PRODUCT =====
make_table("c1", ["a"], [(2,),(4,)])
make_table("c2", ["b"], [(6,),(8,)])
make_table("c3", ["a","b"], [(2,6),(2,8),(4,6),(4,8)])

# ===== EXTRAS =====
make_table("extraA", ["x","y"], [(50,60),(70,80)])
make_table("extraB", ["z"], [(99,),(100,)])

conn.commit()
conn.close()

print("input2.db created successfully!")
