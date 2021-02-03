
# for variable in range(20):
#     # if variable % 4 == 0:
#         print(variable)
# print(variable)


# PROBLEM 1
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# s = 'azcbobobegghakl'
# totalVowels = 0
# for value in range(len(s)):
#     if s[value] == 'a' or s[value] == 'e' or s[value] == 'i' or s[value] == 'o' or s[value] == 'u':
#         totalVowels +=1
# print('Number of vowels: '+ str(totalVowels))



# PROBLEM 2

# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2



# s = 'azcbobobegghakl'
# word = 'bob'
# count = 0
# for i in range(len(s)):
#     if s[i:i+len(word)] == word:
#         count +=1
# print(count)

#     count = 0
# phrase = "hello, world"

# for iteration in range(5):
#     count += len(phrase)
#     print("Iteration " + str(iteration) + "; count is: " + str(count))



# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc


# s = 'abcbcd'
# substring = {}
# j = 0
# sequence = 'abcdefghijklmnopqrstuvxzwy'

# for i in range(len(s)):
#     if s[i] == sequence[j]:
#         j+=1
#     :
#         pass

#     if expression:
#         pass





# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
# monthlyInterestRate = (annualInterestRate/12.0)

# # def creditCard(balance) :

# for i in range(12):
#     minimumMonthlyPayment = (monthlyPaymentRate * balance)
#     monthlyUnpaidBalance = (balance - minimumMonthlyPayment)
#     balance = (monthlyUnpaidBalance * monthlyInterestRate)+ monthlyUnpaidBalance

# print('Remaining balance: ' +   "{:.2f}".format(balance))



# pay in 12 months


################SOLUTION PROBLEM 2 WEEK 2
# balance = 3926
# annualInterestRate = 0.2
# mfixedPayment = 10

# mInterestRate = (annualInterestRate/12.0)
# updatedBalance = balance
# numMths = 12
# # def creditCard(balance) :
# while updatedBalance >= 0:
#     prvBalance = updatedBalance
#     mUnpaidBalance = (prvBalance - mfixedPayment)
#     updatedBalance = mUnpaidBalance + (mInterestRate * mUnpaidBalance)
#     numMths -=1
#     # print(numMths)
#     if updatedBalance <= 0:
#         print ('Lowest Payment: ' + str(mfixedPayment))
#         break    
#     if (numMths == 0 and updatedBalance != 0):
#         numMths = 12
#         mfixedPayment +=10
#         # print(mfixedPayment)
#         updatedBalance = balance


#SOLUTION PROBLEM 3

# balance = 320000
# annualInterestRate = 0.2


# mInterestRate = (annualInterestRate/12.0)
# updatedBalance = balance
# numMths = 12
# monthlyPaymentLowerBound = balance /12
# monthlyPaymentUpperBound = (balance *((1+ mInterestRate) **12))/12
# # def creditCard(balance) :
# while monthlyPaymentLowerBound <= monthlyPaymentUpperBound:
#     prvBalance = updatedBalance
#     mfixedPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2
#     mUnpaidBalance = (prvBalance - mfixedPayment)
#     updatedBalance = mUnpaidBalance + (mInterestRate * mUnpaidBalance)
#     numMths -=1
#     # print('while your update balance is ' + str(updatedBalance) +  ' your month payment is ' + str(mfixedPayment))
#     # print('While month is = ' + str(numMths) +  ' your month payment is ' + str(mfixedPayment))

#     # if updatedBalance <= 0:
#     #     print ('Lowest Payment: ' + str(mfixedPayment))
#     #     break    
#     # if (numMths == 0 and updatedBalance != 0):
  
#     if (numMths == 0 and updatedBalance > 0):
#         # print('You enter i the loop higher')
#         monthlyPaymentLowerBound = mfixedPayment + 0.01
#         # print('Month LowerBound' +  str(monthlyPaymentLowerBound))
#         numMths = 12
#         updatedBalance = balance
#     elif (numMths == 0 and updatedBalance < 0):
#         # print('You enter i the loop lower')
#         monthlyPaymentUpperBound = mfixedPayment - 0.01
#         # print('Month UpperBound' + str(monthlyPaymentUpperBound))
#         numMths = 12
#         updatedBalance = balance
#     # else:
# print (mfixedPayment)
#         #     mfixedPayment = (mfixedPayment + monthlyPaymentUpperBound)/2
#         # elif updatedBalance < 0:
#         #     mfixedPayment = 
#         # # print(mfixedPayment)
        



##Exercise GUESS MY NUMBER

# choosedNumber = int(input('Please think of a number between 0 and 100!'))
# counter = 0
# low = 0
# high = 100

# number = 0

# while number != choosedNumber:
#     middle = (low + high)/2
#     number = middle
#     counter +=1
#     print('Is your number ', int(number),  ' ?')
#     question = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.  ")

#     if question == 'h':
#         high = middle
#     if question == 'l':
#         low = middle
#     if question == 'c':
#         print(' Game over. Your secret number was: ', int(number))
#         break
#     else:
#         print(' Sorry, I did not understand your input. ')


# # CORRECT SOLUTION

# print("Please think of a number between 0 and 100!")

# # Upper bound is 100 (but will never reach) and the lowest is 0.
# hi = 100
# lo = 0
# guessed = False

# # Loop until we guess it correctly
# while not guessed:
#     # Bisection search: guess the midpoint between our current high and low guesses
#     guess = (hi + lo)//2
#     print("Is your secret number " + str(guess)+ "?")
#     user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

#     if user_inp == 'c':
#         # We got it right!
#         guessed = True
#     elif user_inp == 'h':
#         # Guess was too high. So make the current guess the highest possible guess.
#         hi = guess
#     elif user_inp == 'l':
#         # Guess was too low. So make the current guess the lowest possible guess.
#         lo = guess
#     else:
#         print("Sorry, I did not understand your input.")

# print('Game over. Your secret number was: ' + str(guess))



'''

A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is:  0.25∗n∗s**2tan(π/n) 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the regular polygon. 
The function returns the sum, rounded to 4 decimal places.

'''

import math

def polysum(n, s):

    def areaPolygon(n,s):
        area = (0.25*n*s**2)/ math.tan(math.pi / n)
        return area
    
    def perimeterPolygon(n,s):
        perimeter = n*s
        return perimeter

    sum = areaPolygon(n,s) + (perimeterPolygon(n,s) ** 2)
    return round(sum,4)


print(polysum(11, 4))

    #sum area and square perimeter rounded 4 decimal places
