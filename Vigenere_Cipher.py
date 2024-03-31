def encryptVigenereCipher(plaintext, keys):
    enc = ""

    lena = len(keys)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            k = keys[i % lena]

            if char.islower():
                enc = enc + chr((ord(char) - 97 + k) % 26 + 97)
            else:
                enc = enc + chr((ord(char) - 65 + k) % 26 + 65)
        else:
            mapping = {'.': ',', ',': '.', '!': '?', '?': '!',
                       '0': '1', '1': '0', '2': '3', '3': '2',
                       '4': '5', '5': '4', '6': '7', '7': '6',
                       '8': '9', '9': '8'}

            enc = enc + mapping.get(char, char)

    return enc

def decryptVigenereCipher(encrypted, keys):
    dec = ""
    lana = len(keys)

    for i, char in enumerate(encrypted):
        if char.isalpha():
            k = keys[i % lana]

            if char.islower():
                dec = dec + chr((ord(char) - 97 - k) % 26 + 97)
            else:
                dec = dec + chr((ord(char) - 65 - k) % 26 + 65)
        else:
            mapping = {'.': ',', ',': '.', '!': '?', '?': '!',
                       '0': '1', '1': '0', '2': '3', '3': '2',
                       '4': '5', '5': '4', '6': '7', '7': '6',
                       '8': '9', '9': '8'}

            dec = dec + mapping.get(char, char)

    return dec

keys = [1, 3, 2]
print("Key: ", keys)

text = "Cipher Programming - 101!"
print("Text: ", text)

enc = encryptVigenereCipher(text, keys)
print("Encrypted text: ", enc)

dec = decryptVigenereCipher(enc, keys)
print("Decrypted text: ", dec)
