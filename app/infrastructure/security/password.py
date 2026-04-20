import hashlib


def hash_password(raw: str, salt: str) -> str:
    return hashlib.sha256(f'{salt}:{raw}'.encode()).hexdigest()


def verify_password(raw: str, hashed: str, salt: str) -> bool:
    return hash_password(raw, salt) == hashed
