

import operator
import math
import random
import pickle
import copy
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
#pset.addPrimitive(max, 2)
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
     inds.append([x for x in ind])

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
    
    newinds = []
    
    for nb_arg in range(nb_args):
        args = [sel[nb_arg] for sel in selectioned]
        while len(args) < nb_inds:
            for father, mother in zip(args[:-1], args[1:]):
                print len(father)
                args.append(mother)
                args.append(father)
                son1 = copy.deepcopy(father)
                son2 = copy.deepcopy(mother)
                tools.cxOnePoint(son1, son2)
                print "Father"
                print father
                print gp.compile(father, pset)
                print "Mother"
                print mother
                print gp.compile(mother, pset)
                print son1
                print gp.compile(son1, pset)
                print son2
                print gp.compile(son2, pset)
                args.append(son1)
                args.append(son2)

        args = args[:nb_inds] # select only nb_ind individus
        newinds.append(args)
    return newinds
    #print len(selectioned)

# Generation loop
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

    print select

    args = [ ]
    inds = makenewinds(inds, select, nb_inds, nb_args)
    #print len(inds)
    #print len(zip(*inds))
    inds = zip(*inds)
    #print len(inds)
    for ind in inds:
        #print len(ind)
        #print gp.compile(ind[0][0], pset)
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

