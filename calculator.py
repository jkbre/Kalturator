import matrixMaker as matMak
import numpy as np

class calculator():

    def __init__(self):
        super().__init__()
        self.matricesDictName = "matricesDict.npy"
        

    def matrixMaker(self):
        doAgain = "y"
        while doAgain == "y":     
            making = matMak.matrixMaker()
            making.matrixDef()
            making.valuesInserter()
            making.saveToFile(self.matricesDictName)
            border = 1
            while border >= 1:
                try:
                    doAgain = input("Chcesz utworzyć kolejną macierz? (y/n): ")
                    if doAgain != "y" and doAgain != "n":
                        if border > 1:
                            print("WPISZ Y LUB N!")
                        else:
                            print("Wpisz y lub n...")
                        border += 1
                    else:
                        border = 0
                except:
                    print("Została podana zła wartość")

    def dictShow(self):
        matricesDict = np.load(self.matricesDictName, allow_pickle = 'TRUE')
        print(matricesDict)