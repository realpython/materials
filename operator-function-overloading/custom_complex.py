from math import hypot, atan2, sin, cos


class CustomComplex:
    """
    A class to represent a complex number, a+bj.
    Attributes:
        real - int or float, representing the real part
        imag - int or float, representing the imaginary part

    Implements the following:

    * Addition with a complex number or a real number using `+`
    * Multiplication with a complex number or a real number using `*`
    * Subtraction of a complex number or a real number using `-`
    * Calculation of absolute value using `abs`
    * Raise complex number to a power using `**`
    * Nice string representation using `__repr__`
    * Nice user-end viewing using `__str__`

    Notes:
        * The constructor has been intentionally kept simple
        * It is configured to support one kind of call:
            CustomComplex(a, b)
        * Error handling was avoided to keep things simple
    """

    def __init__(self, real, imag):
        """
        Initializes a complex number, setting real and imag part
        Arguments:
            real: Number, real part of the complex number
            imag: Number, imaginary part of the complex number
        """
        self.real = real
        self.imag = imag

    def conjugate(self):
        """
        Returns the complex conjugate of a complex number
        Return:
            CustomComplex instance
        """
        return self.__class__(self.real, -self.imag)

    def argz(self):
        """
        Returns the argument of a complex number
        The argument is given by:
            atan2(imag_part, real_part)
        Return:
            float
        """
        return atan2(self.imag, self.real)

    def __abs__(self):
        """
        Returns the modulus of a complex number
        Return:
            float
        """
        return hypot(self.real, self.imag)

    def __repr__(self):
        """
        Returns str representation of an instance of the
        class. Can be used with eval() to get another
        instance of the class
        Return:
            str
        """
        return f"{self.__class__.__name__}({self.real}, {self.imag})"

    def __str__(self):
        """
        Returns user-friendly str representation of an instance
        of the class
        Return:
            str
        """
        return f"({self.real}{self.imag:+}j)"

    def __add__(self, other):
        """
        Returns the addition of a complex number with
        int, float or another complex number
        Return:
            CustomComplex instance
        """
        if isinstance(other, (int, float)):
            real_part = self.real + other
            imag_part = self.imag
        elif isinstance(other, CustomComplex):
            real_part = self.real + other.real
            imag_part = self.imag + other.imag
        else:
            return NotImplemented

        return self.__class__(real_part, imag_part)

    def __sub__(self, other):
        """
        Returns the subtraction from a complex number of
        int, float or another complex number
        Return:
            CustomComplex instance
        """
        if isinstance(other, (int, float)):
            real_part = self.real - other
            imag_part = self.imag
        elif isinstance(other, CustomComplex):
            real_part = self.real - other.real
            imag_part = self.imag - other.imag
        else:
            return NotImplemented

        return self.__class__(real_part, imag_part)

    def __mul__(self, other):
        """
        Returns the multiplication of a complex number with
        int, float or another complex number
        Return:
            CustomComplex instance
        """
        if isinstance(other, (int, float)):
            real_part = self.real * other
            imag_part = self.imag * other
        elif isinstance(other, CustomComplex):
            real_part = (self.real * other.real) - (self.imag * other.imag)
            imag_part = (self.real * other.imag) + (self.imag * other.real)
        else:
            return NotImplemented

        return self.__class__(real_part, imag_part)

    def __radd__(self, other):
        """
        Same as __add__; allows 1 + CustomComplex(x, y)
        x + y == y + x
        """
        return self.__add__(other)

    def __rmul__(self, other):
        """
        Same as __mul__; allows 2 * CustomComplex(x, y)
        x * y == y * x
        """
        return self.__mul__(other)

    def __rsub__(self, other):
        """
        Returns the subtraction of a complex number from
        int or float
        x - y != y - x
        Subtraction of another complex number is not handled by __rsub__
        Instead, __sub__ handles it since both sides are instances of
        this class
        Return:
            CustomComplex instance
        """
        if isinstance(other, (int, float)):
            real_part = other - self.real
            imag_part = -self.imag
        else:
            return NotImplemented

        return self.__class__(real_part, imag_part)

    def __eq__(self, other):
        """
        Checks equality of two complex numbers
        Two complex numbers are equal when:
            * Their real parts are equal AND
            * Their imaginary parts are equal
        Return:
            bool
        """
        if not isinstance(other, (int, float, CustomComplex)):
            return NotImplemented
        # Note: comparing floats directly is not a good idea in general
        # due to floating-point precision
        return (self.real == other.real) and (self.imag == other.imag)

    def __ne__(self, other):
        """
        Checks inequality of two complex numbers
        Two complex numbers are unequal when:
            * Their real parts are unequal OR
            * Their imaginary parts are unequal
        Return:
            bool
        """
        if not isinstance(other, (int, float, CustomComplex)):
            return NotImplemented
        return (self.real != other.real) or (self.imag != other.imag)

    def __pow__(self, other):
        """
        Raises a complex number to a power
        Formula:
            z**n = (r**n)*[cos(n*argz) + sin(n*argz)j], where
            z = complex number
            n = power
            r = absolute value of z
            argz = argument of z
        Return:
            CustomComplex instance
        """
        r_raised = abs(self) ** other
        argz_multiplied = self.argz() * other

        real_part = round(r_raised * cos(argz_multiplied))
        imag_part = round(r_raised * sin(argz_multiplied))

        return self.__class__(real_part, imag_part)
