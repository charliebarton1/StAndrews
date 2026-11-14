from pyfiglet import Figlet
import sys

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1]== "--font":
        try:
            f = Figlet(font = sys.argv[2])
        except:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) > 3:
    sys.exit("Invalid usage")
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")
else:
    f = Figlet(font ="epic")
x = input("Type anything: ")
print(f.renderText(x))



