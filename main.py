from Readers.log_reader import LogReader
from Readers.csv_country_ipv4_reader import CSVCountryIPV4Reader
from Readers.csv_country_locations_reader import CSVCountryLocationsReader
from Parsers.apache_parser import ApacheParser
from Aggregators.aggregator import Aggregator
from Formatters.terminal_formatter import TerminalFormatter
import sys

COUNTRY_IPV4_CSV_PATH = "GeoLite2-Country-Blocks-IPv4.csv"
COUNTRY_LOCATIONS_CSV_PATH = "GeoLite2-Country-Locations-en.csv"

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path>")
        return

    log_file_path = sys.argv[1]
    print(f"Analyzing file: {log_file_path}...\n")
    csv_country_ipv4_reader = CSVCountryIPV4Reader(COUNTRY_IPV4_CSV_PATH)
    csv_country_locations_reader = CSVCountryLocationsReader(COUNTRY_LOCATIONS_CSV_PATH)
    reader = LogReader()
    apache_parser = ApacheParser(csv_country_ipv4_reader, csv_country_locations_reader)
    aggregator = Aggregator()
    terminal_formatter = TerminalFormatter()

    log_lines = reader.read(log_file_path)
    parsed_data = apache_parser.parse(log_lines)
    stats, total = aggregator.aggregate(parsed_data)
    print(terminal_formatter.format(stats, total))

if __name__ == "__main__":
    main()