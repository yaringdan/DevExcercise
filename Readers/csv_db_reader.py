from reader import Reader
import csv

class CSVDBReader(Reader):
    def read(self, file_path):
        try:
            with open(file_path, mode='r') as f:
                reader = csv.DictReader(f)
                
                return reader
                    
        except FileNotFoundError:
            print("File not found.")