import matrixMaker as matMak
import matrixOperations as matOp
import numpy as np
import os

class calculator():

    def __init__(self):
        """
        Obiekt kalkulatora, pozwalający na obsługę funkcji tworzących macierzę oraz funkcji matematycznych
        poprzez wpisywanie komend bądź argumentów konsoli. 
        """
        super().__init__()
        self.matricesDictName = "matricesDict.npy"
        self.resultsDictName = "resultsDict.npy"
        self.ans = None
        self.devMode = 0

    def matrixMaker(self):
        """
        Funkcja służąca do tworzenia macierzy o dowolnej wielkości.
        """
        doAgain = "y"
        while doAgain == "y":     
            making = matMak.matrixMaker(self.devMode)
            shield = making.matrixDef()
            if shield != 1:
                shield = making.valuesInserter()
                if shield != 1:
                    making.saveToFile(self.matricesDictName)
                else:
                    doAgain = "n"
                    break
            else:
                doAgain = "n"
                break
            
            border = 1

            while border >= 1:
                try:
                     # >>>
                    doAgain = input("Chcesz utworzyć kolejną macierz? (y/n): ").lower()
                    if doAgain != "y" and doAgain != "n":
                        if border > 1:
                            print("WPISZ Y LUB N!")
                        else:
                            print("Wpisz y lub n...")
                        border += 1
                    else:
                        border = 0
                except Exception as e:
                    print("Została podana zła wartość")
                    if self.devMode == 1:
                        print(e)

    def dictShow(self, mat = "."):
        """
        Funckja pokazująca wszystkie zapisane macierzę.
        """
        if os.path.exists(self.matricesDictName):
            matricesDictNP = np.load(self.matricesDictName, allow_pickle = 'TRUE')
            if mat != ".":
                try:
                    matricesDict = matricesDictNP.item()
                    print(mat, ":\n", matricesDict[mat], '\n')
                except Exception as e:
                    print("Nie ma takiej macierzy")
            else:
                print("\n==========MATRICES==========\n")
                for key,value in matricesDictNP.item().items():
                    print(key, ':\n', value, '\n')
        else:
            print("Brak zapisanych macierzy")

    def resultsShow(self):
        """
        Funkcja pokazująca wszystkie zapisane wyniki działań matemtycznych.
        """
        if os.path.exists(self.resultsDictName):
            resultsDictNP = np.load(self.resultsDictName, allow_pickle = 'TRUE')
            print("\n==========RESULTS==========\n")
            for key,value in resultsDictNP.item().items():
                print(key, ':\n', value, '\n')
        else:
            print("Brak zapisanych wyników w pamięci")

    def matrixOperations(self,operando):
        """
        Funkcja przyjmująca listę zawierającą działanie matemtyczne wpisane przez użytkownika.
        Przeprowadzone działanie matematyczne, może zostać zapisane przez użytkownika do pliku.\n
        operando -> lista zawierająca wpisane przez użytkownika działanie
        """
        doing = matOp.matrixOperations(self.matricesDictName, self.resultsDictName, self.devMode)
        border = doing.operations(operando, self.ans)
        if border != 1:
            self.ans = doing.saveToFile(operando)

    def helpGuide(self):
        """
        Fukcja wyświetlająca spis dostepnych komend i działań w aplikacji.
        """
        print("\n Możliwe działania:")
        print("\t Tworzenie Macierzy (make)")
        print("\t Wyświetlenie utworzonych macierzy / otrzmanych wyników / konkretnej macierzy (show mat/res/<imię macierzy>)")
        print("\t Wyłączenie programu (exit)")
        print("\t Włączenie\Wyłączenie trybu developerskiego (dev on\off)")
        
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
             # >>>
            roger = input(">>> ")
            workingRoger = [i for i in list(roger.split(" ")) if i.strip()]
            if self.devMode == 1:
                print("Wpisano: ", workingRoger)

            if workingRoger[0] == "dev":
                if workingRoger[1] == "on":
                    self.devMode = 1
                    print("Włączono tryb developerski")
                if workingRoger[1] == "off":
                    self.devMode = 0
                    print("Wyłączono tryb developerski")

            elif workingRoger[0] == "help":
                self.helpGuide()
            
            elif workingRoger[0] == "exit":
                return 0
            
            elif workingRoger[0] == "clear":  
                try:
                    if workingRoger[1] == "memory":
                        self.clearMemory()
                    elif workingRoger[1] == "history":
                        self.clearHistory()
                    else:
                        return 1
                except Exception as e:
                    self.clearMemory()
                    self.clearHistory()
                    if self.devMode == 1:
                        print(e)               

            elif workingRoger[0] == "make":
                self.matrixMaker()

            elif workingRoger[0] == "show":  
                try:
                    if workingRoger[1] == "mat":
                        self.dictShow()
                    elif workingRoger[1] == "res":
                        self.resultsShow()
                    else:
                        self.dictShow(workingRoger[1])
                except Exception as e:
                    if self.devMode == 1:
                        print(e)
                    # print("==========MATRICES==========")
                    self.dictShow()
                    # print("==========RESULTS==========")
                    self.resultsShow()

            else:
            #if workingRoger[0] == "do":
                try:
                    self.matrixOperations(workingRoger)
                except Exception as e:
                    print("Podano nieznaną komendę")
                    if self.devMode == 1:
                        print(e)
        
    def consoleArg(self):
        """
        Fukcja obsługująca argumenty podane z konsoli.
        """
        import sys

        for i, arg in enumerate(sys.argv):
            if arg == "-ch":
                self.clearHistory()
            if arg == "-cm":
                self.clearMemory()
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
                except Exception as e:
                    print("Podano nieznaną komendę")
                    if self.devMode == 1:
                        print(e)
                return 1
    
    def clearHistory(self):
        if os.path.exists(self.resultsDictName):
            border = 1
            while border >= 1:
                    try:
                        # >>>
                        usure = input("Jesteś pewien, że chcesz wyczyszcić historię obliczeń? (y/n): ").lower()
                        if usure != "y" and usure != "n":
                            if border > 1:
                                print("WPISZ Y LUB N!")
                            else:
                                print("Wpisz y lub n...")
                            border += 1
                        else:
                            border = 0
                    except Exception as e:
                        print("Została podana zła wartość")
                        if self.devMode == 1:
                            print(e)
            if usure == "y":
                os.remove(self.resultsDictName)
                print("Historia obliczeń wyczyszczona")
            if usure == "n":
                print("Anulowano")
        else:
            print("Brak zapisanych wyników w pamięci")
    
    def clearMemory(self):
        if os.path.exists(self.matricesDictName):
            border = 1
            while border >= 1:
                    try:
                        # >>>
                        usure = input("Jesteś pewien, że chcesz wyczyszcić listę zapisanych macierzy? (y/n): ").lower()
                        if usure != "y" and usure != "n":
                            if border > 1:
                                print("WPISZ Y LUB N!")
                            else:
                                print("Wpisz y lub n...")
                            border += 1
                        else:
                            border = 0
                    except Exception as e:
                        print("Została podana zła wartość")
                        if self.devMode == 1:
                            print(e)
            if usure == "y":
                os.remove(self.matricesDictName)
                print("Zapisane macierze zostały usunięte")
            if usure == "n":
                print("Anulowano")
        else:
            print("Brak zapisanych macierzy")