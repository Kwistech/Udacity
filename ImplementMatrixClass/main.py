import numbers


def zeroes(height, width):
    """
    Creates a matrix of zeroes.
    """
    g = [[0.0 for _ in range(width)] for _ in range(height)]
    return Matrix(g)


def identity(n):
    """
    Creates a n x n identity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I


def dot_product(vector_one, vector_two):
    total = 0

    if len(vector_one) != len(vector_two):
        return total

    for i in range(len(vector_one)):
        product = vector_one[i] * vector_two[i]
        total += product

    return total


class Matrix(object):
    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):  # Done
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise (
            ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise (NotImplementedError,
                   "Calculating determinant not implemented for matrices "
                   "largerer than 2x2.")

        # TODO - your code here
        determinant = 0

        if self.h == 1:
            if self.g[0][0] == 0:
                return determinant
            determinant = 1.0 / self.g[0][0]
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            determinant = (a * d) - (b * c)

        return determinant * 1.0

    def trace(self):  # Done
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise (
            ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        total = 0

        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    total += self.g[i][j]

        return total

    def inverse(self):  # Done
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise (ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise (NotImplementedError,
                   "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        matrix_inv = []
        determinant = self.determinant()

        if self.h == 1:
            if determinant == 0:
                return
            matrix_inv = [[1.0 / self.g[0][0]]]
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            matrix_inv.append([d / determinant, -b / determinant])
            matrix_inv.append([-c / determinant, a / determinant])

        return Matrix(matrix_inv)

    def T(self):  # Done
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        t = []

        for i in range(self.w):
            new_row = []
            for j in range(self.h):
                new_row.append(self.g[j][i])
            t.append(new_row)

        return Matrix(t)

    def is_square(self):
        return self.h == self.w

        #

    # Begin Operator Overloading
    ############################
    def __getitem__(self, idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):  # Done
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError,
                   "Matrices can only be added if the dimensions are the same")
            #
        # TODO - your code here
        #
        matrix_sum = []

        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                total = self.g[i][j] + other[i][j]
                new_row.append(total)
            matrix_sum.append(new_row)

        return Matrix(matrix_sum)

    def __neg__(self):  # Done
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #
        # TODO - your code here
        #
        matrix_neg = []

        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append(-self.g[i][j])
            matrix_neg.append(new_row)

        return Matrix(matrix_neg)

    def __sub__(self, other):  # Done
        """
        Defines the behavior of - operator (as subtraction)
        """
        #
        # TODO - your code here
        #
        matrix_dif = []

        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                difference = self.g[i][j] - other[i][j]
                new_row.append(difference)
            matrix_dif.append(new_row)

        return Matrix(matrix_dif)

    def __mul__(self, other):  # Done
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #
        # TODO - your code here
        #
        matrix_mul = []

        for i in self.g:
            new_row = []
            for j in other.T():
                product = dot_product(i, j)
                new_row.append(product)
            matrix_mul.append(new_row)

        return Matrix(matrix_mul)

    def __rmul__(self, other):  # Done
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #
            # TODO - your code here
            #
            scalar = []

            for i in range(self.h):
                new_row = []
                for j in range(self.w):
                    product = self.g[i][j] * other
                    new_row.append(product)
                scalar.append(new_row)

            return Matrix(scalar)
