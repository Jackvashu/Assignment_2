from random import sample


sampleLst = [(2,5),(1,2),(4,4,),(2,3),(2,1)] # sample list of printing
for i in range(len(sampleLst)):  # for loop list range
    for j in range(len(sampleLst)): # for loop for list range in tuple
        if sampleLst[i][1] < sampleLst[j][1]: # check if last element of i is smaller then j
            sampleLst[i],sampleLst[j] = sampleLst[j],sampleLst[i]  # Swapping the Value without 3 variable

print("Sorted list are : {}".format(sampleLst))  # printing the sorted list 