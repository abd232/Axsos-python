class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def display_info(self):
        return (f" with name: {self.name} a {self.sex} with {self.age} years old")

class Lion(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
    
    def display_info(self):
        print("A Lion" + super().display_info())

class Tiger(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
    
    def display_info(self):
        print("A Tiger" + super().display_info())

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name, age, sex):
        self.animals.append( Lion(name, age, sex) )
    def add_tiger(self, name, age, sex):
        self.animals.append( Tiger(name, age, sex) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 4, "female")
zoo1.add_lion("Simba", 2, "male")
zoo1.add_tiger("Rajah",6, "male")
zoo1.add_tiger("Shere Khan", 9, "male")
zoo1.print_all_info()