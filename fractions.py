class fraction:
    def __init__(self,n,d) :
        self.num =n
        self.den =d
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)
    def __add__(self,other):
        temp = self.num * other.den + self.den * other.num
        temp_den = self.den*other.den
        return '{}/{}'.format(temp, temp_den)
    def __sub__(self,other):
        temp = self.num * other.den - self.den * other.num
        temp_den = self.den*other.den
        return '{}/{}'.format(temp, temp_den)

    def __mul__(self,other):
        temp = self.num *other.num
        temp_den = self.den*other.den
        return '{}/{}'.format(temp, temp_den)
    def __truediv__(self,other):
        temp = self.num *other.den
        temp_den = self.den*other.num
        return '{}/{}'.format(temp, temp_den)

x = fraction(2,3)
y = fraction(4,7)
print(type(x))
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
    
