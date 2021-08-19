import pytest
from app import kek, lol

def test_lol():
    assert lol(1, 2) == 3

def test_kek():
    assert len(kek(2)) == 2
    assert kek(2)[0] == 1
    assert kek(2)[1] == 1
