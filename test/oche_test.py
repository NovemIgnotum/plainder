"""
Tests unitaires pour les fonctions palindrome et salutation
"""

import unittest
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from plainde.classes import oche


class TestPalindrome(unittest.TestCase):
    """Tests pour la fonction oche.OCHE.is_palindrome"""
    
    def test_simple_palindrome(self):
        """Test avec des mots simples palindromes"""
        self.assertTrue(oche.OCHE.is_palindrome('radar'))
        self.assertTrue(oche.OCHE.is_palindrome('kayak'))
        self.assertTrue(oche.OCHE.is_palindrome('level'))
    
    def test_simple_non_palindrome(self):
        """Test avec des mots simples non palindromes"""
        self.assertFalse(oche.OCHE.is_palindrome('hello'))
        self.assertFalse(oche.OCHE.is_palindrome('world'))
        self.assertFalse(oche.OCHE.is_palindrome('python'))
    
    def test_phrase_palindrome_with_spaces(self):
        """Test avec des phrases palindromes contenant des espaces"""
        self.assertTrue(oche.OCHE.is_palindrome('A man a plan a canal Panama'))
        self.assertTrue(oche.OCHE.is_palindrome('race a car'))
        self.assertTrue(oche.OCHE.is_palindrome('step on no pets'))
    
    def test_phrase_with_punctuation(self):
        """Test avec des phrases contenant de la ponctuation"""
        self.assertTrue(oche.OCHE.is_palindrome('Madam, I\'m Adam'))
        self.assertTrue(oche.OCHE.is_palindrome('Was it a car or a cat I saw?'))
        self.assertTrue(oche.OCHE.is_palindrome('A Santa at NASA'))
    
    def test_french_palindromes(self):
        """Test avec des palindromes français"""
        self.assertTrue(oche.OCHE.is_palindrome('Elu par cette crapule'))
        self.assertTrue(oche.OCHE.is_palindrome('ressasser'))
        self.assertTrue(oche.OCHE.is_palindrome('été'))
    
    def test_numeric_palindromes(self):
        """Test avec des palindromes numériques"""
        self.assertTrue(oche.OCHE.is_palindrome('12321'))
        self.assertTrue(oche.OCHE.is_palindrome('1001'))
        self.assertTrue(oche.OCHE.is_palindrome('7337'))
    
    def test_mixed_alphanumeric(self):
        """Test avec des palindromes alphanumériques"""
        self.assertTrue(oche.OCHE.is_palindrome('A1B2b1a'))
        self.assertTrue(oche.OCHE.is_palindrome('1a2b2a1'))
    
    def test_empty_string(self):
        """Test avec une chaîne vide"""
        self.assertTrue(oche.OCHE.is_palindrome(''))
    
    def test_single_character(self):
        """Test avec un caractère unique"""
        self.assertTrue(oche.OCHE.is_palindrome('a'))
        self.assertTrue(oche.OCHE.is_palindrome('Z'))
        self.assertTrue(oche.OCHE.is_palindrome('5'))
    
    def test_case_insensitive(self):
        """Test de la insensibilité à la casse"""
        self.assertTrue(oche.OCHE.is_palindrome('RaceCar'))
        self.assertTrue(oche.OCHE.is_palindrome('MadAm'))
    
    def test_invalid_types(self):
        """Test avec des types invalides"""
        self.assertFalse(oche.OCHE.is_palindrome(123))
        self.assertFalse(oche.OCHE.is_palindrome(None))
        self.assertFalse(oche.OCHE.is_palindrome([]))
        self.assertFalse(oche.OCHE.is_palindrome({}))


class TestSalutation(unittest.TestCase):
    """Tests pour la fonction oche.OCHE.get_salutation"""
    
    def test_morning_salutation(self):
        """Test salutation du matin"""
        morning_time = datetime(2024, 1, 1, 8, 0, 0)
        self.assertEqual(oche.OCHE.get_salutation(morning_time), 'Bonjour')
        
        early_morning = datetime(2024, 1, 1, 5, 0, 0)
        self.assertEqual(oche.OCHE.get_salutation(early_morning), 'Bonjour')
        
        late_morning = datetime(2024, 1, 1, 11, 59, 59)
        self.assertEqual(oche.OCHE.get_salutation(late_morning), 'Bonjour')
    
    def test_afternoon_salutation(self):
        """Test salutation de l'après-midi"""
        afternoon_time = datetime(2024, 1, 1, 14, 0, 0)
        self.assertEqual(oche.OCHE.get_salutation(afternoon_time), 'Bon après-midi')
        
        noon = datetime(2024, 1, 1, 12, 0, 0)
        self.assertEqual(oche.OCHE.get_salutation(noon), 'Bon après-midi')
        
        late_afternoon = datetime(2024, 1, 1, 17, 59, 59)
        self.assertEqual(oche.OCHE.get_salutation(late_afternoon), 'Bon après-midi')
    
    def test_evening_salutation(self):
        """Test salutation du soir"""
        evening_time = datetime(2024, 1, 1, 19, 0, 0)
        self.assertEqual(oche.OCHE.get_salutation(evening_time), 'Bonsoir')
        
        early_evening = datetime(2024, 1, 1, 18, 0, 0)
        self.assertEqual(oche.OCHE.get_salutation(early_evening), 'Bonsoir')
        
        late_evening = datetime(2024, 1, 1, 21, 59, 59)
        self.assertEqual(oche.OCHE.get_salutation(late_evening), 'Bonsoir')
    
    def test_night_salutation(self):
        """Test salutation de la nuit"""
        night_time = datetime(2024, 1, 1, 23, 0, 0)
        self.assertEqual(oche.OCHE.get_salutation(night_time), 'Bonne nuit')
        
        late_night = datetime(2024, 1, 1, 2, 0, 0)
        self.assertEqual(oche.OCHE.get_salutation(late_night), 'Bonne nuit')
        
        early_night = datetime(2024, 1, 1, 22, 0, 0)
        self.assertEqual(oche.OCHE.get_salutation(early_night), 'Bonne nuit')
    
    def test_boundary_times(self):
        """Test des heures limites"""
        # Limite matin/après-midi
        self.assertEqual(oche.OCHE.get_salutation(datetime(2024, 1, 1, 11, 59, 59)), 'Bonjour')
        self.assertEqual(oche.OCHE.get_salutation(datetime(2024, 1, 1, 12, 0, 0)), 'Bon après-midi')
        
        # Limite après-midi/soir
        self.assertEqual(oche.OCHE.get_salutation(datetime(2024, 1, 1, 17, 59, 59)), 'Bon après-midi')
        self.assertEqual(oche.OCHE.get_salutation(datetime(2024, 1, 1, 18, 0, 0)), 'Bonsoir')
        
        # Limite soir/nuit
        self.assertEqual(oche.OCHE.get_salutation(datetime(2024, 1, 1, 21, 59, 59)), 'Bonsoir')
        self.assertEqual(oche.OCHE.get_salutation(datetime(2024, 1, 1, 22, 0, 0)), 'Bonne nuit')
    
    def test_current_time(self):
        """Test avec l'heure actuelle (sans paramètre)"""
        result = oche.OCHE.get_salutation()
        self.assertIn(result, ['Bonjour', 'Bon après-midi', 'Bonsoir', 'Bonne nuit'])


