from Readers.log_reader import read
from Readers.db_reader import read
from Parsers.apache_parser import parse
from Analyzers.analyzer import analyze
from Formatters.terminal_format import output_format

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path>")
        return

    log_file = sys.argv[1]
    print(f"Analyzing file: {log_file}...\n")


if __name__ == "__main__":
    main()