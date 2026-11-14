x = input("Input file name: ").lower().strip()
x = x.split(".")
if x[-1]=="gif":
    print("image/gif", end="")
elif x[-1]=="jpg":
    print("image/jpeg", end="")
elif x[-1]=="jpeg":
    print("image/jpeg", end="")
elif x[-1]=="png":
    print("image/png", end="")
elif x[-1]=="pdf":
    print("application/pdf", end="")
elif x[-1]=="txt":
    print("text/plain", end="")
elif x[-1]=="zip":
    print("application/zip", end="")
else:
    print("application/octet-stream", end="")

