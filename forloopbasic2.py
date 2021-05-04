def posToBig(listgiven):
    for i in range(len(listgiven)):
        if listgiven[i]>0:
            listgiven[i]="big"
    return listgiven
print(posToBig([-1,0,4,3,0,-2]))

def CountPos(listgiven):
    count=0
    for val in listgiven:
        if val>0:
            count+=1
    listgiven[len(listgiven)-1]=count
    return listgiven
print(CountPos([1,2,3,4,-1]))

def SumTotal(listgiven):
    sum=0
    for val in listgiven:
        sum+=val
    return sum
print(SumTotal([1,2,3]))

def Average(listgiven):
    sum=0
    sum=0
    for val in listgiven:
        sum+=val
    return sum/(len(listgiven))
print(Average([1,2,3,3]))

def Length(listgiven):
    return len(listgiven)

print(Length([0,1]))

def Minimum(listgiven):
    if(len(listgiven)==0):
        return False

    else:
        min=listgiven[0]
        for val in listgiven:
            if min>val:
                min=val
    return min
print(Minimum([]))
print(Minimum([0,1,2,-3,4]))

def Maximum(listgiven):
    if(len(listgiven)==0):
        return False
    
    else:
        max=listgiven[0]
        for val in listgiven:
            if max<val:
                max=val
    return max
print(Maximum([]))
print(Maximum([0,1,2,-3,4]))

def FullAnalysis(listgiven):
    max=listgiven[0]
    min=listgiven[0]
    sum=0
    for val in listgiven:
        if(max<val):
            max=val
        if(min>val):
            min=val
        sum+=val
    analyzeDict={}
    analyzeDict["sumTotal"]=sum
    analyzeDict["average"]=sum/len(listgiven)
    analyzeDict["minimum"]=min
    analyzeDict["maximum"]=max
    analyzeDict["length"]=len(listgiven)
    return analyzeDict

print(FullAnalysis([1,2,4,6,-3,4]))

def ListReverse(listgiven):
    temp=0
    for i in range(len(listgiven)):
        if i >len(listgiven)/2:
            return listgiven
        
        temp=listgiven[i]
        listgiven[i]=listgiven[len(listgiven)-i-1]
        listgiven[len(listgiven)-i-1]=temp

print(ListReverse([1,2,3,4,5]))