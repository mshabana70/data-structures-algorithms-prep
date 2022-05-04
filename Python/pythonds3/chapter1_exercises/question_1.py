"""
1. Implement the simple methods get_num and get_den that will 
return the numerator and denominator of a fraction.
"""

class Fraction:
    """Class Fraction"""  
    def __init__(self, top, bottom):
        """Constructor definition"""
        self.common = self.gcd(top, bottom)
        self.num = top // self.common
        self.den = bottom // self.common
    
    def gcd(self, m, n):
        while m % n != 0:
            m, n = n, m % n
        return n

    def show(self):
        print(f"{self.num}/{self.den}")

    def __str__(self):
        return f"{self.num}/{self.den}"


my_fraction = Fraction(6, 8)
print(my_fraction)