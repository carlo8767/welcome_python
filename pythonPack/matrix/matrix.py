class Test:

 def rec(self, n):
    if n == 0:
        return 0
    else:
        return n + self.rec(n - 1)


def mystery(n):
    if n <= 1:
        return 1
    else:
        print(n)
        return mystery(n//3) + mystery(2*n//3) + n

if __name__ == '__main__' :

    ts = mystery(10)

    n = Test()
    sum = n.rec(4)
    print(sum)
    matrix = [[0,1,0],[1,0,0],[1,0,0]]
    count_clique = 0
    dict_clique = dict()
    list_clique = list()
    for x, y in enumerate(matrix):
        for p, n in enumerate(matrix[x]):
            if n == 1:
                # verify clique
                if matrix[p][x] == 1:
                    dict_clique[x] = list_clique.append(p)
                print(f'the row is {x} and the colum is {p}')




