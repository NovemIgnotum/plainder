from plainde.classes import oche
from plainde.classes import constante

# PYTHONPATH=. pytest test/

def test_true():
    assert True

def test_palindrome():
    oche_instance = oche.OCHE()
    assert oche_instance.palindrome(constante.palindrome) == True