"""
1. Implement the simple methods get_num and get_den that will 
return the numerator and denominator of a fraction.
"""

class Fraction:
    """Class Fraction"""  
    def __init__(self, top, bottom):
        """Constructor definition"""
        self.num = top 
        self.den = bottom 
    
    def get_num(self):
        """Method that returns the numerator of a fraction."""
        return self.num
    
    def get_den(self):
        """Method that returns the denominator of a fraction."""
        return self.den

    def show(self):
        print(f"{self.num}/{self.den}")

    def __str__(self):
        return f"{self.num}/{self.den}"


# Testing new methods
my_fraction = Fraction(6, 8)
print(my_fraction.get_num()) # Output = 6
print(my_fraction.get_den()) # Output = 8