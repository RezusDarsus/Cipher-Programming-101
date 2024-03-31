def encryptCaesarCipher(text, k):
    enc = ""
    for char in text:
        if char.isalpha():
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

def decryptCaesarCipher(encrypted, k):
    dec = ""
    for char in encrypted:
        if char.isalpha():
            if char.islower():
                dec = dec + chr((ord(char) - 97 - k) % 26 + 97)
            else:
                dec = dec + chr((ord(char) - 65 - k) % 26 + 65)
        else:
            mapping = {',': '.', '.': ',', '?': '!', '!': '?',
                       '1': '0', '0': '1', '3': '2', '2': '3',
                       '5': '4', '4': '5', '7': '6', '6': '7',
                       '9': '8', '8': '9'}
            dec = dec + mapping.get(char, char)
    return dec

text = input("text ")
k = int(input("write shift "))
print("key: ", k)
print("text: ", text)
enc = encryptCaesarCipher(text, k)
print("encrypted text: ", enc)

dec = decryptCaesarCipher(enc, k)
print("decrypted text: ", dec)

