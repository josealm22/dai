# generate_token.py
import secrets

token = secrets.token_urlsafe(32)
with open("../secret_token.txt", "w") as f:
    f.write(token)
print(f"Token generado y guardado en secret_token.txt: {token}")
