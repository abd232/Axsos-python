x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#2-1
x[1][0] = 15
print(x)
#2-2
students[0]["last_name"] = 'Bryant'
print(students)
#2-3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
#2-4
z[0]['y'] = 30
print(z)

#3 + 4

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for dictionary in some_list:
        line = ""
        for key in dictionary.keys():
            line += f"{key} - {dictionary[key]} "
        print(line)


iterateDictionary(students)

#5 + 6

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#7 + 8

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    print("# output")
    for key in dojo.keys():
        print(f"{len(dojo[key])} {key.upper()}")
        for x in dojo[key]:
            print(x)
        print("")

printInfo(dojo)