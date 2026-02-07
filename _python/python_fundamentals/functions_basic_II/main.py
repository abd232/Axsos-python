#1
def countDown(num):
    ans = []
    for x in range(num,-1,-1):
        ans.append(x);
    
    return ans

print(countDown(5));

#2
def print_and_return(arr):
    print(f"from the function: {arr[0]}")
    
    return arr[1]

print(print_and_return([1,2]))

#3
def first_plus_length(arr):
    return arr[0] + len(arr)

print(first_plus_length([1,2,3,4,5]))

#4 
def values_greater_than_second(arr):
    if(len(arr) < 2):
        return False;
    result = []
    second_value = arr[1]
    for x in arr:
        if(x > second_value):
            result.append(x)
    
    print(len(result))
    return result

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5 
def length_and_value(length, value):
    result = []
    for x in range(length):
        result.append(value)
    
    return result

print(length_and_value(4,7))
print(length_and_value(6,2))
