

import operator
import math
import random
import pickle

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp
import os
import time

#rectangle(arg1,arg2,arg3,arg4)

pset = gp.PrimitiveSet("main", 0)
pset.addPrimitive(max, 2)
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.mul, 2)
pset.addTerminal(1)
#pset.renameArguments(ARG0="x")
#pset.renameArguments(ARG1="y")

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin, pset=pset)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genFull, pset=pset, min_=2, max_=3)
toolbox.register("individual", tools.initIterate, creator.Individual,
                 toolbox.expr)

nb_inds = 16
nb_args = 4
args = [ ] # Arguments
inds = [ ] # Individuals

for nb_ind in range(nb_inds):
#     print dir(ind)
#func = gp.compile(ind,pset)
#print func
     ind = [toolbox.individual() for x in range(nb_args)]
     args.append([gp.compile(x, pset) for x in ind])
     inds.append([ind for x in ind])

pickle.dump( args, open( "args.p", "wb" ) )
#pickle.dump( inds, open( "inds.p", "wb" ) )


FILENAME_ARGS = "args.p"
FILENAME_SELECT = "select.p"


def makenewinds(inds, select, nb_inds, nb_args):
    """
    parameters:
        inds: list of individu
        select: list of boolean selector
    """
    selectioned = [ind for ind,sel in zip(inds,select) if sel == 1]

    ind1 = ind[0][0]
    print "first individual"
    print ind1

    ind2 = ind[0][1]
    print "second individual"
    print ind2

    filho = tools.cxOnePoint(ind1,ind2)
    print "FILHO"
    for f in filho:
        print f   

    arguments = []
    selectioned = zip(*selectioned)
    print len(selectioned)
    for selection in selectioned:
        print len(selection)
        for i in range(len(selection)):
            print selection[i][0]

while True:
    # # Evaluate fitness function
    # Saves for processing part
    print("Saving new population...")
    pickle.dump(args, open(FILENAME_ARGS, "wb"))

    # Waits for processing:
    while True:
        if os.path.isfile(FILENAME_SELECT):
            with open(FILENAME_SELECT, "r") as f:
                select = eval(f.read())
            os.unlink(FILENAME_SELECT)
            break
        else:
            time.sleep(0.01)

    args = [ ]
    inds = makenewinds(inds, select, nb_inds, nb_args)
    inds = zip(*inds) # reshape the list

    for ind in inds:
        args.append([gp.compile(x[0], pset) for x in ind])
    print args
    #args.append([gp.compile(ind, pset) for ind in inds])
    #print inds


#print "AHAHAHAAHAHA"*10
#print "first individual"
#print ind1



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

