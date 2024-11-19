from Cryptodome.Cipher import AES
from base64 import b64encode


def aesEncrypt(key, password):
    password_to_encrypt = bytes(password, encoding='utf-8')
    cipher = AES.new(key, AES.MODE_CFB)
    ct_bytes = cipher.encrypt(password_to_encrypt)
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return {"iv": iv, "ct": ct}
