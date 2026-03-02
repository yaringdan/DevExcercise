from abc import ABC, abstractmethod

class Formatter:
    @abstractmethod
    def format(self, output):
        pass
    