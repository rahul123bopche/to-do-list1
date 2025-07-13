import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    # Define possible character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = letters + digits + symbols

    # Ensure at least one character from each category
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_chars, k=length - 3)

    # Shuffle to avoid predictable order
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()