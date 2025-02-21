import pygame
import math
import random
import time


higest_raritiy = 8
rng = random.randint(1, higest_raritiy)

common = higest_raritiy/2
uncommon = higest_raritiy/4
good = higest_raritiy/8

while True:
    random.randint(1, higest_raritiy)
    print(rng)
    time.sleep(1)

    if  rng >= 4:
        print("common")

    elif  rng >= 2:
        print("uncommon")

    elif  rng >= 1:
        print("good")


    