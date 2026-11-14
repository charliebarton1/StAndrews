def N_2(x):
    if x % 2 == 0:
        return x/2
    else:
        return False
def N(x):
    return 3*x + 1
List = []
Num = []
for i in range(1000000):
    count = 0
    n = i 
    while n != 1:
        count += 1
        if N_2(n) == False:
            n = N(n)
        else:
            n = N_2(n)
    List.append(count)
    Num.append(n) 
ind = List.index(max(List))
print(ind) 
print(List[ind],Num[ind])


        
    
