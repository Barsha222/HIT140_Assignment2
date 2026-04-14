import os

# --- PART 1: CORE ENCRYPTION LOGIC (Member 1) ---


def transform_char(char, shift1, shift2, decrypt=False):
    """
    Handles the mathematical shift for a single character based on 
    specific alphabetic ranges.
    """
    if not char.isalpha():
        return char

    # d is the direction: 1 for encryption, -1 for decryption
    d = -1 if decrypt else 1

    # LOWERCASE RULES
    if 'a' <= char <= 'z':
        if 'a' <= char <= 'm':
            # Rule: shift forward by (shift1 * shift2)
            offset = d * (shift1 * shift2)
            return chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
        else:
            # Rule: shift backward by (shift1 + shift2)
            offset = d * (-(shift1 + shift2))
            return chr((ord(char) - ord('a') + offset) % 26 + ord('a'))

    # UPPERCASE RULES
    elif 'A' <= char <= 'Z':
        if 'A' <= char <= 'M':
            # Rule: shift backward by shift1
            offset = d * (-shift1)
            return chr((ord(char) - ord('A') + offset) % 26 + ord('A'))
        else:
            # Rule: shift forward by shift2 squared
            offset = d * (shift2 ** 2)
            return chr((ord(char) - ord('A') + offset) % 26 + ord('A'))

    return char


def process_text(text, shift1, shift2, decrypt=False):
    """Iterates through text to apply transformations."""
    return "".join([transform_char(c, shift1, shift2, decrypt) for c in text])


# --- PART 2: FILE HANDLING & VERIFICATION (Member 2) ---

def encrypt_file(shift1, shift2):
    try:
        with open("raw_text.txt", "r") as f:
            content = f.read()

        encrypted_content = process_text(
            content, shift1, shift2, decrypt=False)

        with open("encrypted_text.txt", "w") as f:
            f.write(encrypted_content)
        print("Done: 'raw_text.txt' encrypted into 'encrypted_text.txt'.")
    except FileNotFoundError:
        print("Error: Please create a file named 'raw_text.txt' first.")


def decrypt_file(shift1, shift2):
    try:
        with open("encrypted_text.txt", "r") as f:
            content = f.read()

        decrypted_content = process_text(content, shift1, shift2, decrypt=True)

        with open("decrypted_text.txt", "w") as f:
            f.write(decrypted_content)
        print("Done: 'encrypted_text.txt' decrypted into 'decrypted_text.txt'.")
    except FileNotFoundError:
        print("Error: 'encrypted_text.txt' not found.")


def verify_decryption():
    try:
        with open("raw_text.txt", "r") as f1, open("decrypted_text.txt", "r") as f2:
            if f1.read() == f2.read():
                print("-" * 30)
                print(
                    "VERIFICATION SUCCESS: The original and decrypted files are identical.")
                print("-" * 30)
            else:
                print("-" * 30)
                print("VERIFICATION FAILED: The content does not match.")
                print("-" * 30)
    except FileNotFoundError:
        print("Verification Error: Files missing.")

# --- MAIN EXECUTION BLOCK ---


if __name__ == "__main__":
    # Ensure raw_text.txt exists for a smooth demo
    if not os.path.exists("raw_text.txt"):
        with open("raw_text.txt", "w") as f:
            f.write("Hello World! This is a test for shift1 and shift2.")
        print("Note: 'raw_text.txt' was created automatically for testing.")

    try:
        # 1. Prompt for inputs
        s1 = int(input("Enter value for shift1: "))
        s2 = int(input("Enter value for shift2: "))

        # 2. Encrypt
        encrypt_file(s1, s2)

        # 3. Decrypt
        decrypt_file(s1, s2)

        # 4. Verify
        verify_decryption()

    except ValueError:
        print("Invalid input. Please enter integers for the shift values.")
