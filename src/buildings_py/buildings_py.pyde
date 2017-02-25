import random


N = 10

WID, HEI = 1000, 410
MIN_HEIGHT = 20
MIN_WIDTH = 10

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
        background(200, 200, 220)
        x = 0
        bottom = HEI
        max_height = 150
        max_width = 50
        objs = []
        for i in range(int(HEI/MIN_HEIGHT)):
            x = 0
            while True:
                c = color(r0(255), r0(255), r0(255))            
                w, h = r(MIN_WIDTH, int(max_width)), r(MIN_HEIGHT, int(max_height))
                rect(x, bottom-h, w, h)
                objs.append([c, x, bottom-h, w, h])
                x += w
                if x >= WID:
                    break
                
            bottom -= MIN_HEIGHT
            max_height *= .9
            max_width *= .9
            if max_height <= MIN_HEIGHT or max_width <= MIN_WIDTH:
                break
        
        for c, x, y, w, h in reversed(objs):
            fill(c)
            rect(x, y, w, h)

        flag_draw = False

    
def mousePressed():
    global flag_draw
    flag_draw = True