from parser import Parser
from readers import BinaryDBReader
from readers import CSVDBReader


class ApacheParser(Parser):
    def __init__(self):
        dimensions_dict = {
            "Country": self.parse_country,
            "OS": self.parse_user_agent[0],
            "Browser": self.parse_user_agent[1]
        }
    @staticmethod
    def parse(self, raw_data):
        for line in raw_data:
            pass

    
    def parse_country():
        return
    
    def parse_user_agent():

        return ,