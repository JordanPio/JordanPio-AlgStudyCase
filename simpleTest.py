# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 


#     iteration = 0
# while iteration < 5:
#     count = 0 #count is set back to 0 all the time compared to previous exercise
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0: #so pretty much this is making the code break straight away and not interate over each letter
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 


# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0
# print(abs(guess**2-x))
# while abs(guess**2-x) >= epsilon:
#     # if abs(guess**2-x) >= epsilon:
#     #     # print('Buceta')
#     if guess <= x:
#         guess += step
#         # print(guess)
#     else:
#         break

# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))


###UBOUND ERROR EXERCISE
# def h(y):
#   x = x + 1

# x = 5
# h(x)
# print(x)


##Functions which I assumed wrong return many times

# def foo(x, y = 5):
#    def bar(x):
#       return x + 1
#    return bar(y * 2)
          
# foo(3)
 

#  def foo(x, y = 5):
#    def bar(x):
#       return x + 1
#    return bar(y * 2)
          
# foo(3, 0)


# str1 = 'exterminate!' 
# str2 = 'number one - the larch'
# str1.upper

# print(str1)
# print(str2.index('n'))
# print(str2.replace('one', 'seven'))
# print(str1.replace('e', '*'))


# RECURSSION EXERCISE

# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#     '''
#     if exp == 0:
#       return 1
#     else:
#       return base * iterPower(base, exp-1)

# # iterative exercise

# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
 
#     returns: int or float, base^exp
#     '''
#     result = 1
#     while exp > 0:
#       result *= base
#       exp -=1
#     return result


# print(iterPower(5,3))

#WEEK 2 PROBLEM 4

# Write an iterative function, gcdIter(a, b), that implements this idea. 
# One easy way to do this is to begin with a test value equal to the smaller of 
# the two input arguments, and iteratively reduce this test value by 1 until you either 
# reach a case where the test divides both a and b without remainder, or you reach 1.


# def gcdIter(a, b):
#     '''
#     a, b: positive integers
    
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     if a < b:
#       divisor = a
#     else:
#        if (a%divisor == 0 and b%divisor == 0):
#         return divisor
#       else:
#         divisor-=1

# print(gcdIter(2, 12)) # = 2

# print(gcdIter(6, 12)) # = 6

# print(gcdIter(9, 12)) # = 3

# print(gcdIter(17, 12)) # = 1


# ### Recursion version of GCD

# def gcdRecur(a, b):
#     '''
#     a, b: positive integers
    
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     if b == 0:
#       return a
#     else:
#       return gcdRecur(b, a%b )


# print(gcdRecur(2, 12)) # = 2

# print(gcdRecur(6, 12)) # = 6

# print(gcdRecur(9, 12)) # = 3

# print(gcdRecur(17, 12)) # = 1

'''
Exercise: is in
We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be.
'''

# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string
    
#     returns: True if char is in aStr; False otherwise
#     '''
#     # Your code here
#     # print(aStr)
#     if len(aStr) == 0:
#       return False
#     elif len(aStr) == 1 :
#       if char[0] == aStr[0]:
#         return True
#       else:
#         return False
    
#     basePoint = int(len(aStr)/2)
#     # print(basePoint)
#     # print(aStr)

#     if char[0] == aStr[basePoint]:
#       return True
#     elif char[0] < aStr[basePoint]:
#       # print('lower')
#       # print(aStr[0:basePoint])
#       return isIn(char, aStr[0:basePoint])
#     else:
#       # print('higher')

#       # print(aStr[basePoint:])
#       return isIn(char, aStr[basePoint+1:])

# print(isIn('d', 'abcefghil'))
#       divisor = b
 
# #     while divisor >= 1:
# #


'''
Learning about TUPLES

'''

'''

x = (1, 2, (3, 'John', 4), 'Hi')

print(x[-1][-1]) # return 'i'
print(x[2][-1]) # return '4'
print(x[2][2]) # return '4'
# print(x[-1][2]) # return error because the last index is 1 since it starts at 0
print(x[0:1]) # return 1,
print(x[0:-1]) # return everything except the last (1, 2, (3, 'John', 4) ############## BE CAREFUL
print(x[-1]) # return last ITEM OF INDEX ############ BE CAREFUL
print(len(x)) # return everything except the last (1, 2, (3, 'John', 4)
print(2 in x) # return TRUE since 2 is inside x
print(3 in x) # return FALSE since 3 is only inside another tulip
print(3 in x[2]) # return return TRUE since 3 is inside the second tulip
print(x[0] = 8) # error since we cant assign it again
print('i' in x) # return false Only the full word can be returned to be true
print('i' in x[-1]) # return TRUE since it verifies the last index
print('i' in x[3]) # return TRUE since it verifies the last index
print('i' in x[3][0]) # return FALSE since its actually H


'''

'''
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, 
where every other element of the input tuple is copied, starting with the first one. 
So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

'''

## Example 1

# def oddTuples(aTup):
#     '''
#     aTup: a tuple
    
