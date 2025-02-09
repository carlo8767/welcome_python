import math


def is_prime(n):
    # is a prime number if is only divisible for itself and one
    for i in range (2,int(n ** .5) + 1 ):
        if n % i == 0:
          return False
    return True

def smaller_prime_number (n):
    list_value = []
    set_prime_number = {}
    for a in range (n):
        list_value.append(a)
    for i in range (2, n):
        for inner in list_value:
            if i % inner == 0  and i !=inner:
              if set_prime_number.get(i) is not None :
                set_prime_number.pop(i)
              break
            else:
              set_prime_number [i] = 0
    list_prime_number = list(set_prime_number)
    return list_prime_number




if __name__ == "__main__":

  dictionary_language = {"Test": "n"}

  list_scores = [('John', 5), ('Dave', 55), ('Robin', 10)]
  list_scores.sort(key=lambda n: n[1])
  for i in list_scores:
      print(i)
  empty_list = []

  if  empty_list:
      print("ok")
  else :
      for i in empty_list:
          print("I am")
  num = int(input("Please enter a number: "))
  if is_prime(num):
    print(f"{num} is a prime")
  else:
    print(f"{num} is not a prime")
  

