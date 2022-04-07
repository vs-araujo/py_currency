class Currency:
    '''Generic currency class. All Currency classes store the variables:
    decimal:str -> decimal separator
    milliad:str -> milliard separator
    symbol:tuple -> 0: notation before the number
                    1: the notation after the number
'''
    symbol = ("", "")
    decimal = "."
    milliard = ""

    def __init__(self, value, format=None):
        '''Initializes and instance of the object.
value: Numeric value
format: use 'cents' if the value is and integer representing cents'''

        # store value as is if format is 'cents' and value is integer
        if format == "cents":
            if isinstance(value, int):
                self.value = value
            else:
                err_msg = "When format='cents', 'value' must be an integer"
                raise ValueError(err_msg) from None

        # if format None, convert value to cents it is numeric
        elif format is None:
            try:
                self.value = int(f"{value:.2f}".replace(".", ""))
            except ValueError:
                err_msg = f"Cannot convert {type(value)} to {self.__class__}"
                raise ValueError(err_msg) from None

        # raise error for invalid format option
        else:
            raise ValueError(
                f"'{format}' is not a valid argument for 'format'")

    def __str__(self):
        '''Formats the number for printing with right notation'''
        value = self.value / 100
        str_value = f"{value:,.2f}".replace(
                        ",", "_").replace(
                        ".", self.decimal).replace(
                        "_", self.milliard)

        return f"{self.symbol[0]} {str_value} {self.symbol[1]}".strip()

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        '''Defines behaviour for adding objects.
Adding same currency returns object of same class.
Currency + numeric: converst numeric and returns first's Currency'''
        # same currency
        if isinstance(other, self.__class__):
            value = self.value + other.value

        # try to convert second item to first's currency
        else:
            try:
                value = self.value + self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot add {type(other)} and {type(self)}"
                raise TypeError(err_msg) from None

        return self.__class__(round(value), format="cents")

    def __sub__(self, other):
        '''Define behaviour for subtracting objects.
Subtracting from same currency returns object of same class.
Currency - numeric: converst numeric and returns first's Currency'''
        # same currency
        if isinstance(other, self.__class__):
            value = self.value - other.value

        # try to convert second item to first's currency
        else:
            try:
                value = self.value - self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot subtract {type(other)} and {type(self)}"
                raise TypeError(err_msg) from None
        return self.__class__(round(value), format="cents")

    def __mul__(self, other):
        '''Define behaviour for multiplying objects.
Accepts only multiplication by numeric values.
Returns value in same Currency'''
        # try to multiply stored value and convert result back to Currency
        try:
            return self.__class__(round(self.value * other), format="cents")
        except (ValueError, TypeError):
            err_msg = f"Cannot multiply {type(self)} and {type(other)}"
            raise TypeError(err_msg) from None

    def __rmul__(self, other):
        '''numeric * Currency has same behaviour as Currency * numeric'''
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return self.value / other.value
        else:
            try:
                return self.__class__(round(self.value // other),
                                      format="cents")
            except (ValueError, TypeError):
                err_msg = f"Cannot divide {type(self)} by {type(other)}"
                raise TypeError(err_msg) from None

    def __floordiv__(self, other):
        if isinstance(other, self.__class__):
            return self.value // other.value
        else:
            try:
                return self.__class__(round(self.value // other),
                                      format="cents")
            except (ValueError, TypeError):
                err_msg = f"Cannot divide {type(self)} by {type(other)}"
                raise TypeError(err_msg) from None

    def __mod__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.value % other.value, format="cents")
        else:
            try:
                return self.__class__(round(self.value % other),
                                      format="cents")
            except (ValueError, TypeError):
                err_msg = f"Cannot divide {type(self)} by {type(other)}"
                raise TypeError(err_msg) from None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            value = self.value == other.value
        else:
            try:
                value = self.value == self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot compare {type(other)} and {type(self)}"
                raise TypeError(err_msg) from None
        return value

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            value = self.value < other.value
        else:
            try:
                value = self.value < self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot compare {type(other)} and {type(self)}"
                raise TypeError(err_msg) from None
        return value

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            value = self.value > other.value
        else:
            try:
                value = self.value > self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot compare {type(other)} and {type(self)}"
                raise TypeError(err_msg) from None
        return value

    def __le__(self, other):
        if isinstance(other, self.__class__):
            value = self.value <= other.value
        else:
            try:
                value = self.value <= self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot compare {type(other)} and {type(self)}"
                raise TypeError(err_msg) from None
        return value

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            value = self.value >= other.value
        else:
            try:
                value = self.value >= self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot compare {type(other)} and {type(self)}"
                raise TypeError(err_msg) from None
        return value


class BRL(Currency):
    '''Brazilian real'''
    symbol = ("R$", "")
    decimal = ","
    milliard = "."


class USD(Currency):
    '''US dollar'''
    symbol = ("US$", "")
    decimal = "."
    milliard = ","


class EUR(Currency):
    '''Euro'''
    symbol = ("", "€")
    decimal = ","
    milliard = " "
