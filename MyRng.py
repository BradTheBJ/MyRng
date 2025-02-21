import pygame
import math
import random
import time

higest_raritiy = 32

pity = 0

common = int(higest_raritiy / 2)
uncommon = int(higest_raritiy / 4)
good = int(higest_raritiy / 8)
great = int(higest_raritiy / 16)
amazing = int(higest_raritiy / 32)

while True:
    time.sleep(1)
  
    pity += 1

    if pity == 10:
        print("2x luck")
        rng = random.randint(1, int(higest_raritiy / 2))
        pity == 0
    else:
        rng = random.randint(1, higest_raritiy)

    print(rng)

    if rng > common:
        print("common")
    elif rng > uncommon:
        print("uncommon")
    elif rng > good:
        print("good")
    elif rng > great:
        print("great")
    else:
        print("amazing")