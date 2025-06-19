
import argparse

def sum (a:int,b:int)-> int:
    return a+b





if __name__ == "__main__":

    names = "Carlo";
    print("h".join(names))
    helloValue = dict()
    helloValue["Number"] = 5
    helloValue.get("Number")
    d = 3
    c = 52
    a = 5
    b = 51
    aa = ""
    bb = "s"

    print(aa is bb)
    print(id(aa))
    print(id(bb))
    print(int(a) == b)




    n = dict()
    n["1"] = 3
    print(n.get("1"))
    dict.values(n)
    parser = argparse.ArgumentParser(description="Run sum function with two integers.")
    parser.add_argument("a", type=int, help="First number")
    parser.add_argument("b", type=int, help="Second number")
    args = parser.parse_args()
    result = sum(args.a, args.b)
    print(f'the addition is {result}')



