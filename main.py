from Readers.log_reader import read_log
from Readers.db_reader import read_db
from Parsers.apache_parser import parse
from Analyzers.analyzer import analyze
from Formatters.terminal_format import output_format

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path>")
        return

    log_file_path = sys.argv[1]
    print(f"Analyzing file: {log_file_path}...\n")
    log_lines = read_log(log_file_path)
    parsed_data = parse(log_lines)
    analyzed_data = analyze(parsed_data)
    output_format()

if __name__ == "__main__":
    main()