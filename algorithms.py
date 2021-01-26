# ===============================================================
# ============ FUNCTION TO DO ASCII BASED ENCRYPTION  ===========
# ============         BASED ON A CERTAIN KEY         ===========
# ================================================================


def encrypt(text, key=0):
    if not isinstance(text, str):
        raise TypeError("{} should be a type string".format(text))
    if not isinstance(key, int):
        raise TypeError("{} should be of type int".format(key))
    return "".join([chr(ord(something) + key) for something in text])


# ===================================================================
# ============= FUNCTION TO DO ASCII BASED DECRYPTION ===============
# =============       BASED ON A CERTAIN KEY          ===============
# ===================================================================


def decrypt(text, key=0):
    if not isinstance(text, str):
        raise TypeError("{} should be a type string".format(text))
    if not isinstance(key, int):
        raise TypeError("{} should be of type int".format(key))
    return "".join([chr(ord(something) - key) for something in text])
