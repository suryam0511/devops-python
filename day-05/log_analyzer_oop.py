class LogAnalyzer:
    """
    A simple log analyzer class to count log levels.
    """

    def __init__(self, log_file, output_file):
        """
        Initialize file paths and counters.
        """
        self.log_file = log_file
        self.output_file = output_file
        self.log_levels = ["INFO", "WARNING", "ERROR"]
        self.counts = {level: 0 for level in self.log_levels}

    def read_and_analyze_logs(self):
        """
        Read the log file and count log levels.
        """
        try:
            with open(self.log_file, "r") as file:
                lines = file.readlines()

                if not lines:
                    raise ValueError("Log file is empty.")

                for line in lines:
                    for level in self.log_levels:
                        if level in line:
                            self.counts[level] += 1

        except FileNotFoundError:
            print(f"Error: File '{self.log_file}' not found.")
            return False
        except ValueError as error:
            print(f"Error: {error}")
            return False

        return True

    def print_summary(self):
        """
        Print log summary to terminal.
        """
        print("Log Analysis Summary:")
        for level, count in self.counts.items():
            print(f"{level}: {count}")

    def write_summary_to_file(self):
        """
        Write log summary to output file.
        """
        with open(self.output_file, "w") as file:
            for level, count in self.counts.items():
                file.write(f"{level}: {count}\n")


def main():
    analyzer = LogAnalyzer("app.log", "log_summary.txt")

    if analyzer.read_and_analyze_logs():
        analyzer.print_summary()
        analyzer.write_summary_to_file()
        print("\nSummary written to 'log_summary.txt'")


if __name__ == "__main__":
    main()
