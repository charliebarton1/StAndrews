x = input("Input the maths").strip()
x, y, z= x.split(" ")
x = int(x)
z= int(z)
if y == "+":
    n = x + z
elif y == "-":
    n = x-z
elif y == "*":
    n = x*z
elif y == "/":
    n = x/z
n = float(n)


print(round(n,1),end="")
