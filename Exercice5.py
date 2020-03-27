import numpy as np

class Matrice:
    def __init__(self,data=[]):
        self.__d = data

    def __add__(self,m1):
        newliste = []
        for i in range(0,4):
            k = self.__d[i] + m1.__d[i]
            newliste.append(k)
            k+=1
        return newliste

    def __sub__(self,m1):
        newliste = []
        for i in range(0,4):
            k = self.__d[i] - m1.__d[i]
            newliste.append(k)
            k+=1
        return newliste

if __name__ == '__main__':
    data1 = [2,6,4,3]
    data2 = [1,9,5,6]
    m1 = Matrice(data1)
    m2 = Matrice(data2)
    m3 = m1 + m2
    m4 = m1 - m2
    print(m3,m4)

