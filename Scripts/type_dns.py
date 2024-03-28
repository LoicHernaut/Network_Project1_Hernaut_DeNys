import pyshark

def count_dns_query_types(pcap_file):
    # Dictionnaire pour stocker le nombre de requêtes pour chaque type
    query_counts = {}

    # Ouvrir le fichier pcapng
    capture = pyshark.FileCapture(pcap_file)
    # Parcourir chaque paquet DNS
    for packet in capture:
        # Vérifier si le paquet est une requête DNS
        if 'dns' in packet:
            dns = packet.dns
            query_type = dns.qry_type
            # Incrémenter le compteur pour ce type de requête
            query_counts[query_type] = query_counts.get(query_type, 0) + 1

    return query_counts

# Chemin vers le fichier pcapng contenant les traces DNS
pcap_file = 'google_com_sub_set.pcapng'

# Compter le nombre de requêtes DNS pour chaque type possible
dns_query_counts = count_dns_query_types(pcap_file)

# Afficher les résultats
print("Nombre de requêtes DNS pour chaque type possible :")
for query_type, count in dns_query_counts.items():
    print(f"Type {query_type}: {count} requêtes")
