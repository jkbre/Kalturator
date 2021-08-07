import numpy as np

class matrixOperations():
    """
        W celu przeprowadzenia obliczeń tworzony jest obiekt przechowujący wszystkie potrzebne informajce do ich przeprowadzenia.\n
        matricesDictName -> nazwa pliku w którym zapisywane są powstałe macierze\n
        resultsDictName -> nazwa pliku w którym zapisywane są otrzymane wyniki
    """

    def __init__(self, matricesDictName, resultsDictName):
        super().__init__()
        self.matricesDictName = matricesDictName
        self.resultsDictName = resultsDictName
        self.loadingFromFile()

    def loadingFromFile(self):
        """
        Funkcja wczytująca słownik zapisany w pliku o wcześniej podanej nazwię.\n
        W przypadku jego braku tworzy nowy plik o podanej nazwię.
        """
        try:
            matricesDictNP = np.load(self.matricesDictName, allow_pickle = 'TRUE')
            self.matricesDict = matricesDictNP.item()
        except:
            print("Błąd podczas wczytywania zapisanych macierzy")

        try:
            resultsDictNP = np.load(self.resultsDictName, allow_pickle = 'TRUE')
            self.resultsDict = resultsDictNP.item()
        except:
            self.resultsDict = {}

    def operations(self,operando):
        
        try:
            self.NumA = float(operando[0])
            self.NumB = float(operando[2])

            if operando[1] == "+":
                self.results = self.NumA + self.NumB
            if operando[1] == "-":
                self.results = self.NumA - self.NumB
            if operando[1] == "*":
                self.results = self.NumA * self.NumB
            if operando[1] == "/":
                try:
                    self.results = self.NumA / self.NumB
                except:
                    print("Dzielenie przez 0")
            if operando[1] == "^":
                self.results = self.NumA ** self.NumB
            if operando[1] == "^/":
                try:
                    self.results = self.NumA ** (1/self.NumB)
                except:
                    print("Dzielenie przez 0")

        except:
            None
        
        if operando[0] == "det" or operando[0] == "transpose" or operando[0] == "inv":
            self.workingMatA = self.matricesDict[operando[1]]
            if operando[0] == "det":
                self.results = np.linalg.det(self.workingMatA)
            if operando[0] == "transpose":
                self.results = np.transpose(self.workingMatA)
            if operando[0] == "inv":
                try:
                    # if np.linalg.det(self.workingMatA) != 0:
                    self.results = np.linalg.inv(self.workingMatA)
                except:
                    print("Wyznacznik macierzy odwracanej równy zero")

        try:
            self.workingMatA = self.matricesDict[operando[0]]
            try:
                self.NumB = float(operando[2])
                if operando[1] == "+":
                    self.results = self.NumA + self.NumB
                if operando[1] == "-":
                    self.results = self.NumA - self.NumB
                if operando[1] == "*":
                    self.results = self.NumA * self.NumB
                if operando[1] == "/":
                    try:
                        self.results = self.NumA / self.NumB
                    except:
                        print("Dzielenie przez 0")
                if operando[1] == "^":
                    self.results = self.NumA ** self.NumB
                if operando[1] == "^/":
                    try:
                        self.results = self.NumA ** (1/self.NumB)
                    except:
                        print("Dzielenie przez 0")
            except:
                self.workingMatB = self.matricesDict[operando[2]]
                
                nXm1 = np.shape(self.workingMatA)
                nXm2 = np.shape(self.workingMatB)
                askVerVek = ((nXm1[0] == nXm2[0]) and (nXm2[1] == 1))
                askHorVek = ((nXm1[1] == nXm2[1]) and (nXm2[0] == 1))

                if operando[1] == "+":
                    if (nXm1 == nXm2) or askVerVek or askHorVek:
                            self.results = self.workingMatA + self.workingMatB
                if operando[1] == "-":
                    if (nXm1 == nXm2) or askVerVek or askHorVek:
                            self.results = self.workingMatA - self.workingMatB
                if operando[1] == "*":
                    if (nXm1 == nXm2) or askVerVek or askHorVek:
                            self.results = self.workingMatA * self.workingMatB
                if operando[1] == "/":
                    if (self.workingMatB.all() != 0): 
                        if (nXm1 == nXm2) or askVerVek or askHorVek:
                            self.results = self.workingMatA / self.workingMatB
                if operando[1] == "@":
                    if nXm1[1] == nXm2[0]:
                        self.results = self.workingMatA @ self.workingMatB
        except:
            None

        print(self.results)

    def saveToFile(self,operando):
        border = 1
        while border >= 1:
            try:
                doSaving = input("Zapisać wynik? (y/n): ")
                if doSaving != "y" and doSaving != "n":
                    if border > 1:
                        print("WPISZ Y LUB N!")
                    else:
                        print("Wpisz y lub n...")
                    border += 1
                else:               
                    border = 0
            except:
                print("Została podana zła wartość")
        
        border = 1
        if doSaving == "y":
            workingDict = {" ".join(operando): self.results}
            try:
                self.resultsDict.update(workingDict)
                np.save(self.resultsDictName,self.resultsDict)
            except:
                np.save(self.resultsDictName,workingDict)