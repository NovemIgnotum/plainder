import datetime

def palinder():
    heure = datetime.datetime.now().hour
    if 5 <= heure < 18:
        salutation = "Bonjour"
    else:
        salutation = "Bonsoir"
    texte = input(f"{salutation}, écrivez quelque chose : ")
    if texte == texte[::-1]:
        print(f"Bien dit ! \n{texte} est un palindrome \n\nAu revoir !")
    else:
        print(f"{texte}\n\nAu revoir !")

if __name__ == "__main__":
    try:
        palinder()
    except KeyboardInterrupt:
        print("\nAu revoir !")