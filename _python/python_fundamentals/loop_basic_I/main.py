#1
for x in range(150):
    print(x)
#2
for x in range(5,1000,5):
    print(x)
#3
for x in range(100):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
#4
sum = 0;
for x in range(1,500000,2):
    sum = sum + x;

print("sum =", sum);
#5
for x in range(2018,0,-4):
    print(x);
#6
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum,highNum + 1,1):
    if(x % mult == 0):
        print(x)