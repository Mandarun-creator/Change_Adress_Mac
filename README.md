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

Cet outil est spécialement utile pour les testeurs en cybersécurité, les administrateurs système ou les utilisateurs cherchant à masquer leur adresse MAC pour des raisons de confidentialité ou de test.

---

## Fonctionnalités

- **Afficher les interfaces réseau disponibles** : Liste toutes les interfaces réseau avec leurs adresses MAC actuelles.
- **Changer l'adresse MAC** : Permet de changer l'adresse MAC d'une ou plusieurs interfaces réseau.
- **Support multi-interface** : Changer l'adresse MAC de plusieurs interfaces en une seule commande.

---

## Prérequis

Avant de commencer, assurez-vous que les éléments suivants sont installés :

- **Python 3.x** (vérifiez avec `python3 --version`)
- **psutil 6.0.0** (le script gère les interfaces réseau via cette bibliothèque)

---

## Installation

Suivez ces étapes pour installer et utiliser **ChangeAddressMac** sur un système Linux (comme Kali Linux) :

1. **Cloner le dépôt GitHub** :
   
   ```bash
   git clone https://github.com/USERNAME/ChangeAddressMac.git
2. **Naviguer dans le répertoire du projet** :
   ```bash
   cd ChangeAddressMac
3. **Installer les dépendances Python** :
   Installez les dépendances nécessaires à l'aide de pip
   ```bash
   pip install -r requirements.txt
4. **Rendre le script exécutable** :
   ```bash
   chmod +x changeadressmac.py
5. **Déplacement du script** :
   (Optionnel) Déplacer le script dans /usr/local/bin pour l'utiliser depuis n'importe où
   ```bash
   sudo mv changeadressmac.py /usr/local/bin/changeadressmac

## Utilisation
**Afficher les interfaces réseau** :

Pour afficher toutes les interfaces réseau disponibles avec leurs adresses MAC, exécutez la commande suivante :
```bash
changeadressmac -I

Pour afficher une interface réseau spécifique avec son adresse MAC, utilisez :
```bash
changeadressmac -I nom de l'interface

**Changer l'adresse MAC** :

