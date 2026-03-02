from Readers.log_reader import LogReader
from Parsers.apache_parser import ApacheParser
from Analyzers.analyzer import Analyzer
from Formatters.terminal_format import TerminalFormatter
import sys

COUNTRY_IPV4_CSV_PATH = "GeoLite2-Country-Blocks-IPv4.csv"
COUNTRY_LOCATIONS_CSV_PATH = "GeoLite2-Country-Locations-en.csv"

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path>")
        return

    log_file_path = sys.argv[1]
    print(f"Analyzing file: {log_file_path}...\n")
    log_lines = LogReader.read(log_file_path)
    parsed_data = ApacheParser.parse(log_lines)
    analyzed_data = analyze(parsed_data)
    output_format()

if __name__ == "__main__":
    main()