#     returns: tuple, every other element of aTup. 
#     '''
#     # Your Code Here
#     newTup = ()
#     for i in range(len(aTup) ):
#       if i % 2 == 0:
#         print(i)
#         newTup = newTup + (aTup[i],)
#         print(newTup)
#     return newTup


##Example 2

# def oddTuples(aTup):
#     '''
#     aTup: a tuple
    
#     returns: tuple, every other element of aTup. 
#     '''
#     # Your Code Here
#     newTup = ()
#     for i in range(0,len(aTup),2 ):
#       print(i)
#       newTup = newTup + (aTup[i],)
#       print(newTup)
#     return newTup


####### LIST EXERCISES


# x = [1, 2, [3, 'John', 4], 'Hi'] 

# print(x[0:1])   ### This will return only [1] as LIST because it stops before indice 1
# print(x[2])   ### This will return [3, 'John', 4] as LIST [] brackets included

# listA = [100,0,1,7,4, 1, 6, 3, 4]
# listB = ['x', 'z', 't', 'q']
# listA.reverse()
# print(listA.count(4))
# print(listA.index(1))
# print(listA)




# aList = [0, 1, 2, 3, 4, 5]
# bList = aList
# aList[2] = 'hello' ##BECAREFUL this will replace whatever is on Index 2 with the word 'hello'
# aList == bList

# print(aList)


# cList = [6, 5, 4, 3, 2]
# dList = []

# for num in cList:
#         dList.append(num)
# cList == dList

# print(cList is dList)


# def applyToEach(L, f):
#   for i in range(len(L)):
#     L[i] = f(L[i])

# testList = [1, -4, 8, -9]

##Solution one
# print(applyToEach(testList, abs))

##Solution 2
#needs to return [2, -3, 9, -8]

# def addOne(x):
#   return x + 1

# applyToEach(testList, addOne)
# print(testList)

# print(subtraction(testList))


##Solution 3

# [1, 16, 64, 81]


# def square(x):
#   return abs(x**2)

# applyToEach(testList, square)
# print(testList)


'''

Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
We want to write some simple procedures that work on dictionaries to return information.

First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:

>>> print(how_many(animals))
6

'''


# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')

#TEST TO RETURN NONE
# animals = {}


# def how_many(aDict):
#   '''
#   aDict: A dictionary, where all the values are lists.

#   returns: int, how many values are in the dictionary.
#   '''
#   # Your Code Here
#   total = 0
#   for i in animals.values():
#     total = total + len(i)
#   return total

# print(how_many(animals))


# '''
# We want to write some simple procedures that work on dictionaries to return information.

# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

# Example usage:

# >>> biggest(animals)
# 'd'
# If there are no values in the dictionary, biggest should return None.
# '''


# def biggest(aDict):
#   '''
#   aDict: A dictionary, where all the values are lists.

#   returns: The key with the largest number of values associated with it
#   '''
#   # Your Code Here
#   dictKeys = aDict.keys()
#   dictValues = aDict.values()

#   if len(dictValues) == 0:
#     return None
#   else:
#     largestKey = max(dictValues)
#     largestKeyNumber = len(largestKey)
#     for v in aDict:
#       # print(v) #PRINT KEY
#       # print(len(v)) #PRINT KEY LENGTH --- MEANS NOTHING AS ALL 1
#       # print(aDict[v]) #PRINT WHAT IS INSIDE THE KEY
#       # print(len(aDict[v])) #PRINT THE TOTAL AMOUNT OF VALUES INSIDE A KEY

#       lengthValue = len(aDict[v])

#       if lengthValue == largestKeyNumber:
#         return v

#     # values = aDict.values()
#     # keyCount = {}
#     # best = max(aDict.values())
#     # for key in aDict.values():
#     #   if key == best:
#     #     return (key, best)
#     #   # if key.values()

# print(biggest(animals))


# # # Example from MIT

# # def biggest(aDict):

# # '''
# # aDict: A dictionary, where all the values are lists.

# # returns: The key with the largest number of values associated with it
# # '''

# #   result = None
# #   biggestValue = 0
# #   for key in aDict.keys():
# #       if len(aDict[key]) >= biggestValue:
# #           result = key
# #           biggestValue = len(aDict[key])
# #   return result


'''
Error Handling Python(EXCEPTION AND ASSERTIONS)


Below are some short Python programs. For each program, answer the associated question.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

These questions will ask you to write what the code prints out. If an exception is raised that is not handled by the code write "error" (no quotes), in addition to any other text that is output.

The function in the following questions takes a list of integers numbersand a position index, and divides each entry in the list of numbers by the value at entry index.

Write what it prints out, separating what appears on a new line by a comma and a space.


'''
#PART 1
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")


# fancy_divide([0, 2, 4], 1)

# fancy_divide([0, 2, 4], 0)
fancy_divide([0, 2, 4], 0)


#PART 2

# def fancy_divide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         fancy_divide(numbers, len(numbers) - 1)
#     except ZeroDivisionError:
#         print("-2")
#     else:
#         print("1")
#     finally:
#         print("0")

# fancy_divide([0, 2, 4], 4) # print 1 0 0 e nao sei porque

