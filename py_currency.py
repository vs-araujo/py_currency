class Currency:
    symbol = ""
    decimal = "."
    milliard = ""

    def __init__(self, value, cents=False):
        if cents:
            if isinstance(value, int):
                self.value = value
            else:
                err_msg = "When 'cents=True', 'value' must be an integer'"
                raise ValueError(err_msg)

        else:
            try:
                self.value = int(f"{value:.2f}".replace(".", ""))
            except ValueError:
                err_msg = f"Cannot convert {type(value)} to {self.__class__}"
                raise ValueError(err_msg) from None

    def __str__(self):
        value = self.value / 100
        value = f"{value:,.2f}".replace(",", "_")
        value = value.replace(".", self.decimal)
        value = value.replace("_", self.milliard)
        return f"{self.symbol} {value}"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, self.__class__):
            value = self.value + other.value
        else:
            try:
                value = self.value + self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot add {type(other)} and {type(self)}"
                raise ValueError(err_msg) from None
        return self.__class__(round(value / 100, 2))

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            value = self.value - other.value
        else:
            try:
                value = self.value - self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot subtract {type(other)} and {type(self)}"
                raise ValueError(err_msg) from None
        return self.__class__(round(value / 100, 2))

    def __mul__(self, other):
        return self.__class__(round(self.value * other / 100, 2))

    def __truediv__(self, other):
        return self.__class__(round(self.value / (100 * other), 2))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            value = self.value == other.value
        else:
            try:
                value = self.value == self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot compare {type(other)} and {type(self)}"
                raise ValueError(err_msg) from None
        return value

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            value = self.value < other.value
        else:
            try:
                value = self.value < self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot compare {type(other)} and {type(self)}"
                raise ValueError(err_msg) from None
        return value

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            value = self.value > other.value
        else:
            try:
                value = self.value > self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot compare {type(other)} and {type(self)}"
                raise ValueError(err_msg) from None
        return value

    def __le__(self, other):
        if isinstance(other, self.__class__):
            value = self.value <= other.value
        else:
            try:
                value = self.value <= self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot compare {type(other)} and {type(self)}"
                raise ValueError(err_msg) from None
        return value

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            value = self.value >= other.value
        else:
            try:
                value = self.value >= self.__class__(other).value
            except (ValueError, TypeError):
                err_msg = f"Cannot compare {type(other)} and {type(self)}"
                raise ValueError(err_msg) from None
        return value


class BRL(Currency):
    symbol = "R$"
    decimal = ","
    milliard = "."


class USD(Currency):
    symbol = "US$"
    decimal = "."
    milliard = ","
