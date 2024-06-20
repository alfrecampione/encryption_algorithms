# Affine substitution cipher
def affine_encrypt(text, key1, key2):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted += chr(((key1 * (ord(char) - shift) + key2) % 26) + shift)
        else:
            encrypted += char
    return encrypted


def multiplicative_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return 1


def affine_decrypt(text, key1, key2):
    decrypted = ""
    inverse_key1 = multiplicative_inverse(key1, 26)
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            decrypted += chr(((inverse_key1 * (ord(char) - shift - key2)) % 26) + shift)
        else:
            decrypted += char
    return decrypted


def main():
    text = "Hello, World!"
    key1 = 5
    key2 = 8
    encrypted = affine_encrypt(text, key1, key2)
    decrypted = affine_decrypt(encrypted, key1, key2)
    print(f"Text: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    assert text == decrypted


if __name__ == "__main__":
    main()
