from Formatters.formatter import Formatter

class TerminalFormatter(Formatter):
    def format(self, stats, total):
        for field, counts in stats.items():
            print(f"{field.capitalize()}:")
            
            sorted_data = sorted(counts.items(), key=lambda x: x[1], reverse=True)
            
            for value, count in sorted_data:
                percentage = (count / total) * 100
                print(f"{value} {percentage:.2f}%")
            
            print()