"""
3. Implement the remaining simple arithmetic operators (__sub__, __mul__, and __truediv__).
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
    

# Testing new methods
x = Fraction(1, 2)
y = Fraction(1, 4)

product = x * y
quotient = x / y
diff = x - y
print(product) # Output = 1/8
print(quotient) # Output = 2
print(diff) # Output = 1/4
