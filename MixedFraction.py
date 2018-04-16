from Fraction import Fraction
__author__ = 'Brandon Hardesty'


class MixedFraction (Fraction):

    def __init__(self, top, bottom=1):
        """ Initializes num and den after reducing top / bottom
        by their gcd by invoking super.
        
        Adds fields whole and n, initialized to 0.
        If num > den, assigns the quotient to whole and the remainder to n.
        :param top: numerator
        :param bottom: denominator
        """
        super().__init__(top, bottom)
        self.whole = 0
        self.n = 0
        if self.num >= self.den:
            self.whole = self.num // self.den
            self.n = self.num % self.den

    def __str__(self):
        """ String representation of this fraction.

        Empty strings are used in place of 0.
        :return: whole num / den :: num / den :: whole
        """
        if self.whole == 0:
            return super().__str__()
        elif self.n == 0:
            return str(self.whole)
        return '{} {}/{}'.format(str(self.whole), str(self.n), str(self.den))

    def __add__(self, other):
        """ Adds this fraction to the input parameter (also a
        Fraction (possibly a MixedFraction).
        
        :param other Fraction or MixedFraction
        :return MixedFraction(n, d)
        """
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        return MixedFraction(n, d)

    def __sub__(self, other):
        """ Subtracts the input parameter (also a
        Fraction (possibly a MixedFraction) from this fraction.
        
        :param other Fraction or MixedFraction
        :return MixedFraction(n, d)
        """


        n = (self.num * other.den) - (self.den * other.num)
        d = self.den * other.den




        return MixedFraction(n,d)
    def __mul__(self,other):
        """
        Multiplies a mixed fraction by another mixed fraction or fraction
        :param other: another fraction or mixed fraction
        :return: the resulting mixed fraction from the multiplication
        """

        n = (self.num) * (other.num)
        d = (self.den * other.den)


        return MixedFraction(n,d)
    def __truediv__(self,other):
        """
        Divides a mixed fraction by another mixed fraction or a fraction
        :param other: another fraction or mixed fraction
        :return: the resulting mixed fraction from the division
        """

        n = (self.num) * other.den
        d = (self.den * other.num)

        return MixedFraction(n,d)




    def __pow__(self, exp):
        """ Multiplies this fraction by itself exp times.

        :param exp: the exponent to be applied
        :return: MixedFraction(n, d) after exponentiation
        """
        f = super().__pow__(exp)
        return MixedFraction(f.num, f.den)


    @classmethod
    def from_string(cls,f):
        if (f.count(" ") == 1):
            w = f[:f.index(" ")]
            n = f[f.index(" ") + 1:f.index("/")]
            d = f[f.index("/")+1:]
            return cls(int(w) * int(d) + int(n), int(d))
        if(f.count(" ") == 0):
            n = f[:f.index("/")]
            d = f[f.index("/") + 1:]
            return cls(int(n),int(d))


    
