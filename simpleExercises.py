'''

Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

Hints
Ideas about the problem
Have the generator keep a list of the primes it's generated. A candidate number x is prime if (x % p) != 0 for all earlier primes p.

'''


def genPrimes():
  num = 2
  numbers = []

  while num > 1:
    for i in range(2,num):
      if (num % i != 0):
        print(num)
        # yield next
        num +=1
      else:
        num+=1
genPrimes()