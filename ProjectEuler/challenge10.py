import math
def is_prime(x):
    a = 1
    a = int(a) 
    while a <= math.sqrt(x): 
        if x % a == 0 and a != 1:
              return False
        a += 1
    return True
n = 1
tot = 2
while n <= 2000000:
    n = n + 2
    if is_prime(n):
        tot += n 

print(tot)
