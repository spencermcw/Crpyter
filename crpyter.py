#!python

import base64
from enum import Enum
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Operation(Enum):
    ENCODE = 1
    DECODE = 2


def pass_to_key(password, salt):
    password = bytes(password, 'utf-8')
    salt = bytes(salt, 'utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=500000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


def execute(password, salt, inText, op):
    if(not op in Operation):
        return None
    try:
        # Encryption Credentials
        key = pass_to_key(password, salt)
        f = Fernet(key)
        inBytes = bytes(inText, 'utf-8')
        # Encrypt
        if op == Operation.ENCODE:
            # print('ENCODING')
            token = f.encrypt(inBytes)
        # Decrypt
        elif op == Operation.DECODE:
            # print('DECODING')
            token = f.decrypt(inBytes)
        # End
        # print(token)
        return token.decode('utf-8')
    except Exception as e:
        # print('Exception:', type(e))
        return None
