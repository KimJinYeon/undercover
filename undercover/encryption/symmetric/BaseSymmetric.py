from abc import ABC, abstractmethod

from undercover.encryption.BaseEncryptor import BaseEncryptor


class BaseSymmetric(BaseEncryptor):
    @abstractmethod
    def generate_key(self):
        pass
