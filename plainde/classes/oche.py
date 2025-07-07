"""
Module contenant les fonctions pour vérifier les palindromes et générer des salutations
"""

import re
from datetime import datetime
from typing import Dict, Union

class OCHE : 

    def is_palindrome(text: str) -> bool:
        """
        Vérifie si un mot ou une phrase est un palindrome
        
        Args:
            text (str): Le texte à vérifier
            
        Returns:
            bool: True si c'est un palindrome, False sinon
        """
        if not isinstance(text, str):
            return False
        
        # Nettoie le texte : enlève les espaces, la ponctuation et met en minuscules
        clean_text = re.sub(r'[^a-z0-9]', '', text.lower())
        
        # Compare avec sa version inversée
        return clean_text == clean_text[::-1]


    def get_salutation(date: datetime = None) -> str:
        """
        Retourne une salutation appropriée selon l'heure
        
        Args:
            date (datetime, optional): L'objet datetime (utilise l'heure actuelle si non fourni)
            
        Returns:
            str: La salutation appropriée
        """
        if date is None:
            date = datetime.now()
        
        hour = date.hour
        
        if 5 <= hour < 12:
            return "Bonjour"  # Matin (5h-12h)
        elif 12 <= hour < 18:
            return "Bon après-midi"  # Après-midi (12h-18h)
        elif 18 <= hour < 22:
            return "Bonsoir"  # Soir (18h-22h)
        else:
            return "Bonne nuit"  # Nuit (22h-5h)


    def analyze_text(text: str, date: datetime = None) -> Dict[str, Union[str, bool]]:
        """
        Fonction utilitaire pour combiner palindrome et salutation
        
        Args:
            text (str): Le texte à vérifier
            date (datetime, optional): L'heure (utilise l'heure actuelle si non fourni)
            
        Returns:
            dict: Dictionnaire avec salutation et résultat palindrome
        """
        if date is None:
            date = datetime.now()
        
        salutation = OCHE.get_salutation(date)
        is_palindrome_result = OCHE.is_palindrome(text)
        
        return {
            'salutation': salutation,
            'text': text,
            'is_palindrome': is_palindrome_result,
            'message': f'{salutation} ! "{text}" {"est" if is_palindrome_result else "n\'est pas"} un palindrome.'
        }

