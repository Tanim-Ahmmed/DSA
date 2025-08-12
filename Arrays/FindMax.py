# finding max number of an array 
def findMax(arr):
    Max = arr[0]
    for i in arr:
        if i > Max:
            Max = i
    return Max
print(findMax([1,2,3,4,5,6,3,5,7,3,2,1]))