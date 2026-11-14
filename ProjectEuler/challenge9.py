def is_pythag(x, y, z):
    if x**2 + y**2 == z**2:
        return True
    else:
        return False
valid = False 
P = []
L = []
tot = 0 

for a in range(1,600):
    for b in range(1,600):
        for c in range(1,600):
            tot = a + b + c
            if is_pythag(a,b,c):
                tot = a + b + c
                P.append(tot)
                L.append(a*b*c)
                break
        if 1000 in P:
            break  # break from b loop
    if 1000 in P:
        break  # break from a loop
position = P.index(1000)
print(L[position])


            

        
    









  
