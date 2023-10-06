import sys
import random
from time import sleep
from pystyle import Write, Colors, Colorate

def init_msg():
  banner = """
┏┓╋┏┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━━━┓╋╋╋╋┏┓╋╋╋┏┓╋╋╋╋╋╋╋╋┏┓
┃┃╋┃┃╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┏━┓┃╋╋╋╋┃┃╋╋╋┃┃╋╋╋╋╋╋╋╋┃┃
┃┗━┛┣━━┳━┳┓┏┳━━┳━━┓┃┃╋┗╋━━┳━┛┣━━┓┃┃╋╋┏━━┳━━┫┃┏┓
┃┏━┓┃┃━┫┏┫┗┛┃┃━┫━━┫┃┃╋┏┫┏┓┃┏┓┃┃━┫┃┃╋┏┫┏┓┃┏━┫┗┛┛
┃┃╋┃┃┃━┫┃┃┃┃┃┃━╋━━┃┃┗━┛┃┗┛┃┗┛┃┃━┫┃┗━┛┃┗┛┃┗━┫┏┓┓
┗┛╋┗┻━━┻┛┗┻┻┻━━┻━━┛┗━━━┻━━┻━━┻━━┛┗━━━┻━━┻━━┻┛┗┛
  """
  print(Colorate.Horizontal(Colors.blue_to_green, banner, 1))
  menu()
  
def menu():
    g = True
    while g:
        global choice
        print("1: Faible  (carctères minuscules uniquement)\n",
              "2: Normal (caractères minuscules, majuscules avec des chiffres)\n",
              "3: Robuste (carctèress minuscules, majuscules avec des chiffres)\n")
        try:
            choice = int(input("Votre choix : "))
        except ValueError:
            print("\nERREUR : Les chiffres sont uniquement autorisés \n")
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
                    print("ERREUR : Veuillez choisir une des options proposées\n")
                    menu()

def generate_password(c):
    nbr_char = int(input("\nCombien de caractères voulez-vous dans votre mot-de-passe : "))
    _pass = ""
    for i in range(nbr_char):
        if c == 1:
            _pass += random.choice(char.ltr)
        if c == 2:
            _pass += random.choice(char.ltr + char.majLtr + char.nbr)
        if c == 3:
            _pass += random.choice(char.ltr + char.majLtr + char.nbr + char.special_ltr + char.special_ltr)

    print("\nVoici votre mot-de-passe =>", _pass)
    restart()

def restart():
    global _restart
    i = True
    while i:
        try:
            _restart = str(input("\nSouhaitez-vous génerer un nouveu mot-de-passe ? Y/N : "))
            i = False
        except ValueError:
            print("\nY = Yes / N = No")

    f = True
    while f:
        if _restart == str("Y") or _restart == str("y"):
            f = False
            menu()
        else:
            if _restart == str("N") or _restart == str("n"):
                f = False
                sys.exit()
            else:
                f = False
                print("\nERREUR choix inconnu")
                restart()

class Charactaire:
  def __init__(self):
    self.nbr = "1234567890"
    self.ltr = "abcdefghijklmnopqrstuvwxyz"
    self.majLtr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    self.special_ltr = "!?,.:#@$£€&%*+=~'-_|^°µ§¨^<[(/{¤}}\)]>"
  
char = Charactaire()

if __name__ == "__main__":
    init_msg()
