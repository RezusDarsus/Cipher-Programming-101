def encryptSimpleEnigmaCipher(text, keys):
    enca = ""
    k1, k2, k3 = keys
    for char in text:
        if char.isalpha():
            lower = char.lower()
            i1 = ord(k1[ord(lower) - 97]) - 97
            i2 = ord(k2[i1]) - 97
            i3 = ord(k3[i2]) - 97
            enc = chr(i3 + 97)
            enca += enc.upper() if char.isupper() else enc
        else:
            enca += char
    return enca
def decryptSimpleEnigmaCipher(enc, keys):
    deca = ""
    k1, k2, k3 = keys
    for char in enc:
        if char.isalpha():
            lower = char.lower()
            i3 = ord(lower) - 97
            i2 = k3.index(chr(i3 + 97))
            i1 = k2.index(chr(i2 + 97))
            dec = chr(k1.index(chr(i1 + 97)) + 97)
            deca += dec.upper() if char.isupper() else dec
        else:
            deca += char
    return deca
keys = ("bcdefghijklmnopqrstuvwxyza","qwertyuioplkjhgfdsazxcvbnm","zxcvbnmlkjhgfdsaqwertyuiop")
print("key: ", keys)
text = "Cipher Programming - 101!"
print("Text: ", text)
enc = encryptSimpleEnigmaCipher(text, keys)
print("Encrypted text: ", enc)
dec = decryptSimpleEnigmaCipher(enc, keys)
print("Decrypted text: ", dec)

