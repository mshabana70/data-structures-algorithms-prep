"""
2. In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.
"""

class Fraction:
    """Class Fraction"""  
    def __init__(self, top, bottom):
        """Constructor definition"""
        self.common = self.gcd(top, bottom)
        self.num = top // self.common
        self.den = bottom // self.common
    
    def get_num(self):
        """Method that returns the numerator of a fraction."""
        return {self.num}
    
    def get_den(self):
        """Method that returns the denominator of a fraction."""
        return {self.den}
    
    def gcd(self, m, n):
        while m % n != 0:
            m, n = n, m % n
        return n

    def show(self):
        print(f"{self.num}/{self.den}")

    def __str__(self):
        return f"{self.num}/{self.den}"


# Testing new constructor

test_fraction_one = Fraction(2, 3)
print(test_fraction_one) # output 2/3

test_fraction_two = Fraction(6, 8)
print(test_fraction_two) # output = 3/4

test_fraction_three = Fraction(12, 15)
print(test_fraction_three) # output = 4/5