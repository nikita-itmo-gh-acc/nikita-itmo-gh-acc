def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    is_up = False
    for i in range(len(plaintext)):
        j = i % len(keyword)
        if plaintext[i].isupper():
            is_up = True
        start = ord("a")
        shift = ord(keyword[j].lower()) - start
        if 65 <= ord(plaintext[i]) <= 90 or 97 <= ord(plaintext[i]) <= 122:
            if is_up:
                ciphertext += chr(start + (ord(plaintext[i].lower()) - start + shift) % 26).upper()
                is_up = False
                continue
            ciphertext += chr(start + (ord(plaintext[i].lower()) - start + shift) % 26)
        else:
            ciphertext += plaintext[i]

    # PUT YOUR CODE HERE
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    is_up = False
    for i in range(len(ciphertext)):
        j = i % len(keyword)
        if ciphertext[i].isupper():
            is_up = True
        start = ord("a")
        shift = ord(keyword[j].lower()) - start
        if 65 <= ord(ciphertext[i]) <= 90 or 97 <= ord(ciphertext[i]) <= 122:
            if is_up:
                plaintext += chr(start + (ord(ciphertext[i].lower()) - start - shift) % 26).upper()
                is_up = False
                continue
            plaintext += chr(start + (ord(ciphertext[i].lower()) - start - shift) % 26)
        else:
            plaintext += ciphertext[i]

    # PUT YOUR CODE HERE
    return plaintext
