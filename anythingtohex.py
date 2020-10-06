import os
import random
import time
import math

for i in range(10):
    mathprob = random.randint(1, 500)
    yeah = (hex(mathprob))
    print(bin(mathprob))
    print(str(yeah))
    #print(mathprob + mathprob)
    if mathprob > 500:
        print("fat")

