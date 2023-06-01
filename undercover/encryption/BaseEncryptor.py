from abc import abstractmethod


class BaseEncryptor:

    encryption_method: str  # describes encryption algorithm

    """
    Encryptor class is an abstract class for encrypting.

    Args:
        encryption_method: describes encryption algorithm
        _encryptor: encryptor module

    Methods:
        encrypt: encrypt file with given encryption key.
        decrypt: decrypt file with given decryption key.
    """

    @abstractmethod
    def encrypt_file(self, file_path, key):
        # if subclass does not override this method, raise NotImplementedError
        raise NotImplementedError("Subclasses must implement encrypt_file method.")

    @abstractmethod
    def decrypt_file(self, file_path, key):
        # if subclass does not override this method, raise NotImplementedError
        raise NotImplementedError("Subclasses must implement decrypt_file method.")

    @abstractmethod
    def encrypt(self, plain_text, key):
        """
        Encrypt file with given key.
        :param plain_text: text to be encrypted
        :param key: key for encryption
        """
        # if subclass does not override this method, raise NotImplementedError
        raise NotImplementedError("Subclasses must implement encrypt method.")

    @abstractmethod
    def decrypt(self, cipher_text, key):
        """
        Decrypt file with given key.
        :param cipher_text: text to be decrypted
        :param key: key for decryption
        """

        # if subclass does not override this method, raise NotImplementedError
        raise NotImplementedError("Subclasses must implement decrypt method.")
