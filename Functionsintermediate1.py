import random
def randInt(min=0   , max=100   ):
    if(min>max or max<min):
        return False
    if(min==max):
        return min
    num = random.randrange(min,max,1)
    return num
print(randInt())
print(randInt(max=-3))
print(randInt(min=0))
print(randInt(min=50, max=50))