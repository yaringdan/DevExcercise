from Readers.csv_db_reader import CSVDBReader
import ipaddress
import bisect

class CSVCountryIPV4Reader(CSVDBReader):
    def __init__(self, file_path):
        self.file_path = file_path
        self.network_data = []
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
        self.network_data.sort(key=lambda x: x[0].network_address)
    
    def get_id_by_ip(self, ip_str):
        try:
            target_ip = ipaddress.ip_address(ip_str)
            idx = bisect.bisect_right(self.network_data, target_ip, key=lambda x: x[0].network_address) - 1
            if idx >= 0:
                network, geoname_id = self.network_data[idx]
                if target_ip in network:
                    return geoname_id
        except ValueError:
            pass
        return None