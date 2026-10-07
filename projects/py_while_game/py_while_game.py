import random

tasodifiy_son = random.randint(1, 101)

while True:

    player = int(input("1 dan 100 gacha son kiriting : "))

    if player == tasodifiy_son:
        print("topdingiz - wictory")
        break
    if player < tasodifiy_son:
        print("son kattaroq edi")
    else:
        print("son kichikroq edi")