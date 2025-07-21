import hashlib   # To generate secure hash values
import json      # To save and load hash values in a JSON file
import os        # To check file existence and paths

# ---------------------------------------------------
# Function: calculate_hash
# Purpose : To generate a unique hash of a file's content using SHA-256
# ---------------------------------------------------

def calculate_hash(file_path):
    sha256 = hashlib.sha256()  # Create a SHA256 hash object

    with open(file_path, "rb") as file:  # Open file in binary mode
        while True:
            chunk = file.read(4096)      # Read file in chunks of 4KB
            if not chunk:
                break
            sha256.update(chunk)         # Update the hash with each chunk

    return sha256.hexdigest()            # Return the final hash string

# ---------------------------------------------------
# Function: create_baseline
# Purpose : To create a JSON file with hash values of important files
# ---------------------------------------------------

def create_baseline(file_list, output_file="hashes.json"):
    # Prevent accidentally overwriting an existing baseline
    if os.path.exists(output_file):
         print(f"⚠️  Baseline file '{output_file}' already exists.")
        return

    hashes = {}
