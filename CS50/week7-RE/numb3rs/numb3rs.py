import re
import sys


def main():
    user = input("IPv4 Address: ")
    ans = validate(user)
    print(ans)
    if ans == False:
        sys.exit(1)



def validate(ip):
    pattern = r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
    match = re.fullmatch(pattern,ip)
    if match:
        return True
    else:
        return False








if __name__ == "__main__":
    main()
