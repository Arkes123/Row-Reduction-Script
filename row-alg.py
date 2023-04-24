class rowOperations:
    def interchange(matrix, i, j):
        matrix[i], matrix[j] = matrix[j], matrix[i]
        return matrix


    def scaling(matrix, i, j):
        pass


    def addRowToScaler(matrix, i, j):
        pass

class matrixFunctions:
    def __init__(self):
        pass



def generateMatrix(numRows, numCols, matrix):
    count = 0
    for i in range(numRows):
        rows = []
        for j in range(numCols):
            rows.append(int(input("Enter an element: ")))
        matrix.append(rows)

    print("\n")
    print("Here is your generated matrix...")
    print("\n")

    for i in range(numRows):
        for j in range(numCols):
            print(matrix[i][j], end=" ")
        print()

def presentOperations():
    print("1) Interchange rows")
    print("2) Scale a row by a real number")
    print("3) Add a row to a scalar multiple of another")

def regularEchelon(matrix):
    print("Here is you matrix...")
    print("\n")

    print("What operation would you like to perform? ")
    presentOperations()

    try:
        userOption = int(input("Enter option: "))
        if userOption == 1:
            firstRow = int(input("1st row to swap: "))
            secondRow = int(input("2nd row to swap: "))
            rowOperations.interchange(matrix, firstRow, secondRow)
            print(matrix)
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

    generateMatrix(numCols, numRows, userMatrix)

    print("Would you like your array in Regular Echelon Form or Reduced Echelon Form?")
    print("------------------------------(EF) or (REF)-------------------------------")

    try:
        userInput = input("Enter your choice: ")
        if userInput == "EF":
            regularEchelon(userMatrix)
        elif userInput == "REF":
            reducedEchelon(userMatrix)
        else:
            raise ValueError
    except ValueError:
        print("Invalid input :(")

            

    




if __name__ == '__main__':
    main()
