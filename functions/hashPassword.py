import hashlib


def hashPassword(password):
    hash = hashlib.new('sha256')
    hash.update(bytes(password, encoding='utf-8'))
    return {"string": hash.hexdigest(), "bytes": hash.digest()}
