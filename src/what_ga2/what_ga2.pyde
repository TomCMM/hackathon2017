import random

N = 10

WID, HEI = 1000, 120


r = random.randint
r0 = lambda x: random.randint(0, x)

def setup():
    size(WID, HEI)
    background(255)
    noStroke()

flag_draw = False

def draw():
    global flag_draw
    if flag_draw:
        background(255)
        x = 0
        for i in range(15):
            c = color(r0(255), r0(255), r0(255))
            fill(c)
            
            y, w, h = r0(HEI), r(10, 120), r(10, 120)
            rect(x, HEI-h, w, h)
            x += w
        flag_draw = False
    
    
def mousePressed():
    global flag_draw
    flag_draw = True