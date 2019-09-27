import math

####################################################################################
#### Vect 3D #######################################################################
####################################################################################
class Vect3D():
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    # Return array
    def to_array(self):
        return [self._x, self._y, self._z]

    # Special
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

    # Unary
    def __neg__(self):
        return Vector3D(-self._x, -self._y, -self._z)

    # Vector * Scalar
    def __mul__(self, scalar):
        return Vector3D(scalar * self._x, scalar * self._y, scalar * self._z)

    # Vector (?) Vector
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
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Return array
    def to_array(self):
        return [self._x, self._y]

    # Special
    def point_distance(self, point):
        return math.sqrt((self._x - point._x)**2 + (self._y - point._y)**2)

    def normalize(self):
        l = self.length() 
        return Vect2D(self._x / l, self._y / l)

    def dot(self, vect):
        return Vect2D(self._x * vect.x, self._y * vect.y)

    def length(self):
        return math.sqrt(self._x**2 + self._y**2)

    # Unary
    def __neg__(self):
        return Vect2D(-self._x, -self._y)

    # Vector * Scalar
    def __mul__(self, scalar):
        return Vect2D(scalar * self._x, scalar * self._y)

    # Vector (?) Vector
    def __add__(self, vect):
        return Vect2D(self._x + vect._x, self._y + vect._y)

    def __sub__(self, vect):
        return Vect2D(self._x - vect._x, self._y - vect._y)

    def __eq__(self, vect):
        return (self._x == vect._x) and (self._y == vect._y)