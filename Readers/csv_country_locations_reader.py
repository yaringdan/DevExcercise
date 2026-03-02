from reader import CSVDBReader

class CSVCountryLocationsReader(CSVDBReader):
    def read(self, file_path):
        reader = super().read(file_path)