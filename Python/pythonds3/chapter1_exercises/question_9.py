"""
9. Research the __repr__ method. How does it differ from __str__? When is it used? Implement __repr__.
"""

class Fraction:
    """Class Fraction"""  
    def __init__(self, top, bottom):
        """Constructor definition"""
        if type(top) is int and type(bottom) is int:
            if bottom < 0:
                self.common = self.gcd((top * -1), (bottom * -1))
                self.num = (top // self.common) * -1
                self.den = (bottom * -1) // self.common
            else:
                self.common = self.gcd(top, bottom)
                self.num = top // self.common
                self.den = bottom // self.common
        else:
            raise RuntimeError("ERROR: Invalid entry for fraction. Please enter integer values for the numerator and denominator")

    def gcd(self, m, n):
        while m % n != 0:
            m, n = n, m % n
        return n
    
    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

# test new method
my_fraction = Fraction(2, 3)
print(repr(my_fraction)) # Output = Fraction(2, 3)
