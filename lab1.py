import numpy as np

class Simplex:
    Matrix = None
    col = None
    row = None

    def __init__(self, c, b, Matrix, var):
        self.Matrix = np.zeros((len(c) + 1, len(b) + 1))

        if var == True:
            Matrix = Matrix.T * -1
            c, b = b * -1, c * -1


        for i in range(0, len(c)):
            self.Matrix[i][0] = b[i]
            for j in range(1, len(c) + 1):
                self.Matrix[i][j] = Matrix[i][j - 1]

        for i in range(1, len(c) + 1):
            self.Matrix[-1][i] = c[i-1]

        self.col = ["X4", "X5", "X6", "F"]
        self.row = ["S0","X1", "X2", "X3"]

        self.printMatrix(self.Matrix)
        print()

    def check_row_col(self, col, row):
        check = False
        for i in range(0, len(self.Matrix) - 1):
            if self.Matrix[i][0] < 0:
                check = True;
                col = i
                break

        if check == True:
            for i in range(1, len(self.Matrix)):
                if self.Matrix[col][i] < 0:
                    row = i
                    break
        return check, col, row

    def start(self):
        flag = self.check()
        while flag == False:
            row = 0
            col = 0
            test = self.check_row_col(col, row)
            if test[0] == False:
                row = self.find_row()
                col = self.find_col(row)
            else:
                col = test[1]
                row = test[2]

            x = self.row[row]
            self.row[row] = self.col[col]
            self.col[col] = x

            self.recounting(row, col)
            self.printMatrix(self.Matrix)
            print()
            flag = self.check()

    def printMatrix (self, matrix):
       print("{:>10}".format(""), end = "")
       for i in range (0, len(self.col)):
          print("{:>10}".format(self.row[i]), end = "")
       print()
       for i in range (0, len(matrix)):
          print("{:>10}".format(self.col[i]), end = "")
          for j in range (0, len(matrix[i])):
              print ( "{:>10}".format(matrix[i][j]), end = "" )
          print ()


    def recounting(self, row, col):
        Matrix = np.zeros((len(self.Matrix), len(self.Matrix[0])))
        razr = self.Matrix[col][row];

        Matrix[col][row] = round(1 / razr, 3);

        for i in range(0, len(self.Matrix[0])):
            if i != row:
                Matrix[col][i] = round(self.Matrix[col][i] / razr, 3)

        for i in range(0, 4):
            if i != col and self.Matrix[i][row] != 0:
                Matrix[i][row] =  round(self.Matrix[i][row] / -razr, 3)



        for i in range(0, len(self.Matrix)):
            for j in range(0, len(self.Matrix[i])):
                if i != col and j != row:
                    Matrix[i][j] = round(self.Matrix[i][j] - (self.Matrix[i][row] * self.Matrix[col][j] / razr), 3);

        self.Matrix = Matrix


    def find_col(self, row):
        col = 0

        for i in range(1, len(self.Matrix) - 1):
            check = 100
            if self.Matrix[i-1][row] != 0:
                check = self.Matrix[i-1][0] / self.Matrix[i-1][row];

            if self.Matrix[i][row] != 0:
                if check > self.Matrix[i][0] / self.Matrix[i][row] and self.Matrix[i][0] / self.Matrix[i][row] > 0:
                    col = i;
        return col

    def find_row(self):
        row = 1
        for i in range(1, len(self.Matrix[-1])):
            row = i
            if self.Matrix[-1][i] > 0:
                break
        return row

    def check(self):
        flag = True
        for i in range(1, len(self.Matrix)):
            if self.Matrix[len(self.Matrix) - i - 1][0] < 0:
                flag = False
            if self.Matrix[len(self.Matrix) - 1][i] > 0:
                flag = False
        return flag

def main():
    c = np.array([2, 8, 3])
    b = np.array([4, 6, 2])
    matrix = np.array([[2.0, 1.0, 1.0], [1.0, 2.0, 0.0], [0.0, 0.5, 1.0]])

    print("First")
    One = Simplex(c, b, matrix, False)
    One.start()

    print("second")
    Two = Simplex(c, b, matrix, True)
    Two.start()

if __name__ == '__main__':
    main()
