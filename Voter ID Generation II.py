import random
import string
import pandas as pd

def generate_unique_id(existing_ids):
    """Generate a unique voter ID based on given constraints."""
    while True:
        first = random.choice(string.ascii_letters)
        mid_part = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=3))
        special = random.choice(string.punctuation)
        next_four = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=4))
        last = random.choice(string.ascii_letters)
        
        voter_id = first + mid_part + special + next_four + last
        
        if voter_id not in existing_ids:
            existing_ids.add(voter_id)
            return voter_id

def append_voter_ids(input_csv, output_csv):
    """Reads a CSV file, appends a column with unique voter IDs, and saves it."""
    df = pd.read_csv(input_csv)
    unique_ids = set()

    df['Voter_ID'] = [generate_unique_id(unique_ids) for _ in range(len(df))]
    
    df.to_csv(output_csv, index=False)
    print(f"Updated CSV file with voter IDs saved as {output_csv}")

if __name__ == '__main__':
    input_file = 'FinalVoterRollCall.csv'  # Change this to the actual input file
    output_file = 'FinalVoterRollCall_with_ids.csv'  # Output file name
    append_voter_ids(input_file, output_file)
