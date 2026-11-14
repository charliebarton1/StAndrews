def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

counter = [0]     # store best count at index 0
a_b = (None, None)

def test(a, b):
    global a_b, counter
    x = 0
    count = 0
    while is_prime(x*x + a*x + b):
        count += 1
        x += 1
    if count >= counter[0]:
        counter[0] = count
        a_b = (a, b)

# primes under 1000
primes = []
for n in range(2, 1000):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        primes.append(n)

for a in range(-1000, 1000):
    for b in primes:          # only prime b
        test(a, b)

print(a_b)        # best (a, b)
print(a_b[0]*a_b[1]) # length of prime run
