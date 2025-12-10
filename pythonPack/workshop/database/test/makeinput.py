import sqlite3

conn = sqlite3.connect("../input.db")
cur = conn.cursor()

def make_table(name, cols, rows):
    col_defs = ", ".join(f"{c} INTEGER" for c in cols)
    cur.execute(f"CREATE TABLE {name} ({col_defs});")
    q = ",".join("?" * len(cols))
    cur.executemany(f"INSERT INTO {name} VALUES ({q});", rows)

# UNION triple
make_table("t7", ["c1","c2"], [(1,2),(3,4)])
make_table("t15", ["d1","d2"], [(3,4),(5,6)])
make_table("t17", ["u1","u2"], [(1,2),(3,4),(5,6)])

# INTERSECTION triple
make_table("t2", ["a","b"], [(10,20),(30,40)])
make_table("t3", ["x","y"], [(30,40),(50,60)])
make_table("t11", ["i1","i2"], [(30,40)])

# CARTPROD triple
make_table("t9", ["p"], [(7,),(8,)])
make_table("t21", ["q"], [(9,),(10,),(11,)])
make_table("t24", ["p","q"], [(7,9),(7,10),(7,11),(8,9),(8,10),(8,11)])

# Extra tables
make_table("t_extra1", ["e1","e2"], [(100,200),(300,400)])
make_table("t_extra2", ["z"], [(999,),(1000,)])

conn.commit()
conn.close()

print("input.db created successfully!")
