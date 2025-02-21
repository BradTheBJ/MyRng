import pygame
import math
import random
import time

higest_raritiy = 8

pity = 0

common = int(higest_raritiy / 2)
uncommon = int(higest_raritiy / 4)
good = int(higest_raritiy / 8)

while True:
    pity += 1

    if pity == 10:
        print("2x luck")
        rng = random.randint(1, int(higest_raritiy / 2))

    else:
        rng = random.randint(1, higest_raritiy)

    time.sleep(1)

    if rng >= 4:
        print("common 1/", common)

    elif rng >= 2:
        print("uncommon 1/", uncommon)

    elif rng >= 1:
        print("good 1/", good)


    