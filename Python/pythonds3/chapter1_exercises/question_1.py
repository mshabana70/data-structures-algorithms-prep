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

    def show(self):
        print(f"{self.num}/{self.den}")

    def __str__(self):
        return f"{self.num}/{self.den}"