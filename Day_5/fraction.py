class Fraction(object):
    '''
    Deining a fraction datatype.
    '''
    def __init__(self , num , den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = other.den * self.den
        return Fraction(new_num , new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = other.den * self.den
        return Fraction(new_num, new_den)

    def __float__(self):
        return self.num / self.den

    def __eq__(self, other):
        return (self.num == other.num) and (self.den == other.den)

    def inverse(self):
        return Fraction(self.den , self.num)



frac_1 = Fraction(1 , 2)
print(frac_1)
frac_2 = Fraction(2 , 3)
print(frac_2)
print(frac_1.inverse())
print(float(frac_2))
print(frac_1 == frac_2)
print(frac_1 + frac_2)
print(frac_1 - frac_2)