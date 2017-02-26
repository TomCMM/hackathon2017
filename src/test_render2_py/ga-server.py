import ga
import os
import time
import pickle

FILENAME_IN = "server-in.txt"
FILENAME_OUT = "server-out.txt"

print("****************************")
print("* Genetic Algorithm Server *")
print("****************************")
print("Input filename: {}".format(FILENAME_IN))
print("")
print("    This file will be used for two things:")
print("        a) tell the GA to generate its first population (token: 'first')")
print("        b) tell the GA the values of the fitness functions (token: 'fitness'")
print("")
print("Outut filename: {}".format(FILENAME_OUT))
print("")
print("    This file will be used for one thing:")
print("        a) pass the encoded individuals to the client")

os.unlink(FILENAME_IN)
os.unlink(FILENAME_OUT)

ST_EXP_FIRST = 'first'
ST_EXP_FITNESS = 'fitness'

state = ST_EXP_FIRST

def read_file(filename):
    with open(filename, "r") as f:
        return f.readlines()
    os.unlink(filename)


while True:
    time.sleep(.01)
    if os.path.isfile(FILENAME_IN):
        lines = read_file(FILENAME_IN)
        token = lines[0]
        if not (state == token):
            raise RuntimeError("Wrong token: expecting '{}', received '{}'".format(state, token))
        elif state == ST_EXP_FITNESS:
            pop = ga.process_fitnesses([eval(s for s in lines[1:])])
            pickle.dump(pop, open(FILENAME_OUT, "wb"))
        elif state == ST_EXP_FIRST:
            pop = ga.get_first_population()
            pickle.dump(pop, open(FILENAME_OUT, "wb"))
