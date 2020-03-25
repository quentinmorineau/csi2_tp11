class Rational:
    def __init__(self,num,den):
        self.__n = num
        self.__d = den

    def __add__(self,r1):
        if self.__d == r1.__d :
            return str(self.__n + r1.__n)+"/"+str(self.__d)
        elif self.__d != r1.__d :
            newDen = self.__d * r1.__d
            newNum = self.__d * r1.__n + self.__n * r1.__d
            return (str(newNum)+"/"+str(newDen))

    def __sub__(self,r1):
        if self.__d == r1.__d :
            return str(self.__n - r1.__n)+"/"+str(self.__d)
        elif self.__d != r1.__d :
            newDen = self.__d * r1.__d
            newNum = -(self.__d * r1.__n - self.__n * r1.__d)
            return (str(newNum)+"/"+str(newDen))

    def __mul__(self,r1):
        newDen = self.__d * r1.__d
        newNum = self.__n * r1.__n
        return str(newNum)+"/"+str(newDen)

    def __lt__(self,r1):
        if self.__d == r1.__d :
            return self.__n < r1.__n
        elif self.__d != r1.__d :
            num1 = self.__n * r1.__d
            num2 = self.__d * r1.__n
            return num1 < num2

if __name__ == '__main__':
    r1 = Rational(4,5)
    r2 = Rational(3,8)
    r3 = r1 + r2
    r4 = r1 - r2
    r5 = r1 * r2
    r6 = r1 < r2
    print(r3,r4,r5,r6)
    print(isinstance(r2,Rational))
