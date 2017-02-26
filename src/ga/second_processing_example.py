import operator
import math
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

mousex = [1,2,3,4,5,6,7,8,9,10] # user input
mousey = [1,2,3,4,5,6,7,8,9,10] # user input
selection = [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


def rectangle(arg1, arg2):
    pass


pset = gp.PrimitiveSet("MAIN", 0)


def progn(*args):
    for arg in args:
        arg()

def prog2(out1, out2):
    return partial(progn,out1,out2)

def prog3(out1, out2, out3):
    return partial(progn,out1,out2,out3)

def if_then_else(condition, out1, out2):
    out1() if condition() else out2()


pset = gp.PrimitiveSet("main", 2)
#pset.addPrimitive(max, 2)
pset.addPrimitive(operator.add, 2)
#pset.addPrimitive(operator.mul, 2)
#pset.addTerminal(rectangle, (float,float,float,float))
#pset.addTerminal(3)
#pset.addPrimitive(ant.if_food_ahead, 2)
#pset.addPrimitive(prog2, 2)
#pset.addPrimitive(prog3, 3)
pset.addPrimitive(rectangle, [float,float], float)
#pset.addTerminal(ant.turn_left)
#pset.addTerminal(ant.turn_right)
pset.renameArguments(ARG0="x")
pset.renameArguments(ARG1="y")

#pset.addPrimitive(operator.neg, 1)

#expr = gp.genFull(pset, min_=1, max_=3)
#tree = gp.PrimitiveTree(expr)
#print tree


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin, pset=pset)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genFull, pset=pset, min_=2, max_=3)
toolbox.register("individual", tools.initIterate, creator.Individual,
                 toolbox.expr)

ind1 = toolbox.individual()
print "AHAHAHAAHAHA"*10
print "first individual"
print ind1

#ind2 = toolbox.individual()
#print "second individual"
#print ind2

#filho = tools.cxOnePoint(ind1,ind2)
#print "FILHO"
#for f in filho:
 #   print f
#print len(filho)


#print "#"*100
#print len(filho)
#for f in filho:
    #try:
   # 	f= gp.mutShrink(f)
 #       print f[0]
   # except IndexError:
  #      print "could not perform mutation"
    #print gp.mf
#    print gp.mutShrink(f)



