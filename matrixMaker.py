import numpy as np

class matrixMaker():

    def __init__(self,devMode = 0):
        """
        Obiekt wykonujący tworzenie oraz zapisywanie macierzy.
        """
        super().__init__()
        self.devMode = devMode
        self.area51 = ['make', 'dev', '.', 'mat', 'res', 'help', 'exit', 'clear', 'show', 'memory', 'history', 'off', 'on', 'cancel']

    def matrixDef(self):
        """
        Funkcja pobierająca od użytkownika wymiary macierzy 
        oraz tworząca puste macierze o podanej wielkości.
        """
        border = 1
        escape = 0

        while border >= 1:
            try:
                cmdl = input("Podaj wymiar macierzy n: ")
                if cmdl == "cancel":
                    escape = 1
                    break
                else:
                    self.n = float(cmdl)

                if self.n != int(self.n) or self.n <= 0:
                    if border > 1:
                        print("ZŁY WYMIAR!")
                    else:
                        print("Podany wymiar jest błędny")
                    border += 1
                else:
                    self.n = int(self.n)
                    border = 0
            except Exception as e:
                print("Podany wymiar jest błędny")
                if self.devMode == 1:
                    print(e)
        if escape == 1:
            return 1

        border = 1
        escape = 0

        while border >= 1:
            try:
                cmdl = input("Podaj wymiar macierzy m: ")
                if cmdl == "cancel":
                    escape = 1
                    break
                else:
                    self.m = float(cmdl)
                
                if self.m != int(self.m) or self.m <= 0:
                    if border > 1:
                        print("ZŁY WYMIAR!")
                    else:
                        print("Podany wymiar jest błędny")
                    border += 1
                else:
                    self.m = int(self.m)
                    border = 0
            except Exception as e:
                print("Została podana zła wartość")
                if self.devMode == 1:
                    print(e)
        if escape == 1:
            return 1
        
        try:
            self.workingMatrix = np.empty((self.n,self.m),float)
        except Exception as e:
            if self.devMode == 1:
                print(e)
            print("Tworzenie macierzy nie powiodło się.\nPodano za dużą wartość wymiarów macierzy")
            return 1

    def valuesInserter(self):
        """
        Funkcja wprowadzająca wartości podane przez użytkownika do wcześniej utworzonych macierzy.
        """
        for i in range(self.n):
            border = 1
            escape = 0
            while border >= 1:
                try:
                    while border >= 1:
                        if self.n == self.m == 1:
                             # >>>
                            workingLine = input("Podaj wartość: ")
                        elif self.n == 1 and self.m != 1:
                             # >>>
                            workingLine = input("Podaj wartości w wierszu (1,2,3,...): ")
                        elif self.m == 1 and self.n != 1:
                             # >>>
                            workingLine = input("Podaj wartości w wierszu {}: ".format(i+1))
                        else:
                             # >>>
                            workingLine = input("Podaj wartości w wierszu {} (1,2,3,...): ".format(i+1))
                        if workingLine == "cancel":
                            escape = 1
                            break
                        workingMatrixInside = list(map(float,list(workingLine.split(","))))
                        if len(workingMatrixInside) < self.m:
                            print("Nie podano wszystkich wartości")
                        elif len(workingMatrixInside) > self.m:
                            print("Podano zbyt wiele wartości")
                        else:
                            self.workingMatrix[i] = np.array(workingMatrixInside)
                            border = 0                
                except Exception as e:
                    if border > 1:
                        print("UŻYTO ZŁEJ SKŁADNI!")
                    else:
                        print("Użyto złej składni")
                        border += 1
                    if self.devMode == 1:
                        print(e)
                if escape == 1:
                    break
            if escape == 1:
                break
        if escape == 1:
            return 1
        
        print("Otrzymana macierz:")
        print(self.workingMatrix)
        self.valueCorrector()
        
    def valueCorrector(self):
        """
        Funkcja pozwalająca na poprawę wprowadzonych wartości umieszczonych w macierzy.
        """
        border = 1
        groundhog = 0
        while border >= 1:
            while border >=1:
                try:
                    if groundhog == 1:
                        doCorrection = input("Chcesz jeszcze coś poprawić? (y/n): ").lower()
                    else:
                        doCorrection = input("Chcesz coś poprawić? (y/n): ").lower()
                    if doCorrection != "y" and doCorrection != "n":
                        if border > 1:
                            print("WPISZ Y LUB N!")
                        else:
                            print("Wpisz y lub n...")
                        border += 1
                    else:               
                        border = 0
                except Exception as e:
                    if self.devMode == 1:
                        print(e)
                    print("Została podana zła wartość")
            
            if doCorrection == "n":
                break

            border = 1
            while border >= 1:
                try:
                    while border >= 1:
                        if self.m == 1 and self.n == 1:
                            correctionPlace = [1, 1]
                        else:
                            correctionPlace = input("Podaj pozycje wartości do poprawy (nxm): ")
                            if self.devMode == 1:
                                print("Wpisano: ", correctionPlace)
                            correctionPlace = list(map(int,list(correctionPlace.split("x"))))
                            if self.devMode == 1:
                                print("Otrzymano: ", correctionPlace)
                        if correctionPlace[0] > self.n or correctionPlace[1] > self.m:
                            if border > 1:
                                print("POZA MACIERZĄ!")
                            else:
                                print("Podano miejsce poza macierzą")
                                border += 1
                        elif correctionPlace[0] == 0 or correctionPlace[1] == 0:
                            if border > 1:
                                print("ZEROWY WYMIAR!")
                            else:
                                print("Podano zerowy wymiar")
                                border += 1
                        else:
                            border = 0                    
                    correctionPlace = [i-1 for i in correctionPlace]
                except Exception as e:
                    if border > 1:
                        print("UŻYTO ZŁEJ SKŁADNI!")
                    else:
                        print("Użyto złej składni")
                        border += 1
                    if self.devMode == 1:
                        print(e)
            
            border = 1
            while border >= 1:
                try:
                    correctedVal = float(input("Podaj nową wartości: "))
                    border = 0
                except Exception as e:
                    if border > 1:
                        print("UŻYTO ZŁEJ SKŁADNI!")
                    else:
                        print("Użyto złej składni")
                        border += 1
                    if self.devMode == 1:
                        print(e)

            self.workingMatrix[correctionPlace[0],correctionPlace[1]] = correctedVal
            print("Macierz po zmianie:")
            print(self.workingMatrix)
            groundhog = 1
            border = 1

    def saveToFile(self,insertedName):
        """
        Funkcja zapisująca otrzymaną macierz do pliku.\n
        insertedName -> nazwa pliku zapisu
        """
        matricesDictName = insertedName
        try:
            matricesDictNP = np.load(matricesDictName, allow_pickle = 'TRUE')
            matricesDict = matricesDictNP.item()
        except Exception as e:
            matricesDict = {}
            if self.devMode == 1:
                print(e)
        
        border = 1
        while border >= 1:
            try:
                doSaving = input("Zapisać macierz? (y/n): ").lower()
                if doSaving != "y" and doSaving != "n":
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
        
        border = 1
        if doSaving == "y":
            while border >=1:
                try:
                    matrixName = input("Podaj nazwę macierzy: ")
                    workingMatrixName = list(matrixName.split())
                    if self.devMode == 1:
                        print("Wpisano: ", matrixName)
                        print("Otrzymano: ", workingMatrixName)
                    if len(workingMatrixName) > 1:
                        border = 1
                        try:
                            workingMatrixName = int(workingMatrixName[0])
                            print("Nazwa macierzy nie może zaczynać się od liczby i posiadać spacji")
                        except Exception as e:
                            print("Nazwa macierzy nie może posiadać spacji")
                            if self.devMode == 1:
                                print(e)
                    else:    
                        try:
                            workingMatrixName = int(workingMatrixName[0])
                            print("Nazwa macierzy nie może być liczbą")
                            border = 1
                        except Exception as e:
                            if self.devMode == 1:
                                print(e)
                            matrixName = workingMatrixName[0]
                            if matrixName in matricesDict:    
                                while border >= 1:
                                    try:
                                        print("Macierz o podanej nazwię już istnieje")
                                        doIt = input("Chcesz ją nadpisać? (y/n): ").lower()
                                        if doIt != "y" and doIt != "n":
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
                                if doIt == "y":
                                    print("Macierz została nadpisana")
                                else:
                                    print("Anulowano operacje")
                                    border = 1
                            elif matrixName in self.area51:
                                print("Wybrano nazwę zastrzeżoną")
                            
                            else:
                                border = 0
                except Exception as e:
                    if border > 1:
                        print("ZOSTAŁA PODANA BŁĘDNA NAZWA!")
                    else:
                        print("Została podana błędna nazwa")
                    if self.devMode == 1:
                        print(e)
                    border += 1
            
            workingDict = {matrixName: self.workingMatrix}
            
            try:
                # matricesDictNP = np.load(matricesDictName, allow_pickle = 'TRUE')
                # matricesDict = matricesDictNP.item()
                matricesDict.update(workingDict)
                np.save(matricesDictName,matricesDict)
            except Exception as e:
                if self.devMode == 1:
                    print(e)
                np.save(matricesDictName,workingDict)
            if self.devMode == 1:
                print(workingMatrixName)
                print(workingMatrixName[0])
                print(matrixName)
            print("Macierz została zapisana jako:", matrixName)