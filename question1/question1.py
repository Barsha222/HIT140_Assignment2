import os

####### ENCRYPTION/DECRYPTION CONFIGURATION ######
ALPHABET_SIZE = 13


def shift_char(char, shift_val, direction):
    """
    Handles the rotational shift within the 13-character bounds.
    """
    if 'a' <= char <= 'm' or 'A' <= char <= 'M':
        base = ord(char.lower()) - ord('a')
    elif 'n' <= char <= 'z' or 'N' <= char <= 'Z':
        base = ord(char.lower()) - ord('n')
    else:
        return char

    if direction == 'forward':
        new_pos = (base + shift_val) % ALPHABET_SIZE
    else:
        new_pos = (base - shift_val) % ALPHABET_SIZE

    # Re-map back to ASCII
    if 'a' <= char <= 'm':
        return chr(new_pos + ord('a'))
    if 'n' <= char <= 'z':
        return chr(new_pos + ord('n'))
    if 'A' <= char <= 'M':
        return chr(new_pos + ord('A'))
    if 'N' <= char <= 'Z':
        return chr(new_pos + ord('N'))


def run_cipher(text, s1, s2, encrypt=True):
    """
    Processes the entire string based on the rules.
    """
    result = []
    for char in text:
        ####### Lowercase logic ######
        if 'a' <= char <= 'z':
            shift = (s1 * s2) if 'a' <= char <= 'm' else (s1 + s2)
            direction = 'forward' if (encrypt and 'a' <= char <= 'm') or (
                not encrypt and 'n' <= char <= 'z') else 'backward'
            result.append(shift_char(char, shift, direction))
        ######## Uppercase logic ######
        elif 'A' <= char <= 'Z':
            shift = s1 if 'A' <= char <= 'M' else (s2 ** 2)
            direction = 'backward' if (encrypt and 'A' <= char <= 'M') or (
                not encrypt and 'N' <= char <= 'Z') else 'forward'
            result.append(shift_char(char, shift, direction))
        else:
            result.append(char)
    return "".join(result)

####### FILE OPERATIONS #######


def save_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)


def load_file(filename):
    with open(filename, 'r') as f:
        return f.read()


if __name__ == "__main__":
    s1, s2 = int(input("Enter s1: ")), int(input("Enter s2: "))

    raw = load_file("raw_text.txt")

    #### Encrypt #####
    encrypted = run_cipher(raw, s1, s2, encrypt=True)
    save_file("encrypted_text.txt", encrypted)

    #### Decrypt #####
    decrypted = run_cipher(encrypted, s1, s2, encrypt=False)
    save_file("decrypted_text.txt", decrypted)

    ###### Verify ######
    print("Match Status:", raw == decrypted)
