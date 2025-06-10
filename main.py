import datetime

# Dictionnaire complet avec ponctuation
galactic_map = {
    'a': 'ᔑ', 'b': 'ʖ', 'c': 'ᓵ', 'd': '↸', 'e': 'ᒷ', 
    'f': '⎓', 'g': '⊣', 'h': '⍑', 'i': '╎', 'j': '⋮', 
    'k': 'ꖌ', 'l': 'ꖎ', 'm': 'ᒲ', 'n': 'リ', 'o': '𝙹', 
    'p': '!', 'q': 'ᑑ', 'r': '∷', 's': 'ᓭ', 't': 'ℸ', 
    'u': '⚍', 'v': '⍊', 'w': '∴', 'x': '̇/', 'y': '||', 'z': '⨅',
    ' ': ' ', '!': '¡', '?': '¿', ',': "'", '.': '˙',
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
    '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'
}

def to_galactic(text):
    """Convertit tout le texte en alphabet galactique"""
    return ''.join([galactic_map.get(c.lower(), c) for c in text])

def get_greeting():
    """Retourne la salutation appropriée en galactique"""
    heure = datetime.datetime.now().hour
    return to_galactic("Bonjour" if 5 <= heure < 18 else "Bonsoir")

def main():
    try:
        # Salutation galactique
        greeting = get_greeting()
        user_input = input(f"{greeting}, ᓭ╎ᒲᒷ ! ╎ꖎ ᔑ∷ℸ¡ ∴╎ꖎꖎ ||𝙹⚍ ℸ ̣ ⍑ᒷリ ᓭ𝙹ᒲᒷℸ ̣ ⍑ℸ ̣ ᓭℸ ̣ : ")
        
        # Vérification palindrome
        if user_input.lower() == user_input.lower()[::-1]:
            msg = to_galactic(f"\nBien dit !\n{user_input} ∴╎ꖎꖎ ℸ ̣ ⍑ᒷ ᔑ !¡ꖎℸ ̣ ⍑ᒷリℸ ̣ ᓭℸ ̣ \n\n⍑ᔑ⨅ᒷ ∴╎ꖎꖎ ℸ ̣ ⍑ᒷ !")
        else:
            msg = to_galactic(f"\n{user_input}\n\n⍑ᔑ⨅ᒷ ∴╎ꖎꖎ ℸ ̣ ⍑ᒷ !")
        
        print(msg)
        
    except KeyboardInterrupt:
        print(to_galactic("\n⍑ᔑ⨅ᒷ ∴╎ꖎꖎ ℸ ̣ ⍑ᒷ !"))

if __name__ == "__main__":
    main()