from reader import CSVDBReader

class CSVCountryIPV4Reader(CSVDBReader):
    def read(self, file_path):
        reader = super().read(file_path)