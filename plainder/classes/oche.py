class OCHE :
    
    def palindrome(self, input : str) -> bool:
        # Renvoie True si la chaine de caractères est un palindrome
        return input == input[::-1]