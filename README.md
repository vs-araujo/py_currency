# PyCurrency

## Monetary Currency class for Python
A simple Python class to work with monetary currency.

## Usage

### Creating the object
Create an instance of the class simply passing the value

```
>>> x = EUR(10000)
>>> print(x)
10 000,00 €
```

If value already in cents, it is possible to use the _format_ argument

```
>>> x = BRL(100, format='cents')
>>> print(x)
R$ 1,00
```

### Arithmetics
Object can be used on arithmetics

```
>>> x = BRL(1000)
>>> y = BRL(100)
>>> print(x + y)
R$ 1.100,00
>>> x / 2
R$ 500,00
>>> y * 10
R$ 1.000,00
>>> P = USD(1000)
>>> r, t = 0.1, 12
>>> P * (1 + r) ** t
US$ 3,138.43
```

## Available currencies

- BRL (Brazilian real)
- USD  (US dollar)
- EUR (Euro)
