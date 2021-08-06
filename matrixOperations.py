import numpy as np

class matrixOperations():

    def __init__(self, matricesDictName, resultsDictName):
        super().__init__()
        self.matricesDictName = matricesDictName
        self.resultsDictName = resultsDictName
        self.loadingFromFile()

    def loadingFromFile(self):
        try:
            matricesDictNP = np.load(self.matricesDictName, allow_pickle = 'TRUE')
            self.matricesDict = matricesDictNP.item()
        except:
            print("Błąd podczas wczytywania zapisanych macierzy")

        try:
            self.resultsDict = np.load(self.resultsDictName, allow_pickle = 'TRUE')
        except:
            None

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
        workingDict = {" ".join(operando): self.results}
        try:
            self.resultsDict.item().update(workingDict)
            np.save(self.resultsDictName,self.resultsDict)
        except:
            np.save(self.resultsDictName,workingDict)