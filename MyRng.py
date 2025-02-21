import pygame
import math
import random


higest_raritiy = 8
rng = random.randint(1, higest_raritiy)

common = higest_raritiy/2
uncommon = higest_raritiy/4
good = higest_raritiy/8

while True:
    random.randint(1, higest_raritiy)

    if  rng >= 4:
        print("common")

    if  rng >= 2:
        print("uncommon")

    if  rng >= 1:
        print("good")


    