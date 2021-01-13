import random as rnd

CH_100 = 9608
CH_75 = 9619
CH_50 = 9618
CH_25 = 9617

def random_image(x=25, y=25, mode=0):
    img = []

    for row in range(y):
        img.append([])
        for col in range(x):
            if mode == 0:
                pix = rnd.randint(0, 1)
                if pix == 1:
                    pix = chr(CH_100)
                else:
                    pix = " "
            elif mode == 1:
                pix = rnd.randint(0,4)
                if pix == 4:
                    pix = chr(CH_100)
                elif pix == 3:
                    pix = chr(CH_75)
                elif pix == 2:
                    pix = chr(CH_50)
                elif pix == 1:
                    pix = chr(CH_25)
                elif pix == 0:
                    pix = " "
            img[row].append(pix)

    return img

def print_image(img):
    for row in img:
        for pix in row:
            print(pix, end="")
        print("")

def main():
    img = random_image(x=80)
    print_image(img)

    print("")

    img = random_image(x=80, mode=1)
    print_image(img)

if __name__ == "__main__":
    main()