from typing import Union
from undercover.encryption.BaseEncryptor import BaseEncryptor
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class AES(BaseEncryptor):
    def encrypt_file(self, file_path, key):
        pass

    def decrypt_file(self, file_path, key):
        pass

    encryption_method: str  # describes encryption algorithm
    bit_length: int  # a length of bit for encryption key generation
    _module: AESGCM
    _key: Union[str, bytes]  # key for encrypting file, could be str or bytes
    _nonce: any
    _associated_data: any

    def __init__(self, bit_length: int = 256):
        super().__init__()
        self.encryption_method = "AESGCM"  # A
        if bit_length in (128, 192, 256):
            self.bit_length = bit_length
        else:
            raise AES.AESInvalidBitLengthException(bit_length)
        _key = AESGCM.generate_key(bit_length=bit_length)
        _module = AESGCM(_key)

    def initialize(self):
        return

    def encrypt(self, plain_text, key):
        return

    def decrypt(self, cipher_text, key):
        return

    class AESInvalidBitLengthException(Exception):
        def __init__(self, bit_length: int):
            super().__init__(f"Valid value for bit length for AES Encryption key are only " +
                             f"128, 192, 256 but {bit_length} was provided.")
