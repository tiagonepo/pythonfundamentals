'''
Exercise: Bowls
Create a new class, Bowl. Creating a new instance of Bowl does not take any arguments, but it does create an empty list, assigned to scoops, which will contain Scoop objects.
Add a new method, add_scoops, to Bowl. The arguments should be instances of Scoop that we want to add to the bowl. This method can take any number of arguments.
Add a new method, flavors, to Bowl. This method takes no arguments, and returns a list of strings -- the flavors of the scoops in the bowl.
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b.flavors())  # ['chocolate', 'vanilla', 'coffee']
'''


#mycode
class scoop:
    def __init__(self, flavor):
        self.flavor = flavor

class bowl:
    def __init__(self):
        self.bowl = bowl
    
    def add_scoop(self):
        return self.add_scoop

    def flavors(self):
        return self.flavors


s1 = scoop('chocolate')
s2 = scoop('vanilla')
s3 = scoop('coffee')

b = bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b.flavors())  # ['chocolate', 'vanilla', 'coffee']



#solution
'''
class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)

    def flavors(self):
        # solution 1: iterate over self.scoops, adding to a list of flavors, and returning it
        # output = []
        # for one_scoop in self.scoops:
        #     output.append(one_scoop.flavor)
        # return output

        # solution 2: use a list comprehension!
        # I have: a list of scoops
        # I want: a list of flavors
        # I can map from the first to the second with .flavor
        return [one_scoop.flavor
                for one_scoop in self.scoops]


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
#
# for one_scoop in [s1, s2, s3]:
#     print(one_scoop.flavor)

b = Bowl()                 # ask the bowl factory (Bowl class) to create a new bowl
b.add_scoops(s1, s2)       # add scoops s1 and s2 to our bowl
b.add_scoops(s3)           # add scoop s3 to our bowl
print(b.flavors())         # what flavors to the bowl's scoops contain?
'''