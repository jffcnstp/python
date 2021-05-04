def SelectionSort(listgiv):
   

    for i in range(len(listgiv)):
        swap=i
        for j in range(i+1,len(listgiv)):
            if(listgiv[swap]>listgiv[j]):
                swap=j
        listgiv[i],listgiv[swap]=listgiv[swap],listgiv[i]
    return listgiv

print(SelectionSort([3,5,7,8,1,4,3,2,15,9,-2]))


