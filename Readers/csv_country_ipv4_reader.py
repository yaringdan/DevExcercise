from reader import CSVDBReader
import ipaddress

class CSVCountryIPV4Reader(CSVDBReader):
    def __init__(self):
        self.network_data = []
        
    def read(self, file_path):
        self.file_path = file_path
        reader = super().read(self.file_path)
        network_list = []

        for row in reader:
            try:
                net_obj = ipaddress.ip_network(row['network'])
                network_list.append((net_obj, row['geoname_id']))
            except (ValueError, KeyError):
                continue
        
        return network_list
    
    