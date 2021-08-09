import matrixMaker as matMak
import matrixOperations as matOp
import numpy as np

class calculator():

    def __init__(self):
        """
        Obiekt kalkulatora, pozwalający na obsługę funkcji tworzących macierzę oraz funkcji matematycznych
        poprzez wpisywanie komend bądź argumentów konsoli. 
        """
        super().__init__()
        self.matricesDictName = "matricesDict.npy"
        self.resultsDictName = "resultsDict.npy"

    def matrixMaker(self):
        """
        Funkcja służąca do tworzenia macierzy o dowolnej wielkości.
        """
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
        """
        Funckja pokazująca wszystkie zapisane macierzę.
        """
        matricesDictNP = np.load(self.matricesDictName, allow_pickle = 'TRUE')
        for key,value in matricesDictNP.item().items():
            print(key, ':\n', value)

    def resultsShow(self):
        """
        Funkcja pokazująca wszystkie zapisane wyniki działań matemtycznych.
        """
        resultsDictNP = np.load(self.resultsDictName, allow_pickle = 'TRUE')
        for key,value in resultsDictNP.item().items():
            print(key, ':\n', value)

    def matrixOperations(self,operando):
        """
        Funkcja przyjmująca listę zawierającą działanie matemtyczne wpisane przez użytkownika.
        Przeprowadzone działanie matematyczne, może zostać zapisane przez użytkownika do pliku.\n
        operando -> lista zawierająca wpisane przez użytkownika działanie
        """
        doing = matOp.matrixOperations(self.matricesDictName, self.resultsDictName)
        border = doing.operations(operando)
        if border != 1:
            doing.saveToFile(operando)

    def helpGuide(self):
        """
        Fukcja wyświetlająca spis dostepnych komend i działań w aplikacji.
        """
        print("\n Możliwe działania:")
        print("\t Tworzenie Macierzy (make)")
        print("\t Wyświetlenie utworzonych macierzy / otrzmanych wyników (show mat/res)")
        print("\t Wyłączenie programu (exit)")
        print("\t Wykonanie obliczenia (do ...)")
        
        print("\n Możliwe obliczenia:")
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
        """
        Funkcja slużąca do obsługi funkcjonalności kalkulatora.
        """
        argMode = self.consoleArg()
        if argMode == 1:
            return 0
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
                try:
                    if workingRoger[1] == "mat":
                        self.dictShow()
                    elif workingRoger[1] == "res":
                        self.resultsShow()
                    else:
                        print("Wpisano nieznaną komendę")
                except:
                    self.dictShow()
                    self.resultsShow()

            if workingRoger[0] == "do":
                try:
                    self.matrixOperations(workingRoger[1:])
                except:
                    print("Podano nieznaną komendę")
        
    def consoleArg(self):
        """
        Fukcja obsługująca argumenty podane z konsoli.
        """
        import sys

        for i, arg in enumerate(sys.argv):
            if arg == "-h":
                self.helpGuide()
                return 1
            if arg == "-m":
                self.matrixMaker()
                return 1
            if arg == "-s":
                self.dictShow()
                self.resultsShow()
                return 1
            if arg == "-sm":
                self.dictShow()
                return 1
            if arg == "-sr":
                self.resultsShow()              
                return 1
            if arg == "-d":
                try:
                    self.matrixOperations(sys.argv[2:])
                except:
                    print("Podano nieznaną komendę")
                return 1