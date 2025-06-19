
def default (number = 3):
    print(number)


def partition(arr, lower, upper):
    i = lower
    pivot = arr[upper]
    for jj in range(lower,upper+1):
        if arr [jj] < pivot:
            tmp = arr[i]
            arr [i] = arr[jj]
            arr [jj] = tmp
            i+=1
    # WHEN WE COMPLETE WE SWITCH THE PIVOT ELEMENT WITH THE OTHER BIGGER
    tmp = arr[i]
    arr[i] = arr[upper]
    arr[upper] = tmp
    return i



def quick_sort(arr, lower, upper):
    # END CONDITION
    if lower < upper:
      flag_i =   partition(arr, lower, upper)
      quick_sort(arr,lower, flag_i-1 )
      quick_sort(arr, flag_i+1, upper)
    print(arr)



def insertion_sort (items):
    print(f'before the sort {items}')
    for i in range (1, len(items)):
        j = i
        while j > 0 and items[j-1] > items[j]:
          tmp = items[j-1]
          items[j-1] =  items[j]
          items[j] = tmp
          j -=1
        print(f'after the sort {items}')

def selection_sort (items):
  for i in range (0, len(items)):
    min_index = i
    for j in range (i, len(items)):
        if items[j] < items[min_index]:
            min_index = j
    if min_index != i:
        tmp = items[i]
        items[i] = items[min_index]
        items[min_index] = tmp
        print(f'after the sort {items}')


if __name__ == "__main__":


    list_values = [2, 10, 6, 8, 3, 6, 9]
    quick_sort(list_values, 0, len(list_values)-1)

    p = set()
    p.add("5")

    for s in p:
        print(s)

    a = "abcdefg"
    print(" ".join(a[1::2]))
    a = [9, 3, 4]
    for i in range(2):
        print(a[i])
    default(2)
    a = 0.7
    b = 20
    print(a < 12 or b == a)
    print(10.0 < b < 30 and a != 1.0)
    print(not (a > b))

    hello = "Hello"
    print(id(hello))
    hello += "n"
    print(id(hello))