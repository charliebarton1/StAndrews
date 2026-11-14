import sys
from PIL import Image, ImageOps
def main():
    if get_images(sys.argv) == True:
        t_shirt = Image.open("shirt.png")
        size = t_shirt.size
        with Image.open(sys.argv[1]) as im:
            im = ImageOps.fit(im, size)
            im.paste(t_shirt, t_shirt)
            im.save(sys.argv[2])


def get_images(x):
    if len(x) == 3:
        if ".jpg" or ".jpeg" or ".png" in x[1]:
            try:
                images = Image.open(x[1])
            except:
                sys.exit("File 1 does not exist")
            if x[1].split(".")[-1] == x[2].split(".")[-1]:
                return True
            else:
                sys.exit("Not same file types")
        else:
            sys.exit("File 1 was not the right file type")
    elif len(x)> 3:
        sys.exit("Too many command line arguments")
    else:
        sys.exit("Too few command line arguments")

main()


