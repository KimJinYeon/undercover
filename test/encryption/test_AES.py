import pytest

from undercover.encryption.symmetric.AES import AES


class TestAES:
    @pytest.fixture
    def aes(self):
        return AES()

    def test_encrypt_file(self, aes):
        file_path = "testme.txt"
        encryption_key = aes.generate_encryption_key()

        aes.set_encryptor(encryption_key)
        aes.encrypt(file_path, encryption_key)
        print(aes._nonce)
        # aes.decrypt_file(file_path, encryption_key)
        assert True

    def test_decrypt_file(self):
        assert False

    def test_generate_encryption_key(self):
        assert False

    def test_generate_decryption_key(self):
        assert False

    def test_set_encryption_key(self):
        assert False

    def test_get_encryption_key(self):
        assert False

    def test_set_decryption_key(self):
        assert False

    def test_get_decryption_key(self):
        assert False

    def test_set_encryptor(self):
        assert False

    def test_validate_key(self):
        assert False
