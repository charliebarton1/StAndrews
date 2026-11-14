def fact(x):
    tot = 1 
    for i in range(1,x):
        tot *= i
    return tot
value = fact(100) 
List = [int(d) for d in str(value)]
total = 0 
for i in range(len(str(value))):
    total  += List[i]
print(total)
