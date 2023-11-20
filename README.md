# ascii-encryption-python
Beginner guide to ascii based encryption implemented in Python 

Getting started 
----------------
This is just a simple encryption algorithms that can be cool when it comes to understanding and exploring how does encryption works, but not seriously used to handle security on real life circumstances 

To get started with repo you might have to clone or download the repository just as shown below;

```bash

git clone https://github.com/Kalebu/ascii-encryption-python

```

Basics
----------------
If you're new to ascii encryption, this simple involving converting the alphabetics to their ascii numerical value and using a secret number to add or substract from their real value and then turning back into characters as encrypted one.

For instance 

```bash

Encrypting 

a - > 97 -> 97 (+|-) secret_number -> new characer

Lets say our secret number is 5

a -> 97 -> 97 + 5 -> f

Decrypting 

To descrypt we need to know the secret number otherwise we wont be able to do it so

f -> 102 -> 102 (+|-) secret number -> decrypted character

Since we know the serect number is 5

f -> 102 -> 102 - 5 > a 

```

In this repository I have implemented two simple function just do that, which take a textual input of any size and then encrypt it using ascii value based on your secret number and then it will return back encrypted text.

Samewise to decryption, you are going to specify the secret number and then it will recieve your encrypted text input and then render to you decrypted text output 

# ASCII-based Encryption/Decryption

This Python script provides simple ASCII-based encryption and decryption functionalities. The code has been improved to enhance key handling, error checking, and overall robustness.

## Improvements

### Key Handling
- The `key` parameter now accepts both strings and bytes, providing more flexibility for different types of keys.
- The key is automatically encoded if it is provided as a string.

### Non-ASCII Characters
- The script now handles non-ASCII characters more gracefully.

### Error Handling
- Error checks have been added to ensure that both the text and the key are not empty.

### Modulo Operation
- A modulo operation has been introduced to prevent overflow issues during character shifting. This ensures that the character values stay within the valid ASCII range.

## Usage

```python
from itertools import cycle

def encrypt(text, key='0'):
    # ... (implementation details)

def decrypt(text, key='0'):
    # ... (implementation details)

# Example Usage:
original_message = "Hello, World!"
encryption_key = "secretkey"

encrypted_message = encrypt(original_message, encryption_key)
print(f"Encrypted: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, encryption_key)
print(f"Decrypted: {decrypted_message}")


Demo 
------------

```python
>>> from algorithms import encrypt , decrypt
>>> army_text = "Throw the missiles at 9pm"
>>> encrypt(army_text, key=10)
'^r|y\x81*~ro*ws}}svo}*k~*Czw'
>>> decrypt('^r|y\x81*~ro*ws}}svo}*k~*Czw', key=10)
'Throw the missiles at 9pm'
```

Explore it 
-----------
Now keep explore it by testing it with various input text to see how you can twist it to your own use

Give it a star 
--------------
Did you find this information useful, then give it a star 


Credits
-----------
All the credits to [kalebu](github.com/kalebu)
