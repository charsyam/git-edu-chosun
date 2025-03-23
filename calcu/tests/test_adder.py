import pytest

from calcu.adder import Adder


def test_adder_success():
    adder = Adder(1,2)
    assert adder.execute() == 3

def test_adder_should_fail():
    adder = Adder(1,2)
    assert adder.execute() != 4
    

def test_adder_success_with_minus_1():
    adder = Adder(-1,2)
    assert adder.execute() == 1


def test_adder_success_with_minus_2():
    adder = Adder(-1,-2)
    assert adder.execute() == -3
