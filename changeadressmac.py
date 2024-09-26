#!/usr/bin/env python3

import argparse
import sys
import psutil
import subprocess

def get_mac_address(interfaces=None):
    """
    Récupère les adresses MAC pour une ou plusieurs interfaces réseau.

    :param interfaces: Une interface réseau spécifique ou une liste d'interfaces (par défaut, toutes les interfaces)
    :return: Un dictionnaire {interface: adresse MAC}
    """
    all_interfaces = psutil.net_if_addrs()
    mac_addresses = {}

    if isinstance(interfaces, str):
        interfaces = [interfaces]

    if interfaces is None:
        interfaces = all_interfaces.keys()

    for interface in interfaces:
        if interface in all_interfaces:
            for addr_info in all_interfaces[interface]:
                if addr_info.family == psutil.AF_LINK:  # AF_LINK correspond à l'adresse MAC
                    mac_addresses[interface] = addr_info.address

    return mac_addresses

def change_mac_address(interface, mac_address):
    """
    Change l'adresse MAC d'une interface réseau.
    
    :param interface: Nom de l'interface réseau (ex: eth0, wlan0, etc.)
    :param mac_address: Nouvelle adresse MAC souhaitée (ex: '00:11:22:33:44:55')
    :return: True si la modification a réussi, False sinon
    """
    try:
        result = subprocess.run(["ip", "link", "show", interface], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[+] Erreur : L'interface '{interface}' n'existe pas.")
            return False
        
        subprocess.run(["sudo", "ip", "link", "set", interface, "down"], check=True)
        subprocess.run(["sudo", "ip", "link", "set", interface, "address", mac_address], check=True)
        subprocess.run(["sudo", "ip", "link", "set", interface, "up"], check=True)

        print(f"[+] Succès : L'adresse MAC de '{interface}' a été changée en '{mac_address}'.")
        return True

    except subprocess.CalledProcessError as e:
        print(f"[+] Erreur : Impossible de changer l'adresse MAC de '{interface}' : {e}")
        return False

def print_interfaces(interface=None):
    """
    Affiche toutes les interfaces réseau disponibles avec leur adresse MAC.
    Si une interface spécifique est fournie, seule celle-ci est affichée.
    
    :param interface: (optionnel) Nom de l'interface réseau spécifique à afficher
    """
    mac_addresses = get_mac_address(interface)
    
    if not mac_addresses:
        print(f"[+] Erreur : L'interface '{interface}' n'existe pas.")
        return
    
    print("===== Interfaces réseau et adresses MAC =====")
    for iface, mac in mac_addresses.items():
        print(f"[+] Interface '{iface}' : MAC = {mac}")

def main():
    parser = argparse.ArgumentParser(
        description="Programme de gestion des adresses MAC et des interfaces réseau",
        formatter_class=argparse.RawTextHelpFormatter,
        usage="""python3 changeadressmac.py [OPTIONS]
        
        -I [interface], --interfaces [interface]   Afficher toutes les interfaces disponibles avec leur adresse MAC
                                                   Si aucune interface n'est spécifiée, toutes les interfaces sont affichées.
        -L, --change-mac                           Changer l'adresse MAC d'une ou plusieurs interfaces (utilisez des paires interface/mac)
        -h, --help                                 Afficher l'aide et quitter
        """,
    )

    parser.add_argument("-I", "--interfaces", nargs='?', const=None, help="Afficher les adresses MAC d'une interface spécifique (facultatif). Si non spécifié, toutes les interfaces sont affichées.")
    parser.add_argument("-L", "--change-mac", nargs='+', help="Changer l'adresse MAC d'une ou plusieurs interfaces. Syntaxe : -L <interface> <new_mac>")
    
    args = parser.parse_args()

    # Vérifier si aucun argument n'a été fourni
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # Afficher les interfaces disponibles avec leurs adresses MAC
    if args.interfaces is None:
        # Afficher toutes les interfaces si aucune n'est spécifiée
        print_interfaces()
    else:
        # Afficher une seule interface si spécifiée
        print_interfaces(args.interfaces)

    # Changer l'adresse MAC d'une ou plusieurs interfaces
    if args.change_mac:
        if len(args.change_mac) % 2 != 0:
            print("[+] Erreur : Chaque interface doit être suivie d'une nouvelle adresse MAC.")
            sys.exit(1)

        # Traiter les paires interface/adresse MAC
        for i in range(0, len(args.change_mac), 2):
            interface = args.change_mac[i]
            new_mac = args.change_mac[i+1]
            success = change_mac_address(interface, new_mac)
            if success:
                print(f"[+] Succès : Adresse MAC changée pour l'interface '{interface}'.")
            else:
                print(f"[+] Erreur : Échec du changement d'adresse MAC pour l'interface '{interface}'.")

if __name__ == "__main__":
    main()
