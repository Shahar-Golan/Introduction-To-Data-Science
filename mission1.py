import math


class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if self.is_complex:
            self.a = a
            self.b = b

    @property
    # here we create a function that checks the input
    def is_complex(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise ValueError("Both parameters must be real numbers.")
        return True

    @property
    def re(self):
        return self.a

    @property
    def im(self):
        return self.b

    def to_tuple(self):
        return self.a, self.b

    def __repr__(self):
        return f"{self.a} + {self.b}i"

    def __eq__(self, other):
        if other.is_complex:
            return self.a == other.a and self.b == other.b

    def __add__(self, other):
        if other.is_complex:
            return ComplexNum(self.a + other.a, self.b + other.b)

    def __neg__(self):
        return ComplexNum(-self.a, -self.b)

    def __sub__(self, other):
        if other.is_complex:
            return self.__add__(other.__neg__())

    def __mul__(self, other):
        if other.is_complex:
            # here we subtract the bi*di because there is i^2
            return ComplexNum(self.a * other.a - (self.b * other.b),
                              self.a * other.b + self.b * other.a)

    def conjugate(self):
        return ComplexNum(self.a, -self.b)

    def abs(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)


'''
# Creating instances
c1 = ComplexNum(3, 4)
c2 = ComplexNum(1, 2)
c3 = ComplexNum(3, 4)

# Testing addition
print(f"Addition of {c1} and {c2}: {c1 + c2}")

# Testing subtraction
print(f"Subtraction of {c1} from {c2}: {c2 - c1}")

# Testing multiplication
print(f"Multiplication of {c1} and {c2}: {c1 * c2}")

# Testing negation
print(f"Negation of {c1}: {-c1}")

# Testing equality
print(f"Checking if {c1} is equal to {c3}: {c1 == c3}")
print(f"Checking if {c1} is equal to {c2}: {c1 == c2}")

# Testing absolute value
print(f"Absolute value of {c1}: {c1.abs()}")

# Testing conjugate
print(f"Conjugate of {c1}: {c1.conjugate()}")

'''

z = ComplexNum(1, 2)

print(str(z))

print(z == ComplexNum(1, 1))
print(z.abs())
