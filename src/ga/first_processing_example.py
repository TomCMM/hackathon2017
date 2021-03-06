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
selection = [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

pset = gp.PrimitiveSet("MAIN", 1) # number of input
pset.addPrimitive(operator.add, 2) # addition operator
pset.renameArguments(ARG0='x') # rename the input variable

creator.create("FitnessMin", base.Fitness, weights=(-1.0,)) # minimum fitness
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin) # create the individual


toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

def evalSymbReg(individual, points):
    # Transform the tree expression in a callable function
    func = toolbox.compile(expr=individual)
    # Evaluate the mean squared error between the expression
    # and the real function : x**4 + x**3 + x**2 + x
    #print "="*80
    #print dir(population)
    #print individual.index
    #print "="*80
    sqerrors = ((func(x) - x**4 - x**3 - x**2 - x)**2 for x in points)
    return math.fsum(sqerrors) / len(points),

def userselection(selection):
    return selection

toolbox.register("evaluate",evalSymbReg , points=[x/10. for x in range(-10,10)])
#toolbox.register("evaluate",
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

if __name__ == "__main__":
    random.seed(2)
    nb_epoch = 1

    pop = toolbox.population(n=16)
    for p in pop:
    	print p
    print len(pop)
   # hof = tools.HallOfFame(nb_epoch)
 #   print hof 
    
    #stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    #stats_size = tools.Statistics(len)
    #mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    #mstats.register("avg", numpy.mean)
    #mstats.register("std", numpy.std)
    #mstats.register("min", numpy.min)
    #mstats.register("max", numpy.max)

  #  pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, nb_epoch, halloffame=hof, verbose=True)

  #  print "HALL OF FAME"
  #  print "*"*80
  #  print len(hof)
  #  print "*"*80

   # print hof
   # for i,h in enumerate(hof):
#	print "generation --" + str(i)
#	print h
    # print log
#    print pop, log, hof

    #print hof[0]

