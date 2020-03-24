class Complex :
    def __init__(self,reel,imag):
        self.__r = reel
        self.__i = imag

    def GetReel(self):
        return self.__r

    def GetImaginaire(self):
        return self.__i

    def __add__(self, c1):
       return Complex(self.__r + c1.__r, self.__i + c1.__i)

    def __sub__(self,c1):
        return Complex(self.__r - c1.__r, self.__i - c1.__i)

    def __mul__(self,c1):
        return Complex(self.__r * c1.__r, self.__i * c1.__i)

    def __truediv__(self, c1):
        return Complex(self.__r / c1.__r, self.__i / c1.__i)

    def __abs__(self):
        return (((self.__r)**2)+((self.__i)**2))**0.5

    def __eq__(self,c1):
        return self.__r == c1.__r and self.__i == c1.__i

    def __ne__(self,c1):
        return self.__r != c1.__r or self.__i != c1.__i


if __name__ =='__main__':
    c1 = complex(-1,1)
    c2 = complex(-3,1)
    c3 = c1 + c2
    c4 = c1 - c2
    c5 = c1 * c2
    c6 = c1 / c2
    c7 = abs(c1)
    c8 = c1 == c2
    c9 = c1 != c2
    print(c3,c4,c5,c6,c7,c8,c9)






