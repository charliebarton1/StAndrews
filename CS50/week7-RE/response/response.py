from validator_collection import validators

def main():
    if valid(input("What is your email? ")):
        print("Valid")
    else:
        print("Invalid")
def valid(e):
    try:
        validators.email(e)
        return True
    except:
        return False

main()


