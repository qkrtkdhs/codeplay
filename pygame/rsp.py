import random

uc = 0
cc = 0

gbb = ["gw","bw", "b" ]

running = True

while running:
    uc = input("내라")
    cc = random.choice(gbb)
    print(cc)

    if uc == "off":
        running = False
        print("end")
    elif uc == "gw":
        if cc == "gw":
            print("무")
        if cc == "bw":
            print("패")
        if cc == "b":
            print("승")
    elif uc == "bw":
        if cc == "gw":
            print("승")
        if cc == "bw":
            print("무")
        if cc == "b":
            print("패")
    elif uc == "b":
        if cc == "gw":
            print("패")
        if cc == "bw":
            print("승")
        if cc == "b":
            print("무")