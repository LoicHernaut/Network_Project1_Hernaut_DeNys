import pyshark

def count_dns_queries(pcap_file):
    dns_queries = {}

    # Ouvrir le fichier pcapng
    capture = pyshark.FileCapture(pcap_file)

    # Parcourir tous les paquets DNS
    for packet in capture:
        if 'DNS' in packet:
            dns = packet['DNS']
            if dns.qry_name:
                domain = dns.qry_name.lower()  # Convertir en minuscules pour éviter les doublons
                if domain in dns_queries:
                    dns_queries[domain] += 1
                else:
                    dns_queries[domain] = 1

    # Fermer le fichier pcapng
    capture.close()

    return dns_queries

if __name__ == "__main__":
    # Chemin vers le fichier pcapng
    pcap_file = 'google_drive_capture_1.pcapng'

    # Compter les requêtes DNS dans le fichier pcapng
    dns_queries = count_dns_queries(pcap_file)

    # Afficher les résultats
    print("Nombre d'occurrences de chaque nom de domaine pour toutes les requêtes DNS :")
    for domain, count in dns_queries.items():
        print(f"{domain}: {count}")
