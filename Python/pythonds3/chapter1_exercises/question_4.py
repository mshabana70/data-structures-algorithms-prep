"""
4. Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__).
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
    
    def get_num(self):
        """Method that returns the numerator of a fraction."""
        return {self.num}
    
    def get_den(self):
        """Method that returns the denominator of a fraction."""
        return {self.den}

    def __mul__(self, fraction):
        new_num = self.num * fraction.num
        new_den = self.den * fraction.den
        common = self.gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    
    def __truediv__(self, fraction):
        new_num = self.num * fraction.den
        new_den = self.den * fraction.num
        common = self.gcd(new_num, new_den)
        if new_den // common == 1:
            return new_num // common
        else:
            return Fraction(new_num // common, new_den // common)
    
    def __sub__(self, fraction):
        new_num = (self.num * fraction.den) - (self.den * fraction.num)
        new_den = (self.den * fraction.den)
        common = self.gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num == second_num
    
    def __gt__(self, fraction):
        frac_1 = float(self.num / self.den)
        frac_2 = float(fraction.num / fraction.den)
        return (frac_1 > frac_2)
    
    def __ge__(self, fraction):
        frac_1 = float(self.num / self.den)
        frac_2 = float(fraction.num / fraction.den)
        return (frac_1 >= frac_2)
    
    def __lt__(self, fraction):
        frac_1 = float(self.num / self.den)
        frac_2 = float(fraction.num / fraction.den)
        return (frac_1 < frac_2)
    
    def __le__(self, fraction):
        frac_1 = float(self.num / self.den)
        frac_2 = float(fraction.num / fraction.den)
        return (frac_1 <= frac_2)
    
    def __ne__(self, fraction):
        frac_1 = float(self.num / self.den)
        frac_2 = float(fraction.num / fraction.den)
        return (frac_1 != frac_2)

# Testing comparison methods
x = Fraction(1, 2)
y = Fraction(1, 4)
x2 = Fraction(2, 4)

print(x > x2) # False
print(x < y) # False
print(x >= y) # True
print(x <= y) # False
print(x != y) # True
print(x != x2) # False
print(x == x2) # True