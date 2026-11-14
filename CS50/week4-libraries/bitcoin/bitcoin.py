import requests
import sys

def main():
    n = get_n()
    try:
        value = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=23fdfa1a89c04ff05a68ad3a17d5e22f1de9170aaaccddf6015d1b3d6afe7074" )
        btc = value.json()
    except requests.RequestException:
       sys.exit("program failed to work")
    dat = btc["data"]
    val = dat['priceUsd']
    tot = float(val) * float(n)
    print(f"${tot:,.4f}")


def get_n():
    try:
        x = float(sys.argv[1])
        return x
    except:
        sys.exit("Error, no float entered after calling python file")

main()

