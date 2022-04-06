import unittest
import py_currency


class TestCurrency(unittest.TestCase):
    def test_casting(self):
        # test if value is correctly stored as cents
        self.assertEqual(py_currency.Currency(10).value, 1000)
        self.assertEqual(py_currency.Currency(0.1).value, 10)
        self.assertEqual(py_currency.Currency(-1).value, -100)
        self.assertEqual(py_currency.Currency(100, format='cents').value, 100)

        # casting error
        with self.assertRaises(ValueError):
            # casting a string
            py_currency.Currency("10")
            py_currency.Currency("0.2")
            py_currency.Currency("number")

            # unsuported format
            py_currency.Currency(123, format='cent')
            py_currency.Currency(123.5, format='abc')

            # casting a float with format='cents'
            py_currency.Currency(123.5, format='cents')
            py_currency.Currency(5.0, format='cents')

    def test_string(self):
        # BRL
        self.assertEqual(py_currency.BRL(10).__str__(), "R$ 10,00")
        self.assertEqual(py_currency.BRL(0.2).__str__(), "R$ 0,20")
        self.assertEqual(py_currency.BRL(1000).__str__(), "R$ 1.000,00")
        self.assertEqual(py_currency.BRL(1000000).__str__(),
                         "R$ 1.000.000,00")
        self.assertEqual(py_currency.BRL(-1).__str__(), "R$ -1,00")

        # BRL
        self.assertEqual(py_currency.USD(10).__str__(), "US$ 10.00")
        self.assertEqual(py_currency.USD(0.2).__str__(), "US$ 0.20")
        self.assertEqual(py_currency.USD(1000).__str__(), "US$ 1,000.00")
        self.assertEqual(py_currency.USD(1000000).__str__(),
                         "US$ 1,000,000.00")
        self.assertEqual(py_currency.USD(-1).__str__(), "US$ -1.00")

        # EUR
        self.assertEqual(py_currency.EUR(10).__str__(), "10,00 €")
        self.assertEqual(py_currency.EUR(0.2).__str__(), "0,20 €")
        self.assertEqual(py_currency.EUR(1000000).__str__(),
                         "1 000 000,00 €")
        self.assertEqual(py_currency.EUR(-1).__str__(), "-1,00 €")

    def test_sum(self):
        # Currency + integer returns same Currency
        self.assertEqual(
            py_currency.Currency(100) + 1,
            py_currency.Currency(101)
            )
        self.assertEqual(
            py_currency.USD(1) + 2.1,
            py_currency.USD(3.1)
            )
        self.assertEqual(
            py_currency.BRL(0.1) + 0.1,
            py_currency.BRL(20, format='cents')
            )

        # same currency
        self.assertEqual(
            py_currency.Currency(1) + py_currency.Currency(1),
            py_currency.Currency(2)
            )
        self.assertEqual(
            py_currency.USD(-1) + py_currency.USD(1),
            py_currency.USD(0)
            )
        self.assertEqual(
            py_currency.EUR(-1) + py_currency.EUR(1),
            py_currency.EUR(0)
            )

        # sum errors
        with self.assertRaises(TypeError):
            (py_currency.Currency(1) + "1")

            # numeric + Currency
            (1 + py_currency.BRL(0.1))
            (10 + py_currency.USD(0.1))
            (0.50 + py_currency.USD(0.1))

            # different currency
            (py_currency.USD(2) + py_currency.BRL(0.1))
            (py_currency.BLR(2) + py_currency.EUR(0.1))
            (py_currency.EUR(2) + py_currency.Currency(0.1))


if __name__ == '__main__':
    unittest.main()
