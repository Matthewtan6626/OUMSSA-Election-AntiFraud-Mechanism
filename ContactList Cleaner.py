import pandas as pd

def remove_duplicates_by_email(input_csv, output_csv):
    """
    Reads a CSV file, removes duplicate rows based on the 'Email' column,
    and saves the cleaned file.
    """
    # Read the CSV file
    df = pd.read_csv(input_csv, dtype=str)  # Read all data as strings to avoid type mismatches

    # Normalize the 'Email' column (strip spaces and standardize case)
    df['Email'] = df['Email'].str.strip().str.lower()

    # Remove duplicates based on the 'Email' column, keeping the first occurrence
    df_cleaned = df.drop_duplicates(subset=['Email'], keep='first')

    # Save the cleaned data to a new file
    df_cleaned.to_csv(output_csv, index=False)

    print(f"Duplicate-free CSV saved as: {output_csv}")


# Example Usage
input_file = "ContactListOUMSSAElectorate.csv"  # Change this to the actual CSV file path
output_file = "CleanedContactListOUMSSAElectorate.csv"

remove_duplicates_by_email(input_file, output_file)
