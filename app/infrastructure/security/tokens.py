import secrets


def issue_token() -> str:
    return secrets.token_urlsafe(24)
