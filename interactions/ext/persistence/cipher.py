"""This file houses the customized Cipher class using the ff3 library."""

from random import choice, randint
from ff3 import FF3Cipher

from .scripts import generate_key


class Cipher:
    """A special Cipher object for encrypting and decrypting packages and tags."""

    def __init__(self, key=None):
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^*()-_=+[]{}|;':\",./<>? "
        key = key or generate_key()
        tweak = "CBD09280979564" # Bad practice; should be private and random. Could not find way to do this.
        # Must mention in docs to never put anything private inside of custom_ids.
        self._encrypter = FF3Cipher.withCustomAlphabet(key, tweak, alphabet)

    def encrypt(self, plain_text: str):
        """
        Encrypts a string.

        Parameters:
            plain_text (str): The string to encrypt.

        Returns:
            str: The encrypted string.
        """
        if len(plain_text) <= 28:
            return self._encrypter.encrypt(plain_text)
        chunks = [str(plain_text[i : i + 28]) for i in range(0, len(plain_text), 28)]
        encrypted_chunks = [self._encrypter.encrypt(chunk) for chunk in chunks]
        return "".join(encrypted_chunks)

    def decrypt(self, encrypted_text):
        """
        Decrypts a string.

        Parameters:
            encrypted_text (str): The string to decrypt.

        Returns:
            str: The decrypted string.
        """
        if len(encrypted_text) <= 28:
            return self._encrypter.decrypt(encrypted_text)
        chunks = [str(encrypted_text[i : i + 28]) for i in range(0, len(encrypted_text), 28)]
        decrypted_chunks = [self._encrypter.decrypt(chunk) for chunk in chunks]
        return "".join(decrypted_chunks)
