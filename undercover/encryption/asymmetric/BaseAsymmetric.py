from abc import ABC, abstractmethod

from undercover.encryption.BaseEncryptor import BaseEncryptor


class BaseAsymmetric(BaseEncryptor):
    @abstractmethod
    def generate_private_key(self):
        pass

    @abstractmethod
    def generate_public_key(self):
        pass
