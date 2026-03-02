from parser import Parser
from ua_parser import user_agent_parser

class ApacheParser(Parser):
    def __init__(self, country_ipv4_reader, country_locations_reader):
        self.country_ipv4_reader = country_ipv4_reader
        self.country_locations_reader = country_locations_reader
        self.dimensions_dict = {
            "Country": self.parse_country,
            "OS": self.parse_os,
            "Browser": self.parse_browser
        }

    def parse(self, raw_data):
        results = []
        for line in raw_data:
            if not line.strip():
                continue
            
            parts = line.split(' ', 1)
            ip = parts[0]
            ua_string = parts[1].strip('"') if len(parts) > 1 else ""
            
            parsed_ua = user_agent_parser.Parse(ua_string)

            entry = {field: func(ip, parsed_ua) for field, func in self.dimensions_dict.items()}
            results.append(entry)
        return results
    
    def parse_country(self, ip, parsed_ua):
        geo_id = self.network_reader.find_id_by_ip(ip)
        return self.location_reader.get_country_name(geo_id) if geo_id else "Unknown"

    def parse_os(self, ip, parsed_ua):
        return parsed_ua.get('os', {}).get('family', 'Unknown')

    def parse_browser(self, ip, parsed_ua):
        return parsed_ua.get('user_agent', {}).get('family', 'Unknown')