from abc import ABC, abstractmethod
from typing import Union


class AbstractEncryptor(ABC):

    encryption_method: str  # describes encryption algorithm
    _encryptor: any  # encryptor module
    _encryption_key: Union[str, bytes]  # key for encrypting file, could be str or bytes
    _decryption_key: Union[str, bytes]  # key for decrypting file, could be str or bytes

    """
    Encryptor class is an abstract class for encrypting.

    Args:
        encryption_method: describes encryption algorithm
        _encryptor: encryptor module
        _encryption_key: key for encrypting file, could be str or bytes
        _decryption_key: key for decrypting file, could be str or bytes

    Attributes:
        encryption_method: describes encryption algorithm
        _encryption_key: key for encrypting file, could be str or bytes
        _decryption_key: key for decrypting file, could be str or bytes

    Methods:
        encrypt_file: encrypt file with given encryption key.
        decrypt_file: decrypt file with given decryption key.
        generate_encryption_key: generate key for encryption.
        generate_decryption_key: generate key for decryption.
        validate_key: validate given encryption key.
    """

    def __init__(self):
        super().__init__()
        pass

    @abstractmethod
    def encrypt_file(self):
        """
        Encrypt file with given key.
        :return:
            any: return encrypted file
        """
        # if subclass does not override this method, raise NotImplementedError
        raise NotImplementedError("Subclasses must implement encrypt_file method.")

    @abstractmethod
    def decrypt_file(self):
        """
        Decrypt file with given key.
        :return:
            any: return decrypted file
        """

        # if subclass does not override this method, raise NotImplementedError
        raise NotImplementedError("Subclasses must implement decrypt_file method.")

    @abstractmethod
    def generate_encryption_key(self):
        """
        generate encryption key which is long enough.
        :return:
            any: return generated encryption key
        """
        # if subclass does not override this method, raise NotImplementedError
        raise NotImplementedError("Subclasses must implement generate_encryption_key method.")

    @abstractmethod
    def generate_decryption_key(self):
        """
        generate decryption key matches with encryption key
        :return:
            any: return generated decryption key
        """
        # if subclass does not override this method, raise NotImplementedError
        raise NotImplementedError("Subclasses must implement generate_decryption_key method.")

    @abstractmethod
    def validate_key(self):
        """
        validate given keys.
        :return:
            bool: True if validated else False
        """
        # if subclass does not override this method, raise NotImplementedError
        raise NotImplementedError("Subclasses must implement validate_key method.")
