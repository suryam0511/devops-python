LOG_LEVELS = ["INFO", "WARNING", "ERROR"]


def analyze_log_file(input_file):
    counts = {level: 0 for level in LOG_LEVELS}

    try:
        with open(input_file, "r") as file:
            lines = file.readlines()

            if not lines:
                raise ValueError("Log file is empty.")

            for line in lines:
                for level in LOG_LEVELS:
                    if level in line:
                        counts[level] += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return None
    except ValueError as error:
        print(f"Error: {error}")
        return None

    return counts


def write_summary(output_file, summary):
    with open(output_file, "w") as file:
        for level, count in summary.items():
            file.write(f"{level}: {count}\n")


def main():
    input_log = "app.log"
    output_file = "log_summary.txt"

    summary = analyze_log_file(input_log)

    if summary:
        print("Log Analysis Summary:")
        for level, count in summary.items():
            print(f"{level}: {count}")

        write_summary(output_file, summary)
        print(f"\nSummary written to '{output_file}'")


if __name__ == "__main__":
    main()
