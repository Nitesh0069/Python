# A demo program to run a functions randomly
# this does teachs me to use random.choice to run a functions randomly


import random

def f1():
    return("f1 is running...")
          
def f2():
    return("f2 is running...")

def f3():
    return("f3 is running...")

def f4():
    return("f4 is running...")
    
# this part works when we use random.choice  and give 1 among 4 of the functions only    
# f_selector= (f1,f2,f3,f4)

# random_value = random.choice(f_selector)

# result = random_value()
# print(result)
# here is where i discover the use case of random.shuffle to shuffle a list randomly

f_shuffler = [f1,f2,f3,f4]

random.shuffle(f_shuffler)

for func in f_shuffler:
    print(func()) 
   