from reader import Reader

class LogReader(Reader):
    @staticmethod
    def read(self, file_path):
        lines = []
        try:
            with open(file_path, 'r') as log_file:
                for line in log_file:
                    line = line.strip()
                    if not line:
                        continue
                    lines.append(line)
            return lines
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")