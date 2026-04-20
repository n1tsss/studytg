import hashlib


def hash_teacher_password(password: str, salt: str) -> str:
    return hashlib.sha256(f'{salt}:{password}'.encode()).hexdigest()
