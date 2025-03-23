import pytest

from calcu.adder import Adder


def test_adder_success():
    adder = Adder(1,2)
    assert adder.execute() == 3
    
