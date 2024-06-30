import argparse
import os


def handle_c_command(date):
    print(f"Executing 'c' command with date: {date}")


def handle_a_command(date):
    print(f"Executing 'a' command with date: {date}")


def handle_e_command(year):
    print(f"Executing 'e' command with year: {year}")


def handle_files_dir(files_dir):
    print(f"Executing 'files-dir' command with path: {files_dir}")


def main():
    parser = argparse.ArgumentParser(description="Weather data processing script")
    parser.add_argument("files_dir", help="Path to the files directory")
    parser.add_argument(
        "-c",
        "--c-command",
        dest="c_date",
        help='Execute the "c" command with the given date (YYYY/MM)',
    )
    parser.add_argument(
        "-a",
        "--a-command",
        dest="a_date",
        help='Execute the "a" command with the given date (YYYY/M)',
    )
    parser.add_argument(
        "-e",
        "--e-command",
        dest="e_year",
        help='Execute the "e" command with the given year (YYYY)',
    )

    args = parser.parse_args()

    # Check if the files directory exists
    if not os.path.isdir(args.files_dir):
        print(f"Error: '{args.files_dir}' is not a valid directory.")
        parser.print_usage()
        return

    # Call the relevant functions based on the provided arguments
    if args.c_date:
        handle_c_command(args.c_date)
    if args.a_date:
        handle_a_command(args.a_date)
    if args.e_year:
        handle_e_command(args.e_year)
    handle_files_dir(args.files_dir)


if __name__ == "__main__":
    main()
