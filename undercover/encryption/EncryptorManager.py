from abc import ABC, abstractmethod
from typing import Union

from undercover.encryption import BaseEncryptor


def get_file(file_path) -> bytes:
    with open(file_path, "rb") as file:
        return file.read()


def set_file(file_path, modification):
    with open(file_path, "wb") as file:
        file.write(modification)