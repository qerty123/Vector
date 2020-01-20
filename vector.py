from math import sqrt, atan2, acos, cos


class Vector:
    def __init__(self, *values):
        self.values = values

    def __str__(self):
        text = ''
        for i in range(len(self.values)):
            text += str(self.values[i])
            if i != len(self.values) - 1:
                text += ', '
        text += ''
        return text

    def __round__(self, n=None):
        if n:
            for i in self.values:
                i.round(n)
        return self

    def __add__(self, other):
        values = []
        if type(other) is Vector or Vector in other.__class__.__bases__:
            if len(other.values) == len(self.values):
                for i in range(len(self.values)):
                    values.append(self.values[i] + other.values[i])
            else:
                raise IOError('Cannot add different sizes vectors')
        else:
            raise IOError('Can add only vectors')
        return Vector(*values)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        values = []
        if type(other) is Vector or Vector in other.__class__.__bases__:
            if len(other.values) == len(self.values):
                for i in range(len(self.values)):
                    values.append(self.values[i] - other.values[i])
            else:
                raise IOError('Cannot subtract different sizes vectors')
        else:
            raise IOError('Can subtract only vectors')
        return Vector(*values)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        values = []
        if type(other) is Vector or Vector in other.__class__.__bases__:
            if len(other.values) == len(self.values):
                length = self.length() * other.length() * cos(self.angle(other))
                return length
            else:
                raise IOError('Cannot multiply different sizes vectors')
        else:
            for i in self.values:
                values.append(i * other)
            return Vector(*values)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        values = []
        if type(other) is Vector or Vector in other.__class__.__bases__:
            raise IOError('Can divide only vectors')
        else:
            for i in self.values:
                values.append(i / other)
        return Vector(*values)

    def __idiv__(self, other):
        return self.__truediv__(other)

    def length(self):
        length = 0
        for i in self.values:
            length += i ** 2
        return sqrt(length)

    def length_squared(self):
        length = 0
        for i in self.values:
            length += i ** 2
        return length

    def normalize(self):
        normalize = self / self.length()
        return normalize

    def set_normalized(self):
        self.values = self.normalize().values
        return self

    def velocity(self, dtime, *new_values):
        if len(new_values) != len(self.values):
            raise IOError('Wrong size vector')
        dmove = Vector(*new_values) - Vector(*self.values)
        vel = dmove / dtime
        self.values = new_values
        return Vector(*vel.values)

    def velocity_ema(self, rate, dtime, *new_values):
        if len(new_values) != len(self.values):
            raise IOError('Wrong size vector')
        dmove = Vector(*new_values) * (1 - rate) - Vector(*self.values) * rate
        vel = dmove / dtime
        self.values = new_values
        return Vector(*vel.values)

    def dot(self, a, b=None):
        if type(b) is Vector or Vector in b.__class__.__bases__:
            length = a.length() * b.length() * cos(a.angle(b))
        else:
            length = self.length() * a.length() * cos(self.angle(a))
        return length

    def angle(self, a, b=None):
        amount = 0
        if type(b) is Vector or Vector in b.__class__.__bases__:
            if len(a.values) != len(b.values):
                raise IOError('Wrong size vector')
            for i in range(len(a.values)):
                amount += a.values[i] * b.values[i]
            angle = amount / (a.length() * b.length())
        else:
            if len(a.values) != len(self.values):
                raise IOError('Wrong size vector')
            for i in range(len(a.values)):
                amount += a.values[i] * self.values[i]
            angle = amount / (a.length() * self.length())
        return acos(angle)


class Vector2d(Vector):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    def __add__(self, other):
        values = super().__add__(other).values
        return Vector2d(*values)

    def __iadd__(self, other):
        values = super().__iadd__(other).values
        return Vector2d(*values)

    def __sub__(self, other):
        values = super().__sub__(other).values
        return Vector2d(*values)

    def __isub__(self, other):
        values = super().__isub__(other).values
        return Vector2d(*values)

    def __mul__(self, other):
        values = super().__mul__(other).values
        return Vector2d(*values)

    def __imul__(self, other):
        values = super().__imul__(other).values
        return Vector2d(*values)

    def __truediv__(self, other):
        values = super().__truediv__(other).values
        return Vector2d(*values)

    def __idiv__(self, other):
        values = super().__idiv__(other).values
        return Vector2d(*values)

    def x(self):
        return self.values[0]

    def y(self):
        return self.values[1]

    def azimuth(self):
        azimuth = atan2(self.x(), self.y())
        return azimuth

    def velocity(self, dtime, *new_values):
        vel = super().velocity(dtime, *new_values).values
        return Vector2d(*vel)

    def ema(self, rate, dtime, *new_values):
        vel = super().velocity(rate, dtime, *new_values).values
        return Vector2d(*vel)


class Vector3d(Vector):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z)

    def __add__(self, other):
        values = super().__add__(other).values
        return Vector3d(*values)

    def __iadd__(self, other):
        values = super().__iadd__(other).values
        return Vector3d(*values)

    def __sub__(self, other):
        values = super().__sub__(other).values
        return Vector3d(*values)

    def __isub__(self, other):
        values = super().__isub__(other).values
        return Vector3d(*values)

    def __mul__(self, other):
        values = super().__mul__(other).values
        return Vector3d(*values)

    def __imul__(self, other):
        values = super().__imul__(other).values
        return Vector3d(*values)

    def __truediv__(self, other):
        values = super().__truediv__(other).values
        return Vector3d(*values)

    def __idiv__(self, other):
        values = super().__idiv__(other).values
        return Vector3d(*values)

    def x(self):
        return self.values[0]

    def y(self):
        return self.values[1]

    def z(self):
        return self.values[2]

    def velocity(self, dtime, *new_values):
        vel = super().velocity(dtime, *new_values).values
        return Vector3d(*vel)

    def ema(self, rate, dtime, *new_values):
        vel = super().velocity(rate, dtime, *new_values).values
        return Vector3d(*vel)
