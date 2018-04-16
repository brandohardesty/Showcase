__author__ = 'Brandon Hardesty'
from primeFact import sieve,primeFactors

class Fraction(object):

    def __init__(self, top, bottom=1):
        """ Constructor for MixedFraction.
        Initializes num and den after reducing top / bottom by their gcd.
        :param top: numerator
        :param bottom: denominator
        """
        g = self.gcd(top, bottom)
        self.num = top // g
        self.den = bottom // g

    @staticmethod
    def gcd(m, n):
        """ Euclid's Division Algorithm to find the greatest common denominator (gcd)
        of two integers.
        <http://people.uncw.edu/tompkinsj/133/proofs/quotientRemainderTheorem.htm>
        :param m: an int
        :param n: an int
        :return: the greatest common denominator of m and n
        """
        while m % n != 0:
            m, n = n, m % n
        return n

    @classmethod
    def from_string(cls,f):
        n = f[:f.index("/")]
        d = f[f.index("/") + 1:]
        return cls(int(n),int(d))



    def __str__(self):
        """ String representation of this fraction.
        :return: 'num / den'
        """
        return '{}/{}'.format(str(self.num), str(self.den))
    def __float__(self):
        result = self.num/self.den
        return result


    def __add__(self, other):
        """ Adds this fraction to the input parameter (also a Fraction or FixedFraction
        (possibly a MixedFraction). For the MixedFraction case,
        Fraction is moved to second operand so
        MixedFraction handles the addition (arithmetic promotion is required).
        :param other a Fraction, FixedFraction, or MixedFraction
        :return Fraction(n, d)
        """
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return Fraction(n, d)
    def __sub__(self,other):
        """ This is going to subtract another fraction from this fraction.
        :param other: The fraction subtracting this fraction
        :return: a fraction resulting from the subtraction
        """
        n = self.num * other.den - self.den * other.num
        d = self.den * other.den
        return Fraction(n,d)

    def __pow__(self, exp):
        """ Multiplies this fraction by itself exp times.
        :param exp: the exponent to be applied
        :return: Fraction(n, d) after exponentiation
        """
        n = self.num ** exp
        d = self.den ** exp
        return Fraction(n, d)
    def __truediv__(self, other):
        """
        Divides a fraction by another fraction
        :param other: another fraction
        :return: a resulting fraction from the division
        """
        n = (self.num * other.den)
        d = (self.den * other.num)
        return Fraction(n,d)
    def __sub__(self,other):
        """
        Subtracts "other" fraction from this fraction
        :param other: another fraction
        :return: a resulting fraction from the subtraction
        """
        n = (self.num * other.den) - (other.num * self.den)
        d = (self.den * other.den)
        return Fraction(n,d)
    def __mul__(self,other):
        """
        Multiplies this fraction by another fraction
        :param other: another fraction
        :return: a resulting fraction from the multiplication
        """
        n = (self.num * other.num)
        d = (self.den * other.den)
        return Fraction(n,d)
    def __eq__(self,other):
        """
        Test if two fractions are equivalent
        :param other: a fraction to test equivalency
        :return: boolean either true or false
        """
        f1 = float(self.num/self.den)
        f2 = float(other.num/other.den)

        if(f1 == f2):
            return True
        else:
            return False
    def __ne__(self,other):
        """
        Test if two fractions aren't equivalent

        :param other:a fraction to test equivalency
        :return: boolean either true or false
        """
        f1 = float(self.num / self.den)
        f2 = float(other.num / other.den)

        if (not(f1 == f2)):
            return True
        else:
            return False
    def __lt__(self,other):
        """
        Test if the current fraction is less than the other fraction
        :param other: another fraction
        :return: boolean true or false
        """
        f1 = float(self.num / self.den)
        f2 = float(other.num / other.den)

        if (f1 < f2):
            return True
        else:
            return False
    def __gt__(self,other):
        """
        Test if the current fraction is greater than the other fraction
        :param other: another fraction
        :return: boolean true or false
        """
        f1 = float(self.num / self.den)
        f2 = float(other.num / other.den)

        if (f1 > f2):
            return True
        else:
            return False
    def __ge__(self,other):
        """
        Test if the current fraction is greater than or equal to the other fraction
        :param other: another fraction
        :return: boolean true or false
        """
        f1 = float(self.num / self.den)
        f2 = float(other.num / other.den)

        if (f1 >= f2):
            return True
        else:
            return False
    def __le__(self,other):
        """
        Test if the current fraction is less than or equal to another fraction
        :param other: another fraction
        :return: boolean true or false
        """
        f1 = float(self.num / self.den)
        f2 = float(other.num / other.den)

        if (f1 <= f2):
            return True
        else:
            return False
    def __abs__(self):
        tempNum = self.num
        if(self.num < 0):
            tempNum *= -1
        else:
            pass
        return Fraction(tempNum,self.den)



    def primeFactorsOfFrac(self):
        n = sieve(max(self.num,self.den))
        factOfNum = primeFactors(self.num,n)
        factOfDen = primeFactors(self.den,n)
        return (factOfNum,factOfDen)




