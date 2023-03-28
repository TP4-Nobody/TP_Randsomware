# TP_Ransomware

## Chiffrement

### Question 1

Cet algorithme de chiffrement s'appelle un XOR Cypher ou (Xor encryption). C'est un inverseur sur commande. Il n'est pas robuste parce qu'il est possible de le brut force. Il ne fournit pas d'authentification donc il ne vérifie pas si les données ont été modifiées.

### Question 2 : 

Si on hashait directement le sel et la clef, il serait possible d'avoir des collisions. De plus, la fonction de hashage n'étant pas prévu pour être robuste, des attaquants pourraient retrouver la clé par brut force. Le HMAC permet d'authentifier les données et de vérifier si elles ont été modifiées. Cependant, ce n'est pas une fonction de dérivation de clé. En utilisant la fonction PBKDF2HMAC, on peut créer une clé sécurisée avec le salt et beaucoup d'itérations. Cela permet de rendre le brut force beaucoup plus difficile. 

