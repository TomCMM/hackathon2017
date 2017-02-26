import random


N = 10

WID, HEI = 1000, 620
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
        KC = .6
        background(int(200*KC), int(200*KC), int(220*KC))
        x = 0
        bottom = HEI
        K = .65
        min_height = 100*K
        max_height = 300*K
        max_width = 100*K
        min_width = 50*K
        max_c = 255
        objs = []
        for i in range(int(HEI/MIN_HEIGHT)):
            x = 0
            while True:
                c = color(r0(int(max_c)), r0(int(max_c)), r0(int(max_c)))            
                w, h = r(int(min_width), int(max_width)), r(int(min_height), int(max_height))
                rect(x, bottom-h, w, h)
                objs.append([c, x, bottom-h, w, h])
                x += w
                if x >= WID:
                    break
                
            bottom -= min_height
            max_height *= .9
            max_width *= .9
            min_height *= .9
            min_width *= .9
            max_c *= .95
            if max_height <= MIN_HEIGHT or max_width <= MIN_WIDTH:
                break
        
        for c, x, y, w, h in reversed(objs):
            fill(c)
            rect(x, y, w, h)

        flag_draw = False

    
def mousePressed():
    global flag_draw
    flag_draw = True