from abc import ABC, abstractmethod

class Reader:
    @abstractmethod
    def read(self, file):
        pass
    