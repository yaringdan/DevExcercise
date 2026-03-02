from abc import ABC, abstractmethod

class Reader:
    @abstractmethod
    def read_log(self, file_path):
        pass
    