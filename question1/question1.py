#----------Question 1-----------
import os

# Always use the folder where THIS file (q1.py) is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- PART 1: CORE ENCRYPTION LOGIC (Member 1) ---

def transform_char(char, shift1, shift2, decrypt=False):
    if not char.isalpha():
        return char

    d = -1 if decrypt else 1

    # LOWERCASE RULES
    if 'a' <= char <= 'z':
        if 'a' <= char <= 'm':
            offset = d * (shift1 * shift2)
            return chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
        else:
            offset = d * (-(shift1 + shift2))
            return chr((ord(char) - ord('a') + offset) % 26 + ord('a'))

    # UPPERCASE RULES
    elif 'A' <= char <= 'Z':
        if 'A' <= char <= 'M':
            offset = d * (-shift1)
            return chr((ord(char) - ord('A') + offset) % 26 + ord('A'))
        else:
            offset = d * (shift2 ** 2)
            return chr((ord(char) - ord('A') + offset) % 26 + ord('A'))

    return char


def process_text(text, shift1, shift2, decrypt=False):
    return "".join([transform_char(c, shift1, shift2, decrypt) for c in text])


# --- PART 2: FILE HANDLING & VERIFICATION (Member 2) ---

def encrypt_file(shift1, shift2):
    try:
        with open(os.path.join(BASE_DIR, "raw_text.txt"), "r") as f:
            content = f.read()

        encrypted_content = process_text(content, shift1, shift2, decrypt=False)

        with open(os.path.join(BASE_DIR, "encrypted_text.txt"), "w") as f:
            f.write(encrypted_content)

        print("Done: 'raw_text.txt' encrypted into 'encrypted_text.txt'.")
    except FileNotFoundError:
        print("Error: Please create a file named 'raw_text.txt' first.")


def decrypt_file(shift1, shift2):
    try:
        with open(os.path.join(BASE_DIR, "encrypted_text.txt"), "r") as f:
            content = f.read()

        decrypted_content = process_text(content, shift1, shift2, decrypt=True)

        with open(os.path.join(BASE_DIR, "decrypted_text.txt"), "w") as f:
            f.write(decrypted_content)

        print("Done: 'encrypted_text.txt' decrypted into 'decrypted_text.txt'.")
    except FileNotFoundError:
        print("Error: 'encrypted_text.txt' not found.")


def verify_decryption():
    try:
        with open(os.path.join(BASE_DIR, "raw_text.txt"), "r") as f1, \
             open(os.path.join(BASE_DIR, "decrypted_text.txt"), "r") as f2:

            if f1.read() == f2.read():
                print("-" * 30)
                print("VERIFICATION SUCCESS: The original and decrypted files are identical.")
                print("-" * 30)
            else:
                print("-" * 30)
                print("VERIFICATION FAILED: The content does not match.")
                print("-" * 30)
    except FileNotFoundError:
        print("Verification Error: Files missing.")


# --- MAIN EXECUTION BLOCK ---

if __name__ == "__main__":
    raw_path = os.path.join(BASE_DIR, "raw_text.txt")

    if not os.path.exists(raw_path):
        with open(raw_path, "w") as f:
            f.write("Hello World! This is a test for shift1 and shift2.")
        print("Note: 'raw_text.txt' was created automatically for testing.")

    try:
        s1 = int(input("Enter value for shift1: "))
        s2 = int(input("Enter value for shift2: "))

        encrypt_file(s1, s2)
        decrypt_file(s1, s2)
        verify_decryption()

    except ValueError:
        print("Input is invalid. Please enter valid integers for shift values.")
