# Credit      : LyFromQixing a.k.a QueenLy
# Date        : 12 November 2021
# Description : A program that accepts N input and writes a Pascal's triangular matrix of size N*N.

def pascal_matrix(N):

  # Creating Pascal's Triangular Matrix
  matrix = [[1 for i in range(N)] for j in range(N)]
  for i in range(1, N):
    for j in range(1, N):
      matrix[i][j] = (matrix[i-1][j] + matrix[i][j-1])

  # Showing matrix
  for i in range(N):
    print()
    for j in range(N):
      print(matrix[i][j], end=" ")

N = int(input("Insert N: "))

pascal_matrix(N)
