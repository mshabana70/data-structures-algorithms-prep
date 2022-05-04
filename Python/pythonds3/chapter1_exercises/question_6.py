"""
6. In the definition of fractions we assumed that negative fractions have a negative numerator and a positive denominator. Using a negative denominator would cause some of the relational operators to give incorrect results. In general, this is an unnecessary constraint. Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly.
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

# Test new constructor
negative_fraction_one = Fraction(-2, 3)
print(negative_fraction_one) # Output = -2/3

negative_fraction_two = Fraction(3, -4)
print(negative_fraction_two) # Output = -3/4
