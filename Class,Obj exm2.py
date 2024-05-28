class first:
    def __init__(self,name,rollnum,matm,phym,chemm,javam,pythonm):
        self.name=name
        self.rollnum=rollnum
        self.matm=matm
        self.phym=phym
        self.chemm=chemm
        self.javam=javam
        self.pythonm=pythonm
    def printAllDetails(self):
        print(self.name)
        print(self.rollnum)
        print(self.matm)
        print(self.phym)
        print(self.chemm)
        print(self.javam)
        print(self.pythonm)
obj=first("Deepu",462,56,78,89,77,89)
obj.printAllDetails()
obj2=first("sweety","4q5",55,89,90,78,88)
obj.printAllDetails()