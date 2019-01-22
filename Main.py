import Floyd as Floyd
import pyodbc

def Main():
    floydAlgorithm = Floyd.Floyd()
    while True:
        W = []
        P = []
        D = []
        citiesNames = {}
        select = int(Menu())
        if select == 1:
            MainOneHelper(W , citiesNames)
        elif select == 2:
            MainTwoHelper(W , citiesNames)
        elif select == 3:
            About()
        else:
            break
        if select != 3:
            citiesCount = len(citiesNames)
            floydAlgorithm.SetFloydAlgorithm(W, P, D, citiesCount)
            while True:
                select = int(TestMenu())
                if select == 1:
                    print("Cities : ")
                    print(citiesNames)
                elif select == 2:
                    Print("Matrix W : " , W )
                elif select == 3:
                    Print("Matrix D : " , D)
                elif select == 4:
                    Print("Matrix P : " , P)
                elif select == 5:
                    Test( D , P , floydAlgorithm , citiesNames , citiesCount )
                else:
                    break

def Menu():
    print("-------------------------------------------------\n"
          "                      MENU                       \n"
          "-------------------------------------------------\n"
          "1.Get Data From User                             \n"
          "2.Get Data From Database                         \n"
          "3.About                                          \n"
          "4.Exit                                           \n"
          "-------------------------------------------------\n")
    return int(input("Choose an option :"))

def MainOneHelper( W , citiesNames ):
    citiesCount = GetCitiesCount()
    GetCitiesNames(citiesNames, citiesCount)
    GetW(W, citiesNames, citiesCount)

def GetCitiesCount():
    citiesCount = int(input("Enter Count Of Cities :"))
    return citiesCount

def GetCitiesNames( citiesNames , citiesCount ):
    for i in range(1 , citiesCount + 1):
        cityName = str(input("Enter City " + str(i) + " Name : "))
        citiesNames[i] = cityName

def GetW( W , citiesNames , citiesCount ):
    for row in range(citiesCount):
        rowW = []
        for cols in range(citiesCount):
            colsW = int(input("Enter W between city '"
                                + str(citiesNames[row + 1]) + "' and '"
                                + str(citiesNames[cols + 1] + "' : " )))
            rowW.append(colsW)
        W.append(rowW)

def MainTwoHelper( W , citiesNames):
    connection = pyodbc.connect("Driver={SQL Server};Server=localhost;Database=FloydDB;")
    GetCitesNamesFromDb(connection , citiesNames)
    GetWFromDb(connection ,W , len(citiesNames))

def GetCitesNamesFromDb(connection , citiesNames):
    cities = connection.cursor()
    cities.execute("SELECT CityId , CityName  FROM Cities WHERE  ExampleId = 1")
    for city in cities:
        citiesNames[city[0]] = city[1]
    cities.close()

def GetWFromDb(connection , W , citiesCount ):
    weights = connection.cursor()
    weights.execute("SELECT StartCityId , EndCityId , WStartEnd FROM W WHERE ExampleId = 1")
    def InitialW(W):
        for i in range(citiesCount):
            w = []
            for j in range(citiesCount):
                w.append(0)
            W.append(w)
    InitialW(W)
    for weight in weights:
        W[weight[0] - 1][weight[1] - 1] = weight[2]
    weights.close()

def About():
    print("Lesson : Designe And Analyze Algorithms\n"
          "Master : Mr. Jahanbakhsh               \n"
          "Students : Mostafa Rahguoy             \n"
          "           Hamed Babaei                \n\n"
          "Summer 96                               \n")

def TestMenu():
    print("-------------------------------------------------\n"
          "                      MENU                       \n"
          "-------------------------------------------------\n"
          "1. Cities Name                                   \n"
          "2. W Matrix                                      \n"
          "3. D Matrix                                      \n"
          "4. P Matrix                                      \n"
          "5. Get D and P between two city                  \n"
          "6. Back To Menu                                  \n"
          "-------------------------------------------------\n")
    return int(input("Choose an option :"))

def Print( msg , dic ):
    print(msg)
    for i in dic:
        print(i)

def Test(D , P , floydAlgorithm , citiesNames , citiesCount ):
    wantToTest = str(input("Do you wand to get P and D of between two city :(y/n)"))
    while wantToTest == "y":
        startPointStr = str(input("Enter Start Point (city name) : "))
        startPoint = GetDicKey(citiesNames, citiesCount, startPointStr)
        destinationStr = str(input("Enter Destination (city name) : "))
        destination = GetDicKey(citiesNames, citiesCount, destinationStr)
        print("Destination between city {0} and {1} is : {2}".format(citiesNames[startPoint]
                                                                     , citiesNames[destination],
                                                                     D[startPoint - 1][destination - 1]))
        floydAlgorithm.PrintPath(P, citiesNames, startPoint, destination)
        wantToTest = str(input("Do you wand to get P and D of between two city ?(y/n)"))

def GetDicKey( citiesNames , citiesCount , value ):
    for i in range(1 , citiesCount + 1):
        if citiesNames[i] == value:
            return i

if __name__ == "__main__":
    Main()
