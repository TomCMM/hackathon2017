import math
import random
import pickle
import os


def render_individual(individual, x0, y0, scale_):
    """
    Renders individual on screen
    
    Args:
        individual: sequence with pair number of elements.
            [(angle_in_degrees, step_in_pixels), ...]
        x0, y0: coordinates of the origin
        scale_: multiplier
    """    
    
    x, y, w, h = individual
    rect(x0, y0, scale_*w, scale_*h)

                         

def get_num_cols_rows(size_):
    """Calculates number of rows and columns based on population size
    """
    num_rows = int(math.sqrt(POPULATION_SIZE))
    
    while num_rows >= 1:
        num_cols = size_/num_rows
        if num_cols-int(num_cols) < 0.01:
            break
        num_rows -= 1
    return num_cols, num_rows

WIDTH, HEIGHT = 600, 600
SCALE_K = 1./250
NUM_STEPS = 100


#os.chdir("/home/j/Documents/projects/garoa/h/hackathon2017/src/ga/test_tom")
os.chdir("/root/hack/hackathon2017/src/ga/test_tom")
SPACING = 10  # spacing between figures

current_k = -1
clicked_left = False
clicked_right = False

GREEN = 1
RED = -1
COLOR255 = color(255, 255, 255)

ST_EXP_POP = 1
ST_SHOWING = 2

FILENAME_POP = "args.p"

state = ST_EXP_POP


def setup():
    size(600, 600)

def draw():
    global nr, nc, fig_width, fig_step, scale_, state, POPULATION_SIZE, selects, pop
    if state == ST_SHOWING:
        stroke(0)
        background(220)
        yborder = SPACING
        k = 0
        current_k = -1
        for j in range(nr):
            xborder = SPACING
            for i in range(nc):
                fill_ = COLOR255
                if xborder <= mouseX <= xborder+fig_width and yborder <= mouseY <= yborder+fig_width:
                    fill_ = lerpColor(color(255, 255, 0), fill_, .5)
                    
                if selects[k] == RED:
                    # red, don't like it
                    fill_ = lerpColor(lerpColor(color(255, 0, 0), COLOR255, .5), fill_, .5)
                elif selects[k] == GREEN:
                    # green, like it
                    fill_ = lerpColor(lerpColor(color(0, 255, 0), COLOR255, .5), fill_, .5)
                
                fill(fill_)
                rect(xborder, yborder, fig_width, fig_width)
                clip(xborder, yborder, fig_width, fig_width)
                ind = pop[k]
                render_individual(ind, xborder, yborder, scale_)
                noClip()
                xborder += fig_step
                k += 1
            yborder += fig_step
    elif state == ST_EXP_POP:
        stroke(255)
        background(30, 30, 30)
        text("Waiting for next population ...", 10, 20)
        if os.path.isfile(FILENAME_POP):
            pop = pickle.load(open(FILENAME_POP, "r"))
            os.unlink(FILENAME_POP)
            POPULATION_SIZE = len(pop)
            nc, nr = get_num_cols_rows(POPULATION_SIZE)
            fig_width = int((WIDTH-SPACING*(nc+1))/nc)
            fig_step = (WIDTH-SPACING*(nc+1))/nc+SPACING  # note that this is a float
            scale_ = fig_width*SCALE_K
            print("Number of columns: {}; number of rows: {}".format(nc, nr))
            
            selects = []
            for i in range(POPULATION_SIZE):
                selects.append(0)
            state = ST_SHOWING
                        
                        
def mouse_to_k(x, y):
    k = -1
    x0 = (x-SPACING) % fig_step
    if x0 <= fig_width:
        y0 = (y-SPACING) % fig_step
        if y0 <= fig_width:
            k = (x-SPACING)/fig_step+(y-SPACING)/fig_step*nc
    return k             
        
def mouseClicked():
    k = mouse_to_k(mouseX, mouseY)
    print("k = {}; mouseButton = {}".format(k, mouseButton))
    if k == -1:
        return
    if mouseButton == 37:  # left
        print("RELECTED GREEN")
        selects[k] = GREEN
    elif mouseButton == 39:  # right
        print("RELECTED RED")
        selects[k] = RED
    elif mouseButton == 3:
        selects[k] = 0
        
def keyPressed():
    global state
    print("OLHOLHO", keyCode)
    if keyCode == 10:
        print(selects)
        with open("select.p", "w") as f:
            f.write(str(selects))
            
        print("Created file select.p")
        state = ST_EXP_POP
        