def vigenere_encrypt(text, key):
    encrypted = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            key_shift = 65 if key[i % key_length].isupper() else 97
            encrypted += chr(((ord(char) - shift + ord(key[i % key_length]) - key_shift) % 26) + shift)
        else:
            encrypted += char
    return encrypted


def vigenere_decrypt(text, key):
    decrypted = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            key_shift = 65 if key[i % key_length].isupper() else 97
            decrypted += chr(((ord(char) - shift - (ord(key[i % key_length]) - key_shift)) % 26) + shift)
        else:
            decrypted += char
    return decrypted


def main():
    text = "Hello, World!"
    key = "key"
    encrypted = vigenere_encrypt(text, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Text: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    assert text == decrypted


if __name__ == "__main__":
    main()
