if __name__ == "__main__":

    try:
        int("String")
    except ValueError:
        print("Value Error")
    finally:print("Always")
    list_value = [1,5,9,0]
    list_value.sort(key=lambda x :x<2)



    print(list_value[::2])
    a = 5
    b = 5
    fa = {1,2,3}
    s = frozenset(fa)
    print(type(s))
    print(a is b)
    ps = {"f":"hello"}
    print(ps.get("afs"))

    n = 0.10
    print(type(n))
    int(n)
    p = set()
    str(p)
