import matrixMaker as matMak
import matrixOperations as matOp
import numpy as np

class calculator():

    def __init__(self):
        super().__init__()
        self.matricesDictName = "matricesDict.npy"
        self.resultsDictName = "resultsDict.npy"
        

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
        matricesDictNP = np.load(self.matricesDictName, allow_pickle = 'TRUE')
        for key,value in matricesDictNP.item().items():
            print(key, ':\n', value)

    def resultsShow(self):
        resultsDictNP = np.load(self.resultsDictName, allow_pickle = 'TRUE')
        for key,value in resultsDictNP.item().items():
            print(key, ':\n', value)

    def matrixOperations(self,operando):
        doing = matOp.matrixOperations(self.matricesDictName, self.resultsDictName)
        doing.operations(operando)
        doing.saveToFile(operando)

    def helpGuide(self):
        print("Możliwe działania:")
        print("\t Tworzenie Macierzy (make)")
        print("\t Wyświetlenie utworzonych macierzy (show)")
        print("\t Wyłączenie programu (exit)")
        print("\t Wykonanie obliczenia (do ...)")
        
        print("\nMożliwe obliczenia:")
        print("\t Dodawanie (A + B)")
        print("\t Odejmowanie (A - B)")
        print("\t Mnożenie (A * B)")
        print("\t Dzielenie (A / B)")
        print("\t Transponowanie (transpose A) ")
        print("\t Liczenie wyznacznika macierzy (det A)")
        print("\t Potęgowanie (A ^ B)")
        print("\t Mnożenie macierzowe (A @ B)")
        print("\t Pierwiastkowanie (A ^/ B)")
        print("\t Odwracanie macierzy (inv A)\n")

    def controlLine(self):
        border = 1
        while border == 1:
            roger = input(">>> ")
            workingRoger = list(roger.split(" "))
        
            if workingRoger[0] == "help":
                self.helpGuide()
            
            if workingRoger[0] == "exit":
                return 0

            if workingRoger[0] == "make":
                self.matrixMaker()

            if workingRoger[0] == "show":
                if workingRoger[1] == "mat":
                    self.dictShow()
                if workingRoger[1] == "res":
                    self.resultsShow()

            if workingRoger[0] == "do":
                self.matrixOperations(workingRoger[1:])
        