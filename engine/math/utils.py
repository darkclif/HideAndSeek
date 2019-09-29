import math

####################################################################################
#### Constans ######################################################################
####################################################################################
pi = 3.141592

####################################################################################
#### Base matrix ###################################################################
####################################################################################
class BaseMatrix():
    """Base class for transformations and vectors
    """
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._mat = self.__zeros(rows, cols)

    # Helpers
    @staticmethod
    def _zeros(rows, cols):
        return [0] * rows * cols

    @staticmethod
    def _identity(size):
        return (([1] + [0] * size) * size)[:-size]

    # Contructor
    @classmethod
    def identity(cls, rows):
        new = cls(rows, rows)
        new._mat = cls.__identity(rows)
        return new

    #### Print #####################################################################
    def __str__(self, fmt = "{:02.2f}"):
        ret_str = ""
        for i in range(self._rows):
            ret_str += "[" + ", ".join([fmt.format(el) for el in self._mat[self._cols * i:self._cols * (i + 1)] ]) + "]\n"
        return ret_str

    ### Special ####################################################################
    def transpose(self):
        new = BaseMatrix(self._cols, self._rows) # Cols and rows swaped!
        new._mat = _mat[:]
        return new

    #### Operators #################################################################
    def __eq__(self, mat):
        if (self._cols != mat._cols) or (self._rows != mat._rows):
            raise Exception("Cannot compare matrices of this size, first [{self._rows},{self._cols}] second [{mat._rows},{mat._cols}]")

        return all(abs(n) < 0.00001 for n in [x - y for x, y in zip(self._mat, mat._mat)])

    def __mul__(self, mat):
        if self._cols != mat._rows:
            raise Exception("Cannot multiply matrices of this size, first [{self._rows},{self._cols}] second [{mat._rows},{mat._cols}]")

        new = BaseMatrix(self._rows, mat._cols)

        for i in range(new._rows):
            for j in range(new._cols):
                acc = 0
                for k in range(self._cols):
                    acc += self._mat[j * self._cols + k] * mat._mat[k * self._cols + i]
                new._mat[i * new._cols + j] = acc

        return new

    def __add__(self, mat):
        if (self._cols != mat._cols) or (self._rows != mat._rows):
            raise Exception("Cannot add matrices of this size, first [{self._rows},{self._cols}] second [{mat._rows},{mat._cols}]")

        new = BaseMatrix(self._rows, self._cols)
        new._mat = [self._mat[i] + mat._mat[i] for i in range(new._rows * new._cols)]

        return new

    def __sub__(self, mat):
        if (self._cols != mat._cols) or (self._rows != mat._rows):
            raise Exception("Cannot add matrices of this size, first [{self._rows},{self._cols}] second [{mat._rows},{mat._cols}]")

        new = BaseMatrix(self._rows, self._cols)
        new._mat = [self._mat[i] - mat._mat[i] for i in range(new._rows * new._cols)]

        return new

    def __neg__(self):
        new = BaseMatrix(self._rows, self._cols)
        new._mat = [-n for n in self._mat]

        return new

####################################################################################
#### Transform matrix 2D ###########################################################
####################################################################################
class Transform2D(BaseMatrix):
    """Class for 2D transformations
    """
    def __init__(self):
        self._rows = 3
        self._cols = 3
        self._mat = self._identity(3)

    # Constructor
    @classmethod
    def identity(cls):
        new = cls()
        new._mat = cls._identity(3)
        return new

    @classmethod
    def rotation(cls, alpha):
        """Returns rotation transform matrix
        
        Arguments:
            alpha {float} -- Angle of rotation in radians
        """
        new = cls()
        new._mat[0 * new._cols + 0] = math.cos(alpha)
        new._mat[0 * new._cols + 1] = math.sin(alpha)
        new._mat[1 * new._cols + 0] = -math.sin(alpha)
        new._mat[1 * new._cols + 1] = math.cos(alpha)
        return new
    
    @classmethod
    def scale(cls, x, y = None):
        """Returns scale transform matrix
        
        Arguments:
            x {float} -- horizontal scale factor
        
        Keyword Arguments:
            y {float} -- vertical scale factor (default: same as x)
        """
        if not y:
            y = x
        
        new = cls()
        new._mat[0 * new._cols + 0] = x
        new._mat[1 * new._cols + 1] = y
        return new

    @classmethod
    def translation(cls, vect):
        """Returns translation transform matrix
        
        Arguments:
            vect {Vector2D} -- 2d vector of translation 
        """
        new = cls()
        new._mat[0 * new._cols + 2] = vect.x
        new._mat[1 * new._cols + 2] = vect.y
        return new

####################################################################################
#### Vect 3D #######################################################################
####################################################################################
class Vect3D():
    """Vector 3D
    """
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    # Return array
    def to_array(self):
        return [self._x, self._y, self._z]

    #### Getters / Setters #########################################################
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self):
        self._y = y

    @property
    def z(self):
        return self._z

    @y.setter
    def z(self):
        self._z = z

    #### Special #########################################################
    def point_distance(self, point):
        return math.sqrt((self._x - point._x)**2 + (self._y - point._y)**2 + (self._z - point._z)**2)

    def normalize(self):
        l = self.length() 
        return Vect3D(self._x / l, self._y / l, self._z / l)

    def cross(self, vect):
        return Vect3D(self._y*vect._z - self._z*vect._y, self._z*vect._x - self._x*vect._z, self._x*vect._y - self._y*vect._x)

    def dot(self, vect):
        return Vect3D(self._x * vect.x, self._y * vect.y, self._z * vect.z)

    def length(self):
        return math.sqrt(self._x**2 + self._y**2 + self._z**2)

    #### Operators #######################################################
    def __neg__(self):
        return Vector3D(-self._x, -self._y, -self._z)

    # Vector * Scalar
    def __mul__(self, scalar):
        return Vector3D(scalar * self._x, scalar * self._y, scalar * self._z)

    def __add__(self, vect):
        return Vector3D(self._x + vect._x, self._y + vect._y, self._z + vect._z)

    def __sub__(self, vect):
        return Point2D(self._x - vect._x, self._y - vect._y, self._z - vect._z)

    def __eq__(self, vect):
        return (self._x == vect._x) and (self._y == vect._y) and (self._z == vect._z)

####################################################################################
#### Vect 2D #######################################################################
####################################################################################
class Vect2D():
    """Vector 2D
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Return array
    def to_array(self):
        return [self._x, self._y]

    #### Getters / Setters #########################################################
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self):
        self._y = y

    #### Special #########################################################
    def point_distance(self, point):
        return math.sqrt((self._x - point._x)**2 + (self._y - point._y)**2)

    def normalize(self):
        l = self.length() 
        return Vect2D(self._x / l, self._y / l)

    def dot(self, vect):
        return Vect2D(self._x * vect.x, self._y * vect.y)

    def length(self):
        return math.sqrt(self._x**2 + self._y**2)

    #### Operators #######################################################
    def __neg__(self):
        return Vect2D(-self._x, -self._y)

    # Vector * Scalar
    def __mul__(self, scalar):
        return Vect2D(scalar * self._x, scalar * self._y)

    def __add__(self, vect):
        return Vect2D(self._x + vect._x, self._y + vect._y)

    def __sub__(self, vect):
        return Vect2D(self._x - vect._x, self._y - vect._y)

    def __eq__(self, vect):
        return (self._x == vect._x) and (self._y == vect._y)
