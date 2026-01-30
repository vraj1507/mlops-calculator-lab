"""
Pytest Tests for Modified Calculator - by Vraj Patel
"""
import sys
sys.path.insert(0, 'src')
from calculator import add, subtract, multiply, divide, power, modulo, compound_operation

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0.5, 0.3) == 0.8

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    """Test custom divide function"""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    try:
        divide(5, 0)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

def test_power():
    """Test custom power function"""
    assert power(2, 3) == 8
    assert power(5, 2) == 25

def test_modulo():
    """Test custom modulo function"""
    assert modulo(10, 3) == 1
    assert modulo(15, 4) == 3

def test_compound_operation():
    """Test custom compound operation"""
    assert compound_operation(2, 3, 4) == 20
