'''
Exercise: Limited-size bowls
As things now stand, our Bowl class doesn't limit how many scoops you can put into an instance of Bowl.

Modify add_scoops such that only the first three scoops added to a bowl will actually get there.
You should never have more than three scoops in a bowl; any extras should be ignored silently.
Use a class attribute, called MAX_SCOOPS, to keep track of how many scoops should be allowed in each bowl. (It's traditional to use ALL CAPS in Python for something that's kind of like a constant.)
So we should be able to write this:

Create (in PyCharm) a class Scoop that represents one scoop (ball) of ice cream. Each instance of Scoop will have a single flavor, stored as a string on the flavor attribute.

The following code should then work with your Scoop class:

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
s6 = Scoop('flavor 6')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3, s4)
b.add_scoops(s5, s6)

print(b.flavors())  # should only show ['chocolate', 'vanilla', 'coffee'] -- ignoring the final 3
print(len(b.scoops))  # should print 3
'''


#mycode
class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

class bowl:
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        while len(self.scoops) <= 3:
            for one_scoop in new_scoops:
                self.scoops.append(one_scoop)

    def flavors(self):
        output = []
        for one_scoop in self.scoops:
            output.append(one_scoop.flavor)
        return output



s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
s6 = Scoop('flavor 6')

b = bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3, s4)
b.add_scoops(s5, s6)

print(b.flavors())  # should only show ['chocolate', 'vanilla', 'coffee'] -- ignoring the final 3
print(len(b.scoops))  # should print 3



#solution
'''
class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl:
    MAX_SCOOPS = 3     # class attribute -- we don't use the name of the class
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) >= Bowl.MAX_SCOOPS:  # use the class attribute
                break
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
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
s6 = Scoop('flavor 6')


# for one_scoop in [s1, s2, s3]:
#     print(one_scoop.flavor)

b = Bowl()                 # ask the bowl factory (Bowl class) to create a new bowl
b.add_scoops(s1, s2)       # add scoops s1 and s2 to our bowl
b.add_scoops(s3)           # add scoop s3 to our bowl
b.add_scoops(s4, s5)
b.add_scoops(s6)

print(b.flavors())         # what flavors to the bowl's scoops contain?
print(len(b.scoops))  # should print 3
'''