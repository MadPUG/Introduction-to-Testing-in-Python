from example_module import (file_iterator, variadic_addition,
                            variadic_multiplication)
import random
import unittest


class TestExample(unittest.TestCase):
    def test_file_iterator_strips_newlines(self):
        """
        Assert the file iterator strips \n from
        yielded lines.
        """
        for line in file_iterator('example_module.py'):
            self.assertFalse(line.endswith('\n'))

    def test_file_iterator_removes_leading_whitespace(self):
        """
        Assert the file iterator strips whitespace
        from the start of yielded lines.
        """
        for line in file_iterator('example_module.py'):
            self.assertFalse(line.startswith(' '))

    def test_file_iterator_removes_all_whitespace(self):
        """
        Assert the file iterator strips whitespace
        from both ends of yielded lines.
        """
        for line in file_iterator('example_module.py'):
            self.assertEqual(line, line.strip())

    def assertIdentity(self, func):
        """
        Assert that ``func(x) == x``.
        """
        x = random.randint(0, 100)
        self.assertEqual(func(x), x)

    def test_variadic_addition_identity(self):
        """
        Assert that variadic_addition will
        calculate the sum of one argument.
        """
        self.assertIdentity(variadic_addition)

    def test_variadic_addition_takes_arbitrary_arguments(self):
        """
        Assert an arbitrary number of arguments
        is acceptable.
        """
        self.assertEqual(
            variadic_addition(1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15), 90
            )

    def test_variadic_multiplication_identity(self):
        """
        Assert variadic_multiplication will accept
        and multiply one argument.
        """
        self.assertIdentity(variadic_multiplication)

    def test_variadic_multiplication_takes_arbitrary_arguments(self):
        """Assert an arbitrary number of arguments is acceptable."""
        self.assertEqual(variadic_multiplication(1, 2, 3, 4, 5), 120)


if __name__ == '__main__':
    unittest.main()
