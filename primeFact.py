__author__ = "Brandon Hardesty"

def sieve(n = int(1e7)):
    """
    builds a list of primes less than n
    :param n: limit on our primes
    :return: reverse ordered list of primes less than n
    """
    multiples = set()
    primes = [2]
    for i in range(3,n+1,2):
        if i not in multiples:
            primes.append(i)
            multiples.update(f for f in range(i*i,n+1,i))
    return primes[::-1]

def largestPrimeFactor(n,primes):
    """
    :param n:
    :param primes: list of primes between 0 and n
    :return: the largest prime factor
    """
    for i in primes:
        if n % i == 0:
            return i
    return -1
def primeFactors(n, primes):
   factors = [largestPrimeFactor(n, primes)]
   r = n
   i = 0
   while factors[i] > 0:
     r = r // factors[i]
     i += 1
     factors.append(largestPrimeFactor(r, primes))
   factors.pop()
   product = 1
   for p in factors:
       product *= p
   if product == n:
       return factors
   else:
       factors.insert(0,n//product)
   return factors
def displayFactors(n,factors):
    out = ''
    if factors[0] > 1e14:
        out = 'Warning {:,m} is too large to guarantee all factors are prime\n'
    if factors[0] == n:
        out = '{:,d} is prime'.format(n)



def main():
   #primes = sieve()
   #dataFile = open('datfile1','r')
   #nums = []
   #nums = dataFile.readlines()
   print(largestPrimeFactor(100,sieve(9)))


   print(primeFactors(83*2,sieve(9)))


if __name__ == '__main__':
    main()

