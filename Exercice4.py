class Duree:
    def __init__(self,heure,minute,seconde):
        self.__h = heure
        self.__m = minute
        self.__s = seconde

    def affichage(self):
        print(str(self.__h)+"h"+str(self.__m)+"m"+str(self.__s)+"s")

    def __add__(self,d1):
        addSeconde = self.__s + d1.__s
        addMinute = self.__m + d1.__m
        addHeure = self.__h + d1.__h
        if addSeconde >= 60:
            addSeconde -= 60
            addMinute += 1
        if addMinute >= 60:
            addMinute-=60
            addHeure +=1
        return str(addHeure)+"h"+str(addMinute)+"m"+str(addSeconde)+"s"

if __name__ == '__main__':
    d1 = Duree(13,15,50)
    d2 = Duree(15,46,17)
    d1.affichage()
    d3 = d1 + d2
    print(d3)
