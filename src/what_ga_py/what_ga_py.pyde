import random

N = 10

WID, HEI = 800, 800

size(600, 600)
r = random.randint
r0 = lambda x: random.randint(0, x)

background(255)
noStroke()

for i in range(100):
    c = color(r0(255), r0(255), r0(255))
    fill(c)
    rect(r0(WID), r0(HEI), r(10, 120), r(10, 120))
    