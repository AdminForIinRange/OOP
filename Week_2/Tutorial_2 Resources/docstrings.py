class Calculator:
    # Class Docstring
    """
    A class which represents a calculator.

    Attributes
    ----------
    sum : int
      number resulting from an addition.
    difference : int
      number resulting from a subtraction.
    product: float
      number resulting from a multiplication.
    quotient: float
      number resulting from a division.

    Methods
    -------
    add(a, b):
      Returns the addition of a and b.

    subtract(a, b):
      Returns the subtraction of a from b.

    multiply(a, b):
      Returns the multiplication of a and b.

    divide(a, b):
      Returns the division of a and b.
    """

    def __init__(self):
        self.sum = 0
        self.difference = 0
        self.product = 0
        self.quotient = 0

    def add(a, b):
        # Single Line Docstring
        """Returns the addition of a and b."""
        return a + b

    def subtract(a, b):
        """Returns the subtraction of a from b."""
        return a - b

    def multiply(a, b):
        """Returns the multiplication of a and b."""
        return a * b

    def divide(a, b):
        # Multiline docstring
        """ 
        Returns the division of a from b.

          Parameters:
            a (float): The dividend
            b (float): The divisor

          Returns:
            division (float): The resulting quotient
        """
        division = a / b
        return division


# help(Calculator.divide)
# help(Calculator)

print(Calculator.__doc__)