class TestAnalyzeText(unittest.TestCase):
    """Tests pour la fonction oche.OCHE.analyze_text"""
    
    def test_palindrome_morning(self):
        """Test palindrome le matin"""
        morning_time = datetime(2024, 1, 1, 9, 0, 0)
        result = oche.OCHE.analyze_text('radar', morning_time)
        
        self.assertEqual(result['salutation'], 'Bonjour')
        self.assertEqual(result['text'], 'radar')
        self.assertTrue(result['is_palindrome'])
        self.assertIn('Bonjour', result['message'])
        self.assertIn('est un palindrome', result['message'])
    
    def test_non_palindrome_evening(self):
        """Test non-palindrome le soir"""
        evening_time = datetime(2024, 1, 1, 20, 0, 0)
        result = oche.OCHE.analyze_text('hello', evening_time)
        
        self.assertEqual(result['salutation'], 'Bonsoir')
        self.assertEqual(result['text'], 'hello')
        self.assertFalse(result['is_palindrome'])
        self.assertIn('Bonsoir', result['message'])
        self.assertIn('n\'est pas un palindrome', result['message'])
    
    def test_analyze_with_current_time(self):
        """Test analyse avec l'heure actuelle"""
        result = oche.OCHE.analyze_text('kayak')
        
        self.assertEqual(result['text'], 'kayak')
        self.assertTrue(result['is_palindrome'])
        self.assertIn('salutation', result)
        self.assertIn('message', result)
    
    def test_complex_palindrome_afternoon(self):
        """Test palindrome complexe l'après-midi"""
        afternoon_time = datetime(2024, 1, 1, 15, 0, 0)
        result = oche.OCHE.analyze_text('A man a plan a canal Panama', afternoon_time)
        
        self.assertEqual(result['salutation'], 'Bon après-midi')
        self.assertTrue(result['is_palindrome'])
        self.assertIn('Bon après-midi', result['message'])
        self.assertIn('est un palindrome', result['message'])


class TestEdgeCases(unittest.TestCase):
    """Tests des cas limites"""
    
    def test_long_palindrome(self):
        """Test avec un palindrome très long"""
        long_palindrome = 'a' * 1000 + 'b' + 'a' * 1000
        self.assertTrue(oche.OCHE.is_palindrome(long_palindrome))
    
    def test_special_characters(self):
        """Test avec des caractères spéciaux"""
        self.assertTrue(oche.OCHE.is_palindrome('A!B@B#A'))
        self.assertTrue(oche.OCHE.is_palindrome('12@#@21'))
    
    def test_unicode_characters(self):
        """Test avec des caractères Unicode"""
        self.assertTrue(oche.OCHE.is_palindrome('café éfac'))
        self.assertTrue(oche.OCHE.is_palindrome('été'))
    
    def test_whitespace_only(self):
        """Test avec seulement des espaces"""
        self.assertTrue(oche.OCHE.is_palindrome('   '))
        self.assertTrue(oche.OCHE.is_palindrome('\t\n\r'))


def run_custom_tests():
    """Exécute les tests avec un affichage personnalisé"""
    print("🧪 Exécution des tests Python...\n")
    
    # Découverte et exécution des tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(__import__(__name__))
    
    # Runner personnalisé pour un affichage plus joli
    runner = unittest.TextTestRunner(verbosity=2, stream=None)
    result = runner.run(suite)
    
    # Affichage des résultats
    print(f"\n📊 Résultats:")
    print(f"   ✅ Tests réussis: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"   ❌ Tests échoués: {len(result.failures)}")
    print(f"   💥 Erreurs: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ Échecs:")
        for test, error in result.failures:
            print(f"   - {test}: {error}")
    
    if result.errors:
        print("\n💥 Erreurs:")
        for test, error in result.errors:
            print(f"   - {test}: {error}")
    
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun) * 100
    print(f"\n📈 Taux de réussite: {success_rate:.1f}%")


if __name__ == '__main__':
    run_custom_tests()