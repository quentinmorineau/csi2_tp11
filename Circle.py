class Circle:
    def __init__(self,r):
        self.__r = r

    def Getr(self):
        return self.__r

    def __add__(self, c1):
       return Circle(self.__r + c1.__r)

    def __lt__(self, c1):
       return self.__r < c1.__r


    def __gt__(self, c1):
        return self.__r > c1.__r


if __name__ == '__main__':
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c5)
