import math
import random
import copy

    

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
NUM_STEPS = 50
POPULATION_SIZE = 9
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


ST_NEXT = 1
ST_SHOWING = 2

FILENAME_POP = "pop.p"

state = ST_NEXT
g = -1

def draw():
    global g, state, population, selects
    if state == ST_SHOWING:
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
    elif state == ST_NEXT:
        if g == -1:
            pass
        else:
            next = []
            snext = []
            neutral = []
            ngreen = 0
            flag_green = False
            for grade, ind in zip(selects, population):
                if grade == GREEN:
                    next.append(ind)
                    snext.append(GREEN)
                    ngreen += 1
                    flag_green = True
                    
                    if ngreen == 2 and len(next) <= POPULATION_SIZE-2:
                        ch0, ch1 = bang(next[-2], next[-1], .1)
                        print("BANGED 2")
                        next.append(ch0)
                        next.append(ch1)
                        snext.append(0)
                        snext.append(0)
                        ngreen = 0
                        
                    if len(next) < POPULATION_SIZE:
                        next.append(messup(ind, .5, 50))
                        snext.append(0)
                elif grade != RED:
                    if len(next) < POPULATION_SIZE:
                        if random.random() < .5:
                            neutral.append(messup(ind, .3, 5))

            j = -1
            for ind in neutral:
                if len(next) == POPULATION_SIZE:
                    break
                if flag_green:
                    while True:
                        j += 1
                        if j == POPULATION_SIZE-1:
                            j = 0
                        if selects[j] == GREEN:
                            roos = population[j]
                            break
                    next.append(mix1(roos, ind))
                else:
                    next.append(random_individual(NUM_STEPS))
                snext.append(0)
                                            
            j = -1
            for i in range(POPULATION_SIZE-len(next)):
                if not flag_green or random.random() < .5:
                    next.append(random_individual(NUM_STEPS))
                else:
                    while True:
                        j += 1
                        if j == POPULATION_SIZE-1:
                            j = 0
                        if selects[j] == GREEN:
                            roos = population[j]
                            break
                    next.append(mix1(roos, random_individual(NUM_STEPS)))
                snext.append(0)

            population = next
            selects = snext
        g += 1
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
        state = ST_NEXT
        
def messup(individual, prob, num):
    ret = copy.deepcopy(individual)
    N = len(individual)/2
    for i in range(num):
        if random.random() <= prob:
            which = random.randint(0, N-1)
            
            if random.random() < .5:
                ret[(i-1)*2] += (random.random()-.5)*10
            else:
                ret[(i-1)*2+1] += (random.random()-.5)*20
    
    return ret

#def bang(ind0, ind1, prob):
#    # prob: probability **for each element** (must be low!!)
#    ret0, ret1 = copy.deepcopy(ind0), copy.deepcopy(ind1)
#    for i in range(len(ind0)):
#        if random.random() < prob:
#            temp = ret0[i]
#            ret0[i] = ret1[i]
#            ret1[i] = temp
#    return ret0, ret1

def bang(ind0, ind1, prob):
    # prob: probability **for each element** (must be low!!)
    ret0, ret1 = copy.deepcopy(ind0), copy.deepcopy(ind1)
    i = 0
    N = len(ind0)/2
    qtd = 0
    for i in range(0, len(ind0), 2):
        if qtd == 0:
            if random.random() < prob:
                qtd = random.randint(1, 15)
        if qtd > 0:
            temp = ret0[i]
            ret0[i] = ret1[i]
            ret1[i] = temp
            temp = ret0[i+1]
            ret0[i+1] = ret1[i+1]
            ret1[i+1] = temp
            qtd -= 1 
    return ret0, ret1

def mix1(ind0, ind1):
    ret = copy.deepcopy(ind0)
    qtd = 0
    for i in range(0, len(ind0), 2):
        if qtd == 0:
            qtd = random.randint(1, 15)
            if random.random() < .5:
                ind = ind0
            else:
                ind = ind1
        
        ret[i] = ind[i]
        ret[i+1] = ind[i+1]
        qtd -= 1
    return ret
                
