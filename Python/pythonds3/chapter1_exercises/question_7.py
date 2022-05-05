"""
7. Research the __radd__ method. How does it differ from __add__? When is it used? Implement __radd__.
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

    def show(self):
        print(f"{self.num}/{self.den}")

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
                    self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = self.gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    
    def __radd__(self, other_fraction):
        return other_fraction.__add__(self)

# Testing methods
fraction_one = Fraction(1, 2)
fraction_two = Fraction(3, 4)

print(fraction_one + fraction_two)
print(fraction_one.__radd__(fraction_two))

