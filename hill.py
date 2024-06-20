import numpy as np
from sympy import Matrix

class HillCipher:
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = self.create_key_matrix(key)
    
    def create_key_matrix(self, key_message):
        n = int(np.sqrt(len(key_message)))
        if not all(char in self.alphabet for char in key_message):
            raise ValueError("La clave debe contener solo caracteres del alfabeto.")
        if n * n != len(key_message):
            raise ValueError("La clave no forma una matriz cuadrada válida.")
        key_matrix = np.array([self.alphabet.index(char) for char in key_message]).reshape(n, n)
        if np.gcd(int(np.linalg.det(key_matrix).round()), len(self.alphabet)) != 1:
            raise ValueError("La matriz de la clave no es invertible.")
        return key_matrix
    
    def encrypt_decrypt(self, message, encode=True):
        if len(message) % len(self.key) != 0:
            raise ValueError(f"El mensaje debe ser múltiplo de {len(self.key)}.")
        message_indices = [self.alphabet.index(char) for char in message]
        result = []
        key_matrix_inv = None
        if not encode:
            key_matrix_inv = np.array(Matrix(self.key).inv_mod(len(self.alphabet))).astype(int)
        for i in range(0, len(message_indices), len(self.key)):
            block = np.array(message_indices[i:i+len(self.key)]).reshape(-1, 1)
            if encode:
                result_block = (self.key @ block) % len(self.alphabet)
            else:
                result_block = (key_matrix_inv @ block) % len(self.alphabet)
            result.extend(result_block.flatten())
        return ''.join(self.alphabet[i] for i in result)

# Uso del cifrado Hill
cipher = HillCipher("GYBNQKURP", "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz")
message = "hello "
encrypted_msg = cipher.encrypt_decrypt(message)
print("Mensaje cifrado:", encrypted_msg)
decrypted_msg = cipher.encrypt_decrypt(encrypted_msg, encode=False)
print("Mensaje descifrado:", decrypted_msg)