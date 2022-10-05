import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for c in plaintext:
        if 97 <= ord(c) <= 122:
            ciphertext += chr(97 + (ord(c) - 97 + shift) % 26)
        elif 65 <= ord(c) <= 90:
            ciphertext += chr(65 + (ord(c) - 65 + shift) % 26)
        else:
            ciphertext += c
    # PUT YOUR CODE HERE
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """

    plaintext = ""
    for c in ciphertext:
        if 97 <= ord(c) <= 122:
            plaintext += chr(97 + (ord(c) - 97 - shift) % 26)
        elif 65 <= ord(c) <= 90:
            plaintext += chr(65 + (ord(c) - 65 - shift) % 26)
        else:
            plaintext += c
    # PUT YOUR CODE HERE
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
