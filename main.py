import random
from colorama import Fore, Style
import sys
import pyfiglet

from charactaire import Charactaire

char = Charactaire()


def init_msg():
    ASCII_art_1 = pyfiglet.figlet_format("HermesCodeLoc", font='slant')
    print(Fore.RED, ASCII_art_1)
    menu()


def menu():
    g = True
    while g:
        global choice
        print(" 1: facile  (charactaire minuscule uniquement\n",
              "2: normale (charactaire minuscule et majuscule avec des chifre\n",
              "3: robuste (charactaire minuscule et majuscule spéciale avec des chifre)\n")
        try:
            choice = int(input("Qu'elle et votre choix : "))
        except ValueError:
            print("\nERREUR : les chifre sont uniquement autoriser \n")
            menu()

        if choice == 1:
            g = False
            generate_password(1)
        else:
            if choice == 2:
                g = False
                generate_password(2)
            else:
                if choice == 3:
                    g = False
                    generate_password(3)
                else:
                    g = False
                    print("ERREUR : choix inconue \n")
                    menu()


def generate_password(c):
    nbr_char = int(input("Combient de charactaire vouler vous dans votre mots de passe : "))
    _pass = ""
    for i in range(nbr_char):
        if c == 1:
            _pass += random.choice(char.ltr)
        if c == 2:
            _pass += random.choice(char.ltr + char.majLtr + char.nbr)
        if c == 3:
            _pass += random.choice(char.ltr + char.majLtr + char.nbr + char.special_ltr + char.special_ltr)

    print("Voici votre mots de pass =>", _pass)
    restart()


def restart():
    global _restart
    i = True
    while i:
        try:
            _restart = str(input("Souhaiter vous generer un nouveux mots de pass. Y/N : "))
            i = False
        except ValueError:
            print("Velier repondre par Y si oui ou par N si non")

    f = True
    while f:
        if _restart == str("Y") or _restart == str("y"):
            f = False
            init_msg()
        else:
            if _restart == str("N") or _restart == str("n"):
                f = False
                sys.exit()
            else:
                f = False
                print("ERREUR choix inconue")
                restart()


if __name__ == "__main__":
    init_msg()
