import math
while(True):
    radius = input('Sisesta raadius:')

    ümbermõõt = math.pi * float(radius) * 2
    pindala = math.pi * float(radius) * float(radius)

    print('Pindala on: ', round(pindala),"cm2")

    print('Ümbermõõt on: ', round(ümbermõõt),"cm")
