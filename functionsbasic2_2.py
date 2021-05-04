def Countdown(num):
    newlist=[]
    for i in range(num,-1,-1):
        newlist.append(i)
    return newlist
print(Countdown(4))

def PrintandReturn(twolist):
    print(twolist[0])
    return twolist[1]
print(PrintandReturn([1,2]))

def FirstandLength(listvar):
    return listvar[0]+len(listvar)

print(FirstandLength([0,1,2,3]))


def GreaterThanElement2(listvar):
    newlist=[]
    count=0
    for val in listvar :
        if val > listvar[1]:
            newlist.append(val)
            count+=1
    print(count)
    return newlist
print(GreaterThanElement2([1,2,4,1,3,5]))


def ThislengthThatvalue(num1,num2):
    newlist=[]
    for i in range(num1):
        newlist.append(num2)
    return newlist

print(ThislengthThatvalue(3,5))

