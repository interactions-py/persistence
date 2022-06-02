from random import choice, randint
from ff3 import FF3Cipher

# i hope polls is happy with this

class Cipher:
    def __init__(self, key=None):
        hex_alphabet = "0123456789ABCDEF"
        key = key or "".join(choice(hex_alphabet) for _ in range(32))
        tweak = "".join([choice(hex_alphabet) for x in range(14)])
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^*()-_=+[]{}|;':\",./<>? "
        self._cipher = FF3Cipher.withCustomAlphabet(key, tweak, alphabet)
        self.encrypt = self._cipher.encrypt
        self.decrypt = self._cipher.decrypt
    
    def chunk_decrypt(self, encrypted):
        return "".join(self.decrypt(encrypted[i:i+28]) for i in range(0, len(encrypted), 28))