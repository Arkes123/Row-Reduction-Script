class rowOps:
    def interchange(matrix, i, j):
        matrix[i], matrix[j] = matrix[j], matrix[i]
        return matrix

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
    def reducedEchelon(matrix):
        
        m = matrix.userMatrix

        if not matrix:
            return
        
        numRows = matrix.numRows
        numCols = matrix.numCols
        lead = 0

        for r in range(numRows):
            if lead >= numCols:
                return
            i = r
            
            while m[i][lead] == 0:
                i += 1
                if i == numRows:
                    i = r
                    lead += 1
                    if numCols == lead:
                        return
                
            rowOps.interchange(m, i, r)
            lv = m[r][lead]

            m[r] = [ mrx / float(lv) for mrx in m[r]]

            for i in range(numRows):
                if i != r:
                    lv = m[i][lead]
                    m[i] = [iv - lv * rv for rv, iv in zip(m[r], m[i])]
            lead += 1

        matrix.userMatrix = m
        return matrix
                
        

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

    matrix = base.generateMatrix(numCols, numRows, userMatrix)

    print("\n")
    print("Here is your generated matrix...")
    print("\n")

    base.printGivenMatrix(matrix)

    print("------------------------------Reduced Echelon Form-------------------------------")
    print("\n")
    base.printGivenMatrix(base.reducedEchelon(matrix))
    


if __name__ == '__main__':
    main()
