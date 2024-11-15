import hashlib
import os
import sys

def hash_file(file_path):
    """Generate a hash for the given file."""
    hash_algo = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

def are_files_same(path1, path2):
    """Check if two files are the same based on their content."""
    # Ensure both paths are valid files
    if not (os.path.isfile(path1) and os.path.isfile(path2)):
        return False

    # Compare file hashes
    print(hash_file(path1))
    print(hash_file(path2))
    return hash_file(path1) == hash_file(path2)

if __name__ == "__main__":
    result = are_files_same(sys.argv[1], sys.argv[2])
    print(result)  # Output: True or False
