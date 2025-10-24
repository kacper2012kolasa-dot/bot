from random import randint as rnum
import random

def monet():
    å = rnum(1, 2)
    if å == 1:
        return  "orzeł"
    else:
        return "reszka"

def monet_sv():
    ö = rnum(1, 2)
    if ö == 1:
        return  "Krona"
    else:
        return "Klave"


def losuj_liczbe(liczba: int) -> int:
    """Losuje liczbę z zakresu od 1 do podanej liczby."""
    return random.randint(1, liczba)

def generuj_haslo(dlugosc: int) -> str:
    """Generuje bezpieczne hasło o podanej długości."""
    znaki = (
        "abcdefghijklmnopqrstuvwxyz"  # małe litery
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # duże litery
        "0123456789"                  # cyfry
        "!@#$%^&*()-_=+[]{}|;:,.<>?/"  # znaki specjalne
    )
    
    haslo = ''
    for _ in range(dlugosc):
        haslo += random.choice(znaki)
    return haslo