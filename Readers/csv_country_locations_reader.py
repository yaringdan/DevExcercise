from Readers.csv_db_reader import CSVDBReader

class CSVCountryLocationsReader(CSVDBReader):
    def __init__(self, file_path):
        self.file_path = file_path
        self.id_to_country = {}
        self.load_data()

    def load_data(self):
        reader = self.read(self.file_path)
        if reader:
            for row in reader:
                geo_id = row.get('geoname_id')
                country = row.get('country_name')
                if geo_id and country:
                    self.id_to_country[geo_id] = country

    def get_country_name(self, geo_id):
        return self.id_to_country.get(geo_id, "Other")