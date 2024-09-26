
# ChangeAddressMac

**ChangeAddressMac** est un outil en ligne de commande en Python conçu pour afficher et changer l'adresse MAC des interfaces réseau sur les systèmes Linux, en particulier sur Kali Linux.

## Sommaire
- [Description](#description)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
    - [Afficher les interfaces réseau](#afficher-les-interfaces-réseau)
    - [Changer l'adresse MAC](#changer-ladresse-mac)
- [Exemples](#exemples)
- [Tests](#tests)
- [Contribution](#contribution)
- [Licence](#licence)
- [Auteur](#auteur)

---

## Description

**ChangeAddressMac** est un script Python simple et efficace qui permet aux utilisateurs d'afficher toutes les interfaces réseau disponibles avec leurs adresses MAC, ainsi que de changer l'adresse MAC d'une ou plusieurs interfaces.

Cet outil est particulièrement utile pour les testeurs en cybersécurité, les administrateurs système ou les utilisateurs cherchant à masquer leur adresse MAC pour des raisons de confidentialité ou de test.

---

## Fonctionnalités

- **Afficher les interfaces réseau disponibles** : Liste toutes les interfaces réseau avec leurs adresses MAC actuelles.
- **Changer l'adresse MAC** : Permet de changer l'adresse MAC d'une ou plusieurs interfaces réseau.
- **Support multi-interface** : Changer l'adresse MAC de plusieurs interfaces en une seule commande.

---

## Prérequis

Avant de commencer, assurez-vous que les éléments suivants sont installés :

- **Python 3.x** (vérifiez avec `python3 --version`)
- **psutil 6.0.0** (le script utilise cette bibliothèque pour gérer les interfaces réseau)

---

## Installation

Suivez ces étapes pour installer et utiliser **ChangeAddressMac** sur un système Linux (comme Kali Linux) :

1. **Cloner le dépôt GitHub** :
   
   ```bash
   https://github.com/Mandarun-creator/Change_Adress_Mac.git
   ```

2. **Naviguer dans le répertoire du projet** :
   
   ```bash
   cd ChangeAddressMac
   ```

3. **Installer les dépendances Python** :

   Installez les dépendances nécessaires à l'aide de `pip` :
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Rendre le script exécutable** :
   
   ```bash
   chmod +x changeadressmac.py
   ```

5. **Déplacer le script** (optionnel) :

   Déplacez le script dans `/usr/local/bin` pour l'utiliser depuis n'importe où :
   
   ```bash
   sudo mv changeadressmac.py /usr/local/bin/changeadressmac
   ```

---

## Utilisation

### Afficher les interfaces réseau

Pour afficher toutes les interfaces réseau disponibles avec leurs adresses MAC, exécutez la commande suivante :

```bash
changeadressmac -I
```

Pour afficher une interface réseau spécifique avec son adresse MAC, utilisez :

```bash
changeadressmac -I <nom de l'interface>
```

### Changer l'adresse MAC

Pour changer l'adresse MAC d'une interface réseau, utilisez la commande suivante :

```bash
changeadressmac -L <nom de l'interface> <nouvelle adresse MAC>
```

Vous pouvez également changer l'adresse MAC de plusieurs interfaces en une seule commande :

```bash
changeadressmac -L <interface1> <nouvelle MAC1> <interface2> <nouvelle MAC2> ...
```

---

## Exemples

### Exemple 1 : Afficher toutes les interfaces réseau

```bash
$ changeadressmac -I
```

### Exemple 2 : Changer l'adresse MAC de l'interface `eth0`

```bash
$ changeadressmac -L eth0 00:11:22:33:44:57
```

### Exemple 3 : Changer l'adresse MAC de plusieurs interfaces

```bash
$ changeadressmac -L eth0 00:11:22:33:44:57 wlan0 66:77:88:99:AA:BB
```

---

## Tests

Pour exécuter les tests unitaires et vérifier le bon fonctionnement du script, exécutez la commande suivante dans le répertoire du projet :

```bash
python -m unittest discover tests
```

---

## Contribution

Vous souhaitez contribuer à **ChangeAddressMac** ? Voici comment vous pouvez le faire :

1. **Fork** ce projet sur GitHub.
2. Créez une nouvelle branche pour vos modifications :
   
   ```bash
   git checkout -b ma-nouvelle-fonctionnalité
   ```

3. Faites vos modifications et effectuez un commit :
   
   ```bash
   git commit -m "Ajout de ma nouvelle fonctionnalité"
   ```

4. Poussez vos modifications vers votre fork :
   
   ```bash
   git push origin ma-nouvelle-fonctionnalité
   ```

5. Ouvrez une **Pull Request** sur le dépôt original.

---

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

---

## Auteur

Développé par **Gracia Mboma**, passionné de cybersécurité et de développement Python.
