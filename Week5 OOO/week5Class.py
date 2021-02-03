# Understanding CLASSES 


# class Coordinate(object):
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
#   def distance(self, other):
#     x_diff_sq = (self.x-other.x)**2
#     y_diff_sq = (self.y-other.y)**2
#     return (x_diff_sq + y_diff_sq) ** 0.5

#   #Defining your own priting
#   def __str__(self):
#     return "<" + str(self.x) + "," + str(self.y) + ">"
#   def len(self):
#     return self.x.len()


# c = Coordinate(1,2)
# origin = Coordinate(0,0)
# print(c.distance(origin))

# print(Coordinate.distance(c, origin))
# print(c.x)
# print(c.y)
# print(Coordinate(c, origin))
# print(type(c))
# print(c.len())





# # class Clock(object):
# #     def __init__(self, time):
# #       self.time = time
# #     def print_time(self):
# # 	    time = '6:30'
# # 	    print(self.time)

# # clock = Clock('5:30')
# # clock.print_time()

# class Clock(object):
#     def __init__(self, time):
# 	    self.time = time
#     def print_time(self, time):
# 	    print(time)

# clock = Clock('5:30')
# clock.print_time('10:30')

'''
# Exercise 2

class Weird(object):
  def __init__(self, x, y): 
    self.y = y
    self.x = x
  def getX(self):
    return x 
  def getY(self):
    return y

class Wild(object):
 def __init__(self, x, y): 
  self.y = y
  self.x = x
 def getX(self):
  return self.x 
 def getY(self):
  return self.y

X = 7
Y = 8

# w1 = Weird(X, Y)
# print(w1.getX())

# print(w1.getY())

w2 = Wild(X, Y)
print(w2.getX())


'''


'''
EXERCISE COORDINATE
Your task is to define the following two methods for the Coordinate class:

Add an __eq__ method that returns True if coordinates refer to same point in the plane (i.e., have the same x and y coordinate).

Define __repr__, a special method that returns a string that looks like a valid Python expression that could be used to recreate an object with the same value. In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.

For more on __repr__, see this SO post.

'''

# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def getX(self):
#         # Getter method for a Coordinate object's x coordinate.
#         # Getter methods are better practice than just accessing an attribute directly
#         return self.x

#     def getY(self):
#         # Getter method for a Coordinate object's y coordinate
#         return self.y

#     def __str__(self):
#         return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

# # Correct Answer !!!!!!!!!!!!
#     def __eq__(self, other):
#         # First make sure `other` is of the same type 
#         assert type(other) == type(self)
#         # Since `other` is the same type, test if coordinates are equal
#         return self.getX() == other.getX() and self.getY() == other.getY()

#     def __repr__(self):
#         return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'


'''
EXERCISE
Your task is to define the following two methods for the intSet class:

Define an intersect method that returns a new intSet containing elements that appear in both sets. In other words,

s1.intersect(s2)
would return a new intSet of integers that appear in both s1 and s2. Think carefully - what should happen if s1 and s2 have no elements in common?

Add the appropriate method(s) so that len(s) returns the number of elements in s.

Hint: look through the Python docs to figure out what you'll need to solve this problem.

'''


# class intSet(object):
#     """An intSet is a set of integers
#     The value is represented by a list of ints, self.vals.
#     Each int in the set occurs in self.vals exactly once."""

#     def __init__(self):
#         """Create an empty set of integers"""
#         self.vals = []

#     def insert(self, e):
#         """Assumes e is an integer and inserts e into self""" 
#         if not e in self.vals:
#             self.vals.append(e)

#     def member(self, e):
#         """Assumes e is an integer
#            Returns True if e is in self, and False otherwise"""
#         return e in self.vals

#     def remove(self, e):
#         """Assumes e is an integer and removes e from self
#            Raises ValueError if e is not in self"""
#         try:
#             self.vals.remove(e)
#         except:
#             raise ValueError(str(e) + ' not found')

#     def __str__(self):
#         """Returns a string representation of self"""
#         self.vals.sort()
#         return '{' + ','.join([str(e) for e in self.vals]) + '}'
#     def intersect(self, other):
#         # Initialize a new intSet()
#         commonValueSet = intSet()
#         # Go Through the values in this set
#         for val in self.vals:
#           # Check if each value is a member of the other set
#           if other.member(val):
#             commonValueSet.insert(val)

#     def len(self):
#         return self.vals.len()
        

# #TESTS

# setA = {-19,-9,-7,-6,-1,1,6,7,14}
# setB = {-14,-7,-4,-3,0,9,19,20}
# # setA.intersect(setB)   # result should be {-7}
# intSet(setA)
# print(intSet)


'''
ANOTHER GREAT EXERCISE FOR CLASS
Very Confusing part and struggling to understand the print part 
'''


class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

# spell = Accio()
# spell.execute()
# studySpell(spell)
# studySpell(Confundo())


# print(Accio())
Accio()