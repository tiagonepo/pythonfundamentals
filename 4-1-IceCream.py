'''
Exercise: Ice cream
Create (in PyCharm) a class Scoop that represents one scoop (ball) of ice cream. Each instance of Scoop will have a single flavor, stored as a string on the flavor attribute.

The following code should then work with your Scoop class:

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

print(s1.flavor)  # this should print 'chocolate'

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)
'''





#mycode
class scoop:
    def __init__(self, flavor):
        self.flavor = flavor

s1 = scoop('chocolate')
s2 = scoop('vanilla')
s3 = scoop('coffee')

print(s1.flavor)  # this should print 'chocolate'

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)


#solution
