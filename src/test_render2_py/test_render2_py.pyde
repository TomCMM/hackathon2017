import math
import random


def render_individual(individual, x0, y0, scale_):
    """
    Renders individual on screen
    
    Args:
        individual: sequence with pair number of elements.
            [(angle_in_degrees, step_in_pixels), ...]
        x0, y0: coordinates of the origin
        scale_: multiplier
    """
    x, y = 0, 0
    xmin, ymin, xmax, ymax = 99999, 99999, -99999, -99999
    
    # first pass to determine width & height
    for i in range(0, len(individual), 2):
        angle_rad = individual[i]*math.pi/180
        step = individual[i+1]
        xnew = x+step*scale_*cos(angle_rad)
        ynew = y+step*scale_*sin(angle_rad)
        x, y = xnew, ynew
        xmin = min(x, xmin)
        xmax = max(x, xmax)
        ymin = min(y, ymin)
        ymax = max(y, ymax)
        
    w, h = xmax-xmin, ymax-ymin
    
    x = x0+(fig_width-w)/2-xmin
    y = y0+(fig_width-h)/2-ymin
    stroke(0)
    fill(0)
    ellipse(x, y, 4, 4) 
    for i in range(0, len(individual), 2):
        angle_rad = individual[i]*math.pi/180
        step = individual[i+1]
        xnew = x+step*scale_*cos(angle_rad)
        ynew = y+step*scale_*sin(angle_rad)
        line(x, y, xnew, ynew)
        x, y = xnew, ynew

                
def random_individual(num_steps):
    ret = []
    for i in range(num_steps):
        ret.append(random.randint(0, 360))  # angle
        ret.append(random.randint(1, 20))  # step
    return ret
        
        

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
POPULATION_SIZE = 25
SPACING = 10  # spacing between figures
nc, nr = get_num_cols_rows(POPULATION_SIZE)
fig_width = int((WIDTH-SPACING*(nc+1))/nc)
fig_step = (WIDTH-SPACING*(nc+1))/nc+SPACING  # note that this is a float
scale_ = fig_width*SCALE_K
print("Number of columns: {}; number of rows: {}".format(nc, nr))

current_k = -1
clicked_left = False
clicked_right = False

population = []
selects = []
GREEN = 1
RED = 2
COLOR255 = color(255, 255, 255)
for i in range(POPULATION_SIZE):
    population.append(random_individual(NUM_STEPS))
    selects.append(0)

def setup():
    size(600, 600)
    stroke(0)
    background(220)

def draw():
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
            ind = population[k]
            render_individual(ind, xborder, yborder, scale_)
            noClip()
            xborder += fig_step
            k += 1
        yborder += fig_step
        
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
        