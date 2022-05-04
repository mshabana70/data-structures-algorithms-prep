"""
5. Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. If either is not an integer, the constructor should raise an exception.
"""

class Fraction:
    """Class Fraction"""  
    def __init__(self, top, bottom):
        """Constructor definition"""
        if type(top) is int and type(bottom) is int:
            self.common = self.gcd(top, bottom)
            self.num = top // self.common
            self.den = bottom // self.common
        else:
            raise RuntimeError("ERROR: Invalid entry for fraction. Please enter integer values for the numerator and denominator")

    def gcd(self, m, n):
        while m % n != 0:
            m, n = n, m % n
        return n

    def show(self):
        print(f"{self.num}/{self.den}")

    def __str__(self):
        return f"{self.num}/{self.den}"
    
# Testing new constructor
print(Fraction(2.7, 3.5))
print(Fraction("4", "5"))
print(Fraction(4, 5))