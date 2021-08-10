import numpy as np
import os
# from numpy.linalg import solve

class matrixOperations():

    def __init__(self, matricesDictName, resultsDictName, devMode = 0):
        """
        W celu przeprowadzenia obliczeń tworzony jest obiekt przechowujący wszystkie potrzebne informajce do ich przeprowadzenia.\n
        matricesDictName -> nazwa pliku w którym zapisywane są powstałe macierze\n
        resultsDictName -> nazwa pliku w którym zapisywane są otrzymane wyniki
        """
        super().__init__()
        self.matricesDictName = matricesDictName
        self.resultsDictName = resultsDictName
        self.devMode = devMode
        self.loadingFromFile()

    def loadingFromFile(self):
        """
        Funkcja wczytująca słownik zapisany w pliku o wcześniej podanej nazwię.\n
        W przypadku jego braku tworzy nowy plik o podanej nazwię.
        """
        if os.path.exists(self.matricesDictName):
            try:
                matricesDictNP = np.load(self.matricesDictName, allow_pickle = 'TRUE')
                self.matricesDict = matricesDictNP.item()
            except Exception as e:
                print("Błąd podczas wczytywania zapisanych macierzy")
                if self.devMode == 1:
                    print(e)
                

        try:
            resultsDictNP = np.load(self.resultsDictName, allow_pickle = 'TRUE')
            self.resultsDict = resultsDictNP.item()
        except Exception as e:
            self.resultsDict = {}
            if self.devMode == 1:
                print(e)

    def operations(self,operando,ans):
        """
        Funkcja przyjąca listę, zawierającą wpisaną przez użytkownika działanie matematyczne.\n
        W zależności od wpisanej komendy zostają wykonane odpowiednie
        działania, jednak jedynie w przypadku spełnienia odpowiednich warunków matemtycznych.\n
        operando -> lista zawierająca wpisane przez użytkownika działanie
        """
        # pierwszy wyraz
        if operando[0] == "det" or operando[0] == "transpose" or operando[0] == "inv":
            try:
                if operando[1] == "ans" and ans != None:
                    self.workingMatA = ans
                else:
                    self.workingMatA = self.matricesDict[operando[1]]
                solveFor = "fun"
            except Exception as e:
                print("Operacja nie możliwa do wykonania")
                if self.devMode == 1:
                    print(e)
        else:
            if operando[0] == "ans":
                if isinstance(ans, np.ndarray):
                    self.workingMatA = ans
                    solveFor = "mat"
                elif ans != None:
                    self.NumA = ans
                    solveFor = "number"
                else:
                    print("Pamięć jest pusta")
                    return 1
            else:
                try:
                    self.NumA = float(operando[0])
                    solveFor = "number"
                except Exception as e:
                    if self.devMode == 1:
                        print(e)
                    try:
                        self.workingMatA = self.matricesDict[operando[0]]
                        solveFor = "mat"
                    except Exception as e:
                        print("Pierwszy wyraz jest błędny")
                        if self.devMode == 1:
                            print(e)
                
            if operando[2] == "ans":
                if isinstance(ans, np.ndarray):
                    self.workingMatB = ans
                    if solveFor == "mat":
                        solveFor = "mats"
                    else:
                        solveFor = "wrong"
                elif ans != None:
                    self.NumB = ans
                    if solveFor == "mat":
                        solveFor = "matnum"
                    if solveFor == "number":
                        solveFor = "numbers"
                else:
                    print("Pamięć jest pusta")
                    return 1
            else:
                try:
                    self.NumB = float(operando[2])
                    if solveFor == "mat":
                        solveFor = "matnum"
                    if solveFor == "number":
                        solveFor = "numbers"
                except Exception as e:
                    if self.devMode == 1:
                        print(e)
                    try:
                        self.workingMatB = self.matricesDict[operando[2]]
                        if solveFor == "mat":
                            solveFor = "mats"
                        else:
                            solveFor = "wrong"
                    except Exception as e:
                        print("Drugi wyraz jest błędny")
                        if self.devMode == 1:
                            print(e)

        # const i const
        if solveFor == "numbers":
            if operando[1] == "+":
                self.results = self.NumA + self.NumB
            if operando[1] == "-":
                self.results = self.NumA - self.NumB
            if operando[1] == "*":
                self.results = self.NumA * self.NumB
            if operando[1] == "/":
                try:
                    self.results = self.NumA / self.NumB
                except Exception as e:
                    print("Dzielenie przez 0")
                    if self.devMode == 1:
                        print(e)
            if operando[1] == "^":
                self.results = self.NumA ** self.NumB
            if operando[1] == "^/":
                try:
                    self.results = self.NumA ** (1/self.NumB)
                except Exception as e:
                    print("Dzielenie przez 0")
                    if self.devMode == 1:
                        print(e)

        # funkcje macierzowe
        if solveFor == "fun":
            if operando[0] == "det":
                self.results = np.linalg.det(self.workingMatA)
            if operando[0] == "transpose":
                self.results = np.transpose(self.workingMatA)
            if operando[0] == "inv":
                try:
                    # if np.linalg.det(self.workingMatA) != 0:
                    self.results = np.linalg.inv(self.workingMatA)
                except Exception as e:
                    print("Wyznacznik macierzy odwracanej równy zero")
                    if self.devMode == 1:
                        print(e)
        
        # obliczenia na macierzy
        if solveFor == "matnum":    
            if operando[1] == "+":
                self.results = self.workingMatA + self.NumB
            if operando[1] == "-":
                self.results = self.workingMatA - self.NumB
            if operando[1] == "*":
                self.results = self.workingMatA * self.NumB
            if operando[1] == "/":
                try:
                    self.results = self.workingMatA / self.NumB
                except Exception as e:
                    print("Dzielenie przez 0")
                    if self.devMode == 1:
                        print(e)
            if operando[1] == "^":
                self.results = self.workingMatA ** self.NumB
            if operando[1] == "^/":
                try:
                    self.results = self.workingMatA ** (1/self.NumB)
                except Exception as e:
                    print("Dzielenie przez 0")
                    if self.devMode == 1:
                        print(e)

        #obliczenia na macierzach
        if solveFor == "mats":
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
                else:
                    print("Nieprawidłowe wymiary macierzy")
                    print("Liczba kolumn 'm' pierwszej macierzy musi zgadadzać się z liczbą wierszy 'n' drugiej macierzy.")
                    return 1

        if solveFor == "wrong":
            print("Błędna komenda")
            return 1
        
        print(self.results)
        return 0

    def saveToFile(self,operando):
        """
        Funkcja przyjąca listę, zawierającą wpisaną przez użytkownika działanie matematyczne.
        Zapisuje otrzymany przez obiekt wynik podanego działania matematycznego do pliku.\n
        operando -> lista zawierająca wpisane przez użytkownika działanie
        """
        workingDict = {" ".join(operando): self.results}
        try:
            self.resultsDict.update(workingDict)
            np.save(self.resultsDictName,self.resultsDict)
        except Exception as e:
            np.save(self.resultsDictName,workingDict)
            if self.devMode == 1:
                print(e)
        return self.results