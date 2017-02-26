

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

#rectangle(arg1,arg2,arg3,arg4)

pset = gp.PrimitiveSet("main", 0)
pset.addPrimitive(max, 2)
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.mul, 2)
pset.addTerminal(10)
#pset.renameArguments(ARG0="x")
#pset.renameArguments(ARG1="y")

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin, pset=pset)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genFull, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual,
                 toolbox.expr)

nb_inds = 16
nb_args = 4
pop = [ ]

for nb_ind in range(nb_inds):
#     print dir(ind)
#func = gp.compile(ind,pset)
#print func
     pop.append([gp.compile(toolbox.individual(),pset) for x in range(nb_args)])
print pop
pickle.dump( pop, open( "pop.p", "wb" ) )


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

