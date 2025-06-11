from plainder.classes.oche import OCHE
from plainder.classes.constante import palindrome

def test_true():
    assert True

def test_palindrome():
    oche_instance = OCHE()
    assert oche_instance.palindrome(palindrome) == True
