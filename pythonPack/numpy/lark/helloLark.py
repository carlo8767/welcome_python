from lark import *

"https://lark-parser.readthedocs.io/en/latest/"


grammar ="""
start: "0" rest | "1" rest | "2" rest | "3" rest | "4" rest 
| "5" rest | "6" rest | "7" rest | "8" rest | "9" rest
rest: "+" start| "-" start| "*" start |
""";
parser = Lark(grammar,parser ="lalr", keep_all_tokens = True )
tree = parser.parse("7-2*3");

print(tree.children)