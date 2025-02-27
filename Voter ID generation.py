import random
import string

def generate_string():
    # First character: must be a letter (uppercase or lowercase)
    first = random.choice(string.ascii_letters)
    
    # Next three characters: can be any (letters, digits, or punctuation)
    mid_part = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=3))
    
    # Fifth character: must be a special character (not a letter or digit)
    special = random.choice(string.punctuation)
    
    # Next four characters: can be any (letters, digits, or punctuation)
    next_four = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=4))
    
    # Last character: must be a letter
    last = random.choice(string.ascii_letters)
    
    return first + mid_part + special + next_four + last

def main():
    unique_strings = set()

    while len(unique_strings) < 200:
        unique_strings.add(generate_string())

    # Write the unique strings to a file
    with open('output.txt', 'w') as file:
        for s in unique_strings:
            file.write(s + '\n')
    
    print("200 unique strings have been exported to output.txt.")

if __name__ == '__main__':
    main()
