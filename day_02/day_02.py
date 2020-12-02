# The problem is come from hackerank https://www.hackerrank.com/challenges/30-class-vs-instance/problem
# Solved by Kenny
class Person:
    def __init__(self,initialAge):
        if (initialAge < 0):
            print("Age is not valid, setting age to 0.")
            Person.age = 0
        else: Person.age = initialAge
        return
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if ( Person.age < 13 ):
            print("You are young.")
        elif ( Person.age > 12 and Person.age < 18 ):
            print("You are a teenager.")
        else: print("You are old.")
        return
    def yearPasses(self):
        # Increment the age of the person in here
        Person.age += 1
        return
        
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
