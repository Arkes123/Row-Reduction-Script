class rowOps:
    def interchange(matrix, i, j):
        matrix.userMatrix[i], matrix.userMatrix[j] = matrix.userMatrix[j], matrix.userMatrix[i]
        return matrix


    def scaling(matrix, i, j):
        pass


    def addRowToScaler(matrix, i, j):
        pass

    def presentOperations():
        print("1) Interchange rows")
        print("2) Scale a row by a real number")
        print("3) Add a row to a scalar multiple of another")

class base:
    def __init__(self, userMatrix, numRows, numCols):
        self.userMatrix = userMatrix
        self.numRows = numRows
        self.numCols = numCols

    def generateMatrix(numRows, numCols, userMatrix):
        for i in range(numRows):
            rows = []
            for j in range(numCols):
                rows.append(int(input("Enter an element: ")))
            userMatrix.append(rows)
        
        matrix = base(userMatrix, numRows, numCols)
        return matrix

    def printGivenMatrix(matrix):
        for i in range(matrix.numRows):
            for j in range(matrix.numCols):
                print(matrix.userMatrix[i][j], end=" ")
            print()
    
    def regularEchelon(matrix):
        print("Here is you matrix...")
        print("\n")

        print("What operation would you like to perform? ")
        rowOps.presentOperations()

        try:
            userOption = int(input("Enter option: "))
            if userOption == 1:
                firstRow = int(input("1st row to swap: "))
                secondRow = int(input("2nd row to swap: "))
                rowOps.interchange(matrix, firstRow, secondRow)
                base.printGivenMatrix(matrix)
            elif userOption == 2:
                pass
            elif userOption == 3:
                pass
            else:
                raise ValueError
        except ValueError:
            print("Invalid option!")

    def reducedEchelon(matrix):
        print("test")

def main():
    userMatrix = []
    print("---------------------------------------------------------------------------------")
    print("-------------------Linear Alebra Calculator: Row Reduction ----------------------")
    print("---------------------------------------------------------------------------------")

    print("\n")

    numRows = int(input("Number of Columns ~ "))
    print("\n")
    numCols = int(input("Number of Rows ~ "))
    
    print("\n")

    print("Elements are entered from row to row...")
    print("\n")

    matrix = base.generateMatrix(numRows, numCols, userMatrix)

    print("\n")
    print("Here is your generated matrix...")
    print("\n")

    base.printGivenMatrix(matrix)

    print("Would you like your array in Regular Echelon Form or Reduced Echelon Form?")
    print("------------------------------(EF) or (REF)-------------------------------")

    try:
        userInput = input("Enter your choice: ")
        if userInput == "EF":
            base.regularEchelon(matrix)
        elif userInput == "REF":
            base.reducedEchelon(matrix)
        else:
            raise ValueError
    except ValueError:
        print("Invalid input :(")


if __name__ == '__main__':
    main()
