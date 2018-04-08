# Given a 2d matrix, print the matrix spirally
# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

def print_spiral(matrix):
    # define boundaries
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    while top < bottom and left < right:
        # print top row
        i = left
        while i <= right:
            print(matrix[top][i], end=" ")
            i += 1
        top += 1

        # print right column
        i = top
        while i <= bottom:
            print(matrix[i][right], end=" ")
            i += 1
        right -= 1

        # print bottom row
        if top <= bottom:
            i = right
            while i >= left:
                print(matrix[bottom][i], end=" ")
                i -= 1
            bottom -= 1

        # print left column
        if left <= right:
            i = bottom
            while i >= top:
                print(matrix[i][left], end=" ")
                i -= 1
            left += 1


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]]
    print_spiral(matrix)
