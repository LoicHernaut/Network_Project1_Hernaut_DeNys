from scapy.all import *

def print_ttl(pcap_file):
    # Ouvrir le fichier de capture
    packets = rdpcap(pcap_file)

    # Parcourir tous les paquets et afficher le TTL s'ils ont une couche IP
    for packet in packets:
        if IP in packet:
            ttl = packet[IP].ttl
            print(f"{ttl}")

# Appeler la fonction avec le nom du fichier de capture
print_ttl("Traces/google_com_sub_set.pcapng")
