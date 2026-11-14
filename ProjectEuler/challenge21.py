def sum_divisors(x):
    divs= 0
    for i in range(1,x):
        if x % i == 0:
            divs += i 
    return divs
List =[]
for j in range (1,10000):
    j_ = sum_divisors(j)
    k_= sum_divisors(j_)
    if j and j_<= 10000:
        if j ==k_ and j not in List and j!=j_:
            List.append(j)
            List.append(j_) 
print(sum(List))

            
        
        
    
