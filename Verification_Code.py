import csv
import sys
from collections import defaultdict

def read_voter_ids(filename):
    """
    Reads voter IDs from a CSV file.
    Assumes that each row contains the voter ID in the first column.
    """
    ids = []
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:  # skip empty rows
                ids.append(row[0].strip())
    return ids

def main():
    if len(sys.argv) != 3:
        print("Usage: python cross_check_voter_ids.py <voter_ids.csv> <official_list.csv>")
        sys.exit(1)
    
    voter_ids_file = sys.argv[1]
    official_list_file = sys.argv[2]
    
    # Load the official voter IDs into a set for fast lookup
    official_ids = set(read_voter_ids(official_list_file))
    
    # Read all voter IDs from the provided file
    voter_ids = read_voter_ids(voter_ids_file)
    
    invalid_ids = []  # IDs not found in the official list
    valid_ids_count = defaultdict(int)  # Count occurrences of valid voter IDs

    # Process each voter ID
    for vid in voter_ids:
        if vid in official_ids:
            valid_ids_count[vid] += 1
        else:
            invalid_ids.append(vid)
    
    # Identify valid IDs that occur more than once
    duplicate_ids = [vid for vid, count in valid_ids_count.items() if count > 1]
    
    # Write the invalid IDs to a CSV file
    with open("invalid_ids.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Invalid Voter IDs"])
        for invalid in invalid_ids:
            writer.writerow([invalid])
    
    # Write the duplicate valid IDs to a CSV file
    with open("duplicate_ids.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Valid Voter IDs Occurring More Than Once"])
        for dup in duplicate_ids:
            writer.writerow([dup])
    
    print("Invalid voter IDs (not on the official list) have been written to invalid_ids.csv")
    print("Valid voter IDs occurring more than once have been written to duplicate_ids.csv")

if __name__ == "__main__":
    main()
