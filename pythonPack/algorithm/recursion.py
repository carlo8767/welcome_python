# just an example list
a_list = [1,2,3,4,5]

# input a list
# output True if the list is empty, False otherwise
def is_empty(l):
    return l == []

# input a list
# output the first element of the list
def head(l):
    return l[0]

# input a list
# output the list without the first element
def tail(l):
    return l[1:]

# input a list
# output the tuple (head(l), tail(l))
def get_head_and_tail(l):
    return head(l), tail(l)

# input an element and a list
# output the list with the element added at the beginning of the list
def add(elem, l):
    return [elem] + l

# input an element and a list
# output the list with the element appended at the end of the list
def append(elem, l):
    if is_empty(l):
        return [elem]
    head, tail = get_head_and_tail(l)
    return add(head, append(elem,tail))

def get_max(list_collect, accumulator):
    # list_a = [1, 5, 2, 3, 4]
    if is_empty(list_collect):
       return accumulator
    if accumulator > head(list_collect):
        print(f'{accumulator} {list_collect}')
    else:
        accumulator = head(list_collect)
    tails =  tail(list_collect)
    return get_max(tails, accumulator)




def limit (list):
    if is_empty(list):
        return [list]
    head, tail = get_head_and_tail(list)
    return add(head, append(list, tail))



def length(l):
    if not l:
        return []
    return 1 +length(tail(l))


if __name__ == '__main__' :

    list_a = [1, 5, 2, 3, 4]
    get_max(list_a, head(list_a))
