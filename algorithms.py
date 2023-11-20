from itertools import cycle

def encrypt(text, key='0'):
    if not text:
        raise ValueError("Text should not be empty")
    if not key:
        raise ValueError("Key should not be empty")
    
    key = key.encode() if isinstance(key, str) else key
    encrypted_text = ""
    
    for char, key_char in zip(text, cycle(key)):
        encrypted_text += chr((ord(char) + ord(key_char)) % 128)
    
    return encrypted_text

def decrypt(text, key='0'):
    if not text:
        raise ValueError("Text should not be empty")
    if not key:
        raise ValueError("Key should not be empty")
    
    key = key.encode() if isinstance(key, str) else key
    decrypted_text = ""
    
    for char, key_char in zip(text, cycle(key)):
        decrypted_text += chr((ord(char) - ord(key_char)) % 128)
    
    return decrypted_text

# Example Usage:
original_message = "Hello, World!"
encryption_key = "secretkey"

encrypted_message = encrypt(original_message, encryption_key)
print(f"Encrypted: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, encryption_key)
print(f"Decrypted: {decrypted_message}")
