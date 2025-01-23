import sys, os
from twofas_lib import generate_qr_codes

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <source_json_file> <destination_directory>")
        sys.exit(1)

    source_file = sys.argv[1]
    destination_dir = sys.argv[2]

    if not os.path.exists(source_file):
        print(f"Source file {source_file} does not exist.")
        sys.exit(1)

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    generate_qr_codes(source_file, destination_dir)
