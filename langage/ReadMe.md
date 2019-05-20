# Playoff Python Langage

## Scenario 

Tu ressors de cette réunion avec ton client qui c'est bien passé. Il t'a donné 
une série de fichiers de calculs non standard dont il souhaite avoir les 
résultats pour les intégrer en prod, sans avoir à systématiquement les calculer
à la main.
Tu as une heure de train devant toi pour rentrer au bureau, pourquoi ne pas lui
faire une moulinette qui fait le travail automatiquement ? 

### Inputs

L'ensemble des fichiers de calculs que le client t'a donné en exemple sont dans 
le dossier `./input`. 

Attention, il t'a prévenu que ces fichiers peuvent contenir des erreurs de 
syntax ou même fonctionnel, ne prend rien pour acquis !

### Règles fonctionnelles

* Une ligne par calcul (format `Operand Operator Operand`)
* Un opérande peut être soit :
	* un nombre (entier ou décimal) avec le format `Number(XX)`
	* une heure avec le format `Time(XXhYYm)`
* Les opérations attendues sont : 
	* `+` l'addition (nombre/nombre, temps/temps)
	* `-` la soustraction (nombre/nombre, temps/temps)
	* `*` la multiplication (nombre/nombre, temps/nombre)
	* `/` la division (nombre/nombre, temps/nombre)
* La sortie doit être de la forme : 
```
Nom_du_fichier_en_entree:
	* Operande Operator Operande = Resultat
	* Operande Operator Operande : Erreur (si la ligne est en erreur)
	* Operande Operator Operande = Resultat
```
