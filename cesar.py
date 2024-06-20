# Cesar encryption and decryption

def cesar_encrypt(text, key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted += char
    return encrypted


def cesar_decrypt(text, key):
    return cesar_encrypt(text, -key)


def main():
    text = "Hello, World!"
    key = 3
    encrypted = cesar_encrypt(text, key)
    decrypted = cesar_decrypt(encrypted, key)
    print(f"Text: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    assert text == decrypted


if __name__ == "__main__":
    main()
