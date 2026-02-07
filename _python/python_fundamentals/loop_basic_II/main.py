#1
def BiggieSize(arr):
    for x in range(len(arr)):
        if arr[x] > 0:
            arr[x] = "big"
    print(arr)

arr = [-1, 3, 5, -5]
BiggieSize(arr);

#2
def CountPositives(arr):
    counter = 0
    for x in range(len(arr)):
        if arr[x] > 0:
            counter += 1
    
    arr[len(arr) - 1] = counter

    return arr;

arr1 = [-1, 1, 1, 1]
print(CountPositives(arr1))

arr2 = [1, 6, -4, -2, -7, -2]
print(CountPositives(arr2))
#3
def SumTotal(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum

arr1 = [1,2,3,4]
print(SumTotal(arr1));

arr2 = [6,3,-2]
print(SumTotal(arr2))
#4
def Average(arr):
    if len(arr) == 0:
        return 0

    sum = 0
    for x in arr:
        sum += x
    
    return sum / len(arr)

arr = [1,2,3,4]
print(Average(arr))
#5
def Length(arr):
    return len(arr)

arr1 = [37,2,1,-9]
print(Length(arr1))

arr2 = []
print(Length(arr2))

#6
def Minimum(arr):
    if len(arr) == 0:
        return False;
    minimum = arr[0]
    for x in arr:
        if x < minimum:
            minimum = x
    return minimum

arr1 = [37,2,1,-9]
print(Minimum(arr1))

arr2 = []
print(Minimum(arr2))

#7
def Maximum(arr):
    if len(arr) == 0:
        return False;
    maximum = arr[0]
    for x in arr:
        if x > maximum:
            maximum = x
    return maximum

arr1 = [37,2,1,-9]
print(Maximum(arr1))

arr2 = []
print(Maximum(arr2))
#8
def SumTotal(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum

def Average(arr):
    if len(arr) == 0:
        return 0

    sum = 0
    for x in arr:
        sum += x
    
    return sum / len(arr)

def Length(arr):
    return len(arr)

def Minimum(arr):
    if len(arr) == 0:
        return False;
    minimum = arr[0]
    for x in arr:
        if x < minimum:
            minimum = x
    return minimum

def Maximum(arr):
    if len(arr) == 0:
        return False;
    maximum = arr[0]
    for x in arr:
        if x > maximum:
            maximum = x
    return maximum

def UltimateAnalysis(arr):
    return {"SumTotal":SumTotal(arr),"Average":Average(arr),"Minimum":Minimum(arr),"Maximum":Maximum(arr),"Length":Length(arr)}


arr1 = [37,2,1,-9]
print(UltimateAnalysis(arr1))
#9
def ReverseList(arr):
    firstIndex = 0;
    lastIndex = len(arr) - 1
    while firstIndex < lastIndex:
        temp = arr[firstIndex]
        arr[firstIndex] = arr[lastIndex]
        arr[lastIndex] = temp
        firstIndex += 1
        lastIndex -= 1
    return arr

arr1 = [37,2,1,-9]
print(ReverseList(arr1))