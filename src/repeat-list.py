import random

ll = [1, 2, 3]

pop_size = 16

pop = []
for i in range(pop_size):
    idx = random.randint(0, len(ll)-1)
    pop.append(ll[idx])
    
    
print(pop)
