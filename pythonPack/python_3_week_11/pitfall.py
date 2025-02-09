

def live_longer ():

    i =0;
    a=5;
    for i in range (10):
        a+=i
    print(a,i)

def funny_function(a, b):
    return a + b, a * b

def default_value (n: int, default=4):
    print(f'{default}')



def mistake ():
  for i in range(10):
    print(i%2)
    if i % 2 :
      continue
    if i // 4 == 1:
      break
    print(f'professor {i}')

if __name__ == "__main__":

    mistake()
    live_longer()
    la = "la,ts"
    list_la = la.split(",");
    print(repr(list_la))
    default_value(6)
    n , d = funny_function(4,2)
    print(f'the value of n is { n } and the value of d is { d }')
    i = 0;
    for i in range(10, +1):
        print(f'this value is {i}')
    for i in range(10):
        print(i)

    print(i)