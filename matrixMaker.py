import numpy as np

class matrixMaker():

    def __init__(self):
        super().__init__()

    def matrixDef(self):
        """
        funkcja pobierająca od użytkownika wymiary macierzy
        """
        border = 1
        while border >= 1:
            try:
                self.quby = input("Macierz kwadratowa? (y/n): ")
                if self.quby != "y" and self.quby != "n":
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
        if self.quby == "y":
            while border == 1:
                try:
                    self.n = float(input("Podaj wymiar macierzy: "))
                    if self.n != int(self.n) or self.n <= 0:
                        if border > 1:
                            print("ZŁY WYMIAR!")
                        else:
                            print("Podany wymiar jest błędny")
                        border += 1
                    else:
                        self.m = self.n = int(self.n)
                        border = 0
                except:
                    print("Została podana zła wartość")
        if self.quby == "n":
            while border == 1:
                try:
                    self.n = float(input("Podaj wymiar macierzy n: "))
                    if self.n != int(self.n) or self.n <= 0:
                        if border > 1:
                            print("ZŁY WYMIAR!")
                        else:
                            print("Podany wymiar jest błędny")
                        border += 1
                    else:
                        self.n = int(self.n)
                        border = 0
                except:
                    print("Została podana zła wartość")
            
            border = 1
            while border == 1:
                try:
                    self.m = float(input("Podaj wymiar macierzy m: "))
                    if self.m != int(self.m) or self.m <= 0:
                        if border > 1:
                            print("ZŁY WYMIAR!")
                        else:
                            print("Podany wymiar jest błędny")
                        border += 1
                    else:
                        self.m = int(self.m)
                        border = 0
                except:
                    print("Została podana zła wartość")

        if self.quby == "y":
            self.workingMatrix = np.empty((self.n,self.n),float)
        else:
            self.workingMatrix = np.empty((self.n,self.m),float)

    def valuesInserter(self):
        #
        #if self.quby == "y":
        #    self.workingMatrix = np.empty((self.n,self.n),float)
        #else:
        #    self.workingMatrix = np.empty((self.n,self.m),float)
        #
        for i in range(self.n):
            border = 1
            while border >= 1:
                try:
                    while border >= 1:
                        if (self.n == 1 and self.quby == "y"):
                            workingLine = input("Podaj wartość: ")
                        elif self.n == self.m == 1:
                            workingLine = input("Podaj wartość: ")
                        elif self.n == 1 and self.quby == "n":
                            workingLine = input("Podaj wartości w wierszu (1,2,3,...): ")
                        elif self.m == 1 and self.quby == "n":
                            workingLine = input("Podaj wartość w wierszu {}: ".format(i+1))
                        else:
                            workingLine = input("Podaj wartości w wierszu {} (1,2,3,...): ".format(i+1))
                        workingMatrixInside = list(map(float,list(workingLine.split(","))))
                        if len(workingMatrixInside) != self.m:
                            print("Nie podano wszystkich wartości")
                        else:
                            self.workingMatrix[i] = np.array(workingMatrixInside)
                            border = 0                
                except Exception as e:
                    if border > 1:
                        print("UŻYTO ZŁEJ SKŁADNI!: {}".format(e))
                    else:
                        print("Użyto złej składni: {}".format(e))
                        border += 1
        print("Otrzymana macierz:")
        print(self.workingMatrix)
        self.valueCorrector()
        
    def valueCorrector(self):
        border = 1
        groundhog = 0
        while border >= 1:
            try:
                if groundhog == 1:
                    doCorrection = input("Chcesz jeszcze coś poprawić? (y/n): ")
                else:
                    doCorrection = input("Chcesz coś poprawić? (y/n): ")
                if doCorrection != "y" and doCorrection != "n":
                    if border > 1:
                        print("WPISZ Y LUB N!")
                    else:
                        print("Wpisz y lub n...")
                    border += 1
                else:               
                    border = 0
            except:
                print("Została podana zła wartość")
            
            if doCorrection == "n":
                break

            border = 1
            while border >= 1:
                try:
                    while border >= 1:
                        if self.quby == "y" and self.n == 1:
                            correctionPlace = [1, 1]
                        else:
                            correctionPlace = input("Podaj pozycje wartości do poprawy (nxm): ")                   
                            correctionPlace = list(map(int,list(correctionPlace.split("x"))))
                        if correctionPlace[0] > self.n or correctionPlace[1] > self.m:
                            if border > 1:
                                print("POZA MACIERZĄ!")
                            else:
                                print("Podano miejsce poza macierzą")
                                border += 1
                        else:
                            border = 0                    
                    correctionPlace = [i-1 for i in correctionPlace]
                except Exception as e:
                    if border > 1:
                        print("UŻYTO ZŁEJ SKŁADNI!: {}".format(e))
                    else:
                        print("Użyto złej składni: {}".format(e))
                        border += 1
            
            border = 1
            while border >= 1:
                try:
                    correctedVal = float(input("Podaj nową wartości: "))
                    border = 0
                except Exception as e:
                    if border > 1:
                        print("UŻYTO ZŁEJ SKŁADNI!: {}".format(e))
                    else:
                        print("Użyto złej składni: {}".format(e))
                        border += 1

            self.workingMatrix[correctionPlace[0],correctionPlace[1]] = correctedVal
            print("Macierz po zmianie:")
            print(self.workingMatrix)
            groundhog = 1

    def saveToFile(self,insertedName):
        matricesDictName = insertedName
        border = 1
        while border >= 1:
            try:
                doSaving = input("Zapisać macierz? (y/n): ")
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
            # matName = input("Podaj nazwę macierzy: ")
            # with open('matricesStorage.csv', 'a') as store:
            #     np.savetxt(store, self.workingMatrix, delimiter=',', fmt='%f', header = matName, footer = "end of {}".format(matName))
            # print("Macierz została zapisana jako {}".format(matName))
            while border >=1:
                try:
                    matrixName = input("Podaj nazwę macierzy: ")
                    border = 0
                except:
                    if border > 1:
                        print("ZOSTAŁA PODANA BŁĘDNA NAZWA!")
                    else:
                        print("Została podana błędna nazwa")
                    border += 1
            
            workingDict = {matrixName: self.workingMatrix}

            try:
                matricesDict = np.load(matricesDictName, allow_pickle = 'TRUE')
                matricesDict.item().update(workingDict)
                np.save(matricesDictName,matricesDict)
            except:
                np.save(matricesDictName,workingDict)