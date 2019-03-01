from fibonacci import naive, dynamic
import pytest


def pytest_generate_tests(metafunc):
    # fibonacci sequence
    fib = [[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]]
    if 'fib' in metafunc.fixturenames:
        metafunc.parametrize('fib', fib)


def test_naive(fib):
    for i in range(len(fib)):
        assert naive(i) == fib[i]


def test_dynamic(fib):
    for i in range(len(fib)):
        assert dynamic(i) == fib[i]
