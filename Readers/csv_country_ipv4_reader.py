from reader import CSVDBReader
import ipaddress

class CSVCountryIPV4Reader(CSVDBReader):
    def __init__(self, file_path):
        self.file_path = file_path
        self.networks = []
        self.load_data()
        
    def load_data(self):
        reader = self.read(self.file_path)
        if reader:
            for row in reader:
                try:
                    net_obj = ipaddress.ip_network(row['network'])
                    self.network_data.append((net_obj, row['geoname_id']))
                except (ValueError, KeyError):
                    continue
    
    def get_id_by_ip(self, ip_str):
        try:
            target_ip = ipaddress.ip_address(ip_str)
            for network, geoname_id in self.network_data:
                if target_ip in network:
                    return geoname_id
        except ValueError:
            pass
        return None