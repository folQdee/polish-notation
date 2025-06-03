import pytest
from polish import infix_to_rpn, evaluate_rpn

def test_infix_to_rpn():
    assert infix_to_rpn("3 + 4") == ['3', '4', '+']
    assert infix_to_rpn("3 + 4 * 2") == ['3', '4', '2', '*', '+']
    assert infix_to_rpn("( 3 + 4 ) * 2") == ['3', '4', '+', '2', '*']
    assert infix_to_rpn("3.5 + 4.2 * 2") == ['3.5', '4.2', '2', '*', '+']

def test_evaluate_rpn():
    assert evaluate_rpn(['3', '4', '+']) == 7
    assert evaluate_rpn(['3', '4', '2', '*', '+']) == 11
    assert evaluate_rpn(['3', '4', '+', '2', '*']) == 14
    assert evaluate_rpn(['3.5', '4.2', '2', '*', '+']) == pytest.approx(11.9)

def test_errors():
    with pytest.raises(ValueError):
        evaluate_rpn(['3', '4', '&'])
    with pytest.raises(ZeroDivisionError):
        evaluate_rpn(['3', '0', '/'])