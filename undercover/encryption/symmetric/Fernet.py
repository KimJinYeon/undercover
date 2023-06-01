from typing import Union

from cryptography.fernet import Fernet

from undercover.encryption.symmetric.BaseSymmetric import BaseSymmetric


class Fernet(BaseSymmetric):

    encryption_method: str  # describes encryption algorithm
    _encryptor: Fernet
    _key: Union[str, bytes]  # key for encrypting file, could be str or bytes

    def __init__(self, key):
        super().__init__()
        self.encryption_method = "FERNET"
        self._key = Fernet.generate_key()
        self._encryptor = Fernet(self._key)

    def encrypt_file(self, file_path, key):
        text = get_file(file_path)
        encrypted = self.encrypt(text, key)
        set_file(file_path)
        pass




    def encrypt(self, plain_text, key) -> bytes:
        pass

    def decrypt(self, cipher_text, key) -> bytes:
        pass

