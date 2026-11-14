var = input("how would you like to greet me?")
var = var.lower().strip()
if var.split(",")[0]=="hello":
    print("$0")
elif var[0] == "h":
    print("$20")
else:
    print("$100")
