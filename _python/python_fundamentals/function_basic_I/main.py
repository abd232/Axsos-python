#1
def a():
    return 5
print(a())
#this should print 5

#2
def a():
    return 5
print(a()+a())

#this should print 5 + 5 = 10

#3
def a():
    return 5
    return 10
print(a())
#this should print 5 because the 10 will never be reached

#4
def a():
    return 5
    print(10)
print(a())
#this will print 5 because print(10) line will never be reached

#5
def a():
    print(5)
x = a()
print(x)
#this will first print 5 because it called first when we initiate x then will print null beacuse we are printing nothing

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#this will print 1 + 2 and 2 + 3 from the function he will print 
#3
#5
#none or error i don't now

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#this will print 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#this will print first b (100) then i it will return 10 because b >= 10 then the 10 will be printer

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#first print will print 7 because the function a will return 7 
#second print will print 14 because that what the function will return
#then will print 21 because 7 + 14

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#the function will return b + c = 8 and will be printed after returned by print method

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#first will print b 500
#then will print b 500
#then will print b 300 from the function
#then will print b 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#first will print 500
#then will print 500
#then will print 300 from the function
#then will print 500
#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#first will print 500
#then will print 500
#then will print 300 from the function
#then will print 300 the new value of b

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#will print 1 from a then 3 from b then 2 from a again

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#first will print 1 from a
#then print 3 from b 
#then will print 5 new value of x from a
#then will print 10 new value of y in the main function

