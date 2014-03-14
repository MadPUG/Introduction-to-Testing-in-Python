from example_module import (file_iterator, variadic_addition,
                            variadic_multiplication)
import pytest
import random


def test_file_iterator_strips_newlines():
    """
    Assert the file iterator strips \n from
    yielded lines.
    """
    for line in file_iterator('example_module.py'):
        assert line.endswith('\n') is False


def test_file_iterator_removes_leading_whitespace():
    """
    Assert the file iterator strips whitespace
    from the start of yielded lines.
    """
    for line in file_iterator('example_module.py'):
        assert line.startswith(' ') is False


def test_file_iterator_removes_all_whitespace():
    """
    Assert the file iterator strips whitespace
    from both ends of yielded lines.
    """
    for line in file_iterator('example_module.py'):
        assert line == line.strip('\n')

@pytest.fixture
def x():
    return random.randint(1, 100)

def test_variadic_addition_identity(x):
    """
    Assert that variadic_addition will
    calculate the sum of one argument.
    """
    assert variadic_addition(x) == x
