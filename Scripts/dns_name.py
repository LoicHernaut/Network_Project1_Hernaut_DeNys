import pyshark

def extract_domain_names(pcap_file):
    capture = pyshark.FileCapture(pcap_file)
    domain_names = set()
    for packet in capture:
        if 'DNS' in packet:
            dns_query = packet['DNS']
            if dns_query.qry_name:
                domain_names.add(dns_query.qry_name)
    return domain_names

pcap_file = 'google_drive_capture_1.pcapng'
domains = extract_domain_names(pcap_file)
for domain in domains:
    print(domain)
