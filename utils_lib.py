print = {
    "HEADER":'\033[95m',
    "BLUE":'\033[94m',
    "CYAN":'\033[96m',
    "GREEN":'\033[92m',
    "YELLOW":'\033[93m',
    "RED":'\033[91m',
    "CLEAR":'\033[0m',
    "BOLD":'\033[1m',
    "UNDERLINE":'\033[4m'
}


import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Process a given file with an optional unsafe mode flag.")

# Add the --unsafe optional flag
# action='store_true' means, if the --unsafe flag is used, set the variable to True. Default is False.
parser.add_argument("--unsafe", action="store_true",
                    help="Enable unsafe operations.")

# Add the filename argument
# nargs=1 makes it a list of 1 item. If you want it to be a string instead of a list, remove nargs.
parser.add_argument("filename", metavar="FILENAME", type=str,
                    help="The filename to process.")

# Execute the parse_args() method
args = parser.parse_args()

# Extract the filename and store it in the variable 'fname'
fname = args.filename

# Access the unsafe flag value
unsafe_mode = args.unsafe

# Just for demonstration, print the values
print(f"Filename: {fname}")
print(f"Unsafe mode: {'Enabled' if unsafe_mode else 'Disabled'}")


