import random
import time

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

flag_redo = True

def draw():
    global flag_redo, objs
    if flag_redo:
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
            oo = []
            while True:
                c = color(r0(int(max_c)), r0(int(max_c)), r0(int(max_c)))            
                w, h = r(int(min_width), int(max_width)), r(int(min_height), int(max_height))
                rect(x, bottom-h, w, h)
                oo.append([c, x, bottom-h, w, h, 0])
                x += w
                if x >= WID*1.1:
                    break
            objs.append(oo)
            bottom -= min_height
            max_height *= .9
            max_width *= .9
            min_height *= .9
            min_width *= .9
            max_c *= .95
            if max_height <= MIN_HEIGHT or max_width <= MIN_WIDTH:
                break
        flag_redo = False
    
    KC = .6
    background(int(200*KC), int(200*KC), int(220*KC))
    k = 1.
    for oo in reversed(objs):
        x = oo[0][1]
        for i, (c, _, y, w, h, rx) in enumerate(oo):
            fill(c)
            rx += (random.random()-.5)*k
            oo[i][-1] = rx
            weff = w+rx
            rect(x, y, weff, h)
            x += weff
        k /= .90
    time.sleep(0.1)
    
    
def mousePressed():
    global flag_redo
    flag_redo = True