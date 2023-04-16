# TP_Ransomware

## Chiffrement

### Question 1

Cet algorithme de chiffrement s'appelle un XOR Cypher ou (Xor encryption). C'est un inverseur sur commande. Il n'est pas robuste parce qu'il est possible de le brut force. Il ne fournit pas d'authentification donc il ne vérifie pas si les données ont été modifiées.

### Question 2 : 

Si on hashait directement le sel et la clef, il serait possible d'avoir des collisions. De plus, la fonction de hashage n'étant pas prévu pour être robuste, des attaquants pourraient retrouver la clé par brut force. Le HMAC permet d'authentifier les données et de vérifier si elles ont été modifiées. Cependant, ce n'est pas une fonction de dérivation de clé. En utilisant la fonction PBKDF2HMAC, on peut créer une clé sécurisée avec le salt et beaucoup d'itérations. Cela permet de rendre le brut force beaucoup plus difficile. 

### Question 3 :

Il est préférable de vérifier qu’un fichier token.bin n’est pas déjà présent pour éviter d’écraser un token existant. Si ce dernier est écrasé, cela pourrait entraîner des problèmes de sécurité et d’authentification. C'est pourquoi il est important de vérifier l’existence du token.bin avant de le créer.

### Question 4 :

Pour vérifier si la clé candidate est la bonne, on peut dériver une clé à partir du sel et de la clé candidate. Ensuite, on compare cette clé dérivée avec le token stocké dans le self._token. Si les deux valeurs sont égales, cela signifie que la clé candidate est valide.