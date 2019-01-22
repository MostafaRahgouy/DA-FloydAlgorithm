
class Floyd:
    def SetFloydAlgorithm(self, W, P, D, citiesCount):
        self.InitialP( P, citiesCount )
        self.InitialD( D , W , citiesCount )
        self.CalculatePD( W , P , D , citiesCount)

    def InitialP(self, P, citiesCount):
        for row in range(citiesCount):
            p = []
            for cols in range(citiesCount):
                p.append(int(0))
            P.append(p)

    def InitialD(self , D , W , citiesCount):
        for row in range(citiesCount):
            d = []
            for cols in range(citiesCount):
                d.append(int(W[row][cols]))
            D.append(d)

    def CalculatePD(self , W , P , D , citiesCount):
        for k in range(0 , citiesCount):
            for i in range(0 , citiesCount):
                for j in range(0 , citiesCount):
                    if (D[i][k] + D[k][j]) < D[i][j]:
                        P[i][j] = k + 1
                        D[i][j] = D[i][k] + D[k][j]

    def PrintPath(self , P, citiesNames, startPoint, destination):
        print("V = ", citiesNames[startPoint])
        self.Path(P, citiesNames, startPoint  , destination )
        print("V = ", citiesNames[destination])

    def Path(self , P , citiesNames , startPoint , destination):
        if P[startPoint - 1][destination - 1] != 0:
            self.Path(P, citiesNames, startPoint, P[startPoint - 1][destination - 1])
            print("V = ", citiesNames[P[startPoint - 1][destination - 1]])
            self.Path(P, citiesNames, P[startPoint - 1][destination - 1], destination)
