from abc import ABC, abstractmethod

class Parser:
    @abstractmethod
    def parse(self, raw_data):
        pass