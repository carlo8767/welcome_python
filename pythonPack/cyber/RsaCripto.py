from cryptography.hazmat.primitives import serialization

# Generate private key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from jwt import InvalidSignatureError


# CREATION KEY FIRST
# SERIALIZATION
def generate_private_key ():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    print(type(private_key))
    return private_key


def serializations(private_key):
    pem = private_key.private_bytes(
       encoding=serialization.Encoding.PEM,
       format=serialization.PrivateFormat.PKCS8,
       encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
        )
    pem.splitlines()[0]
    # PRINT PRIVATE KEY
    print(pem)
    b'-----BEGIN ENCRYPTED PRIVATE KEY-----'

def encode_message():
    message = b"A message I want to sign"
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print(signature)
    return  signature, message


def generate_public_key(private_key, message, signature):

    try:
        public_key = private_key.public_key()
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    except InvalidSignatureError:
        print("invalid signature")



private_key = generate_private_key()
serializations(private_key)
signature, message = encode_message()
generate_public_key(private_key, message, signature)