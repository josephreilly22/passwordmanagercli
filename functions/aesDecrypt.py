from base64 import b64decode
from Cryptodome.Cipher import AES


def aesDecrypt(key, value, iv):
    try:
        ct = b64decode(value)
        iv = b64decode(iv)
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)
        pt = cipher.decrypt(ct)
        return pt
    except (ValueError, KeyError):
        return False
    