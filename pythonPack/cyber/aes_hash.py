import cryptography as cry

from cryptography.fernet import Fernet
import hashlib as hs



# COUNTER MODE CTR VS ECB



def hash_script(convert_string):
    hex_value = hs.sha256(bytes(convert_string, 'utf-8')).hexdigest()
    hashing = 'F'
    ns = int(hashing, 16)
    convertion_bin = bin(ns)
    binValue = bin(int(hex_value, 16))[2:]
    print(hex_value)

def electronic_cb (key: bytes, value : bytes):
    # key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(value)

    # 3. Decrypt data
    plain_text = cipher_suite.decrypt(cipher_text)
    print(plain_text.decode('utf-8'))  # Output: Secret message


electronic_cb( 00000000000000000000000000000000, b'f34481ec3cc627bacd5dc3fb08f273e6')
hash_script("hello")