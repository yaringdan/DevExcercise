class Aggregator:
    def aggregate(self, parsed_data):
        if not parsed_data: return {}, 0
        
        total = len(parsed_data)
        stats = {field: {} for field in parsed_data[0].keys()}

        for entry in parsed_data:
            for field, value in entry.items():
                stats[field][value] = stats[field].get(value, 0) + 1
        
        return stats, total