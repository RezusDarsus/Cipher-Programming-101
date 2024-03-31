text = input("text is: ")
def encryptAtbashCipher(text):
    normal_alphabet  =  'abcdefghijklmnopqrstuvwxyz'
    reversed_alphabet = normal_alphabet[::-1]

    encrypted_text = ''

    for char in text:
        if char.isalpha():
           index = normal_alphabet.index(char)
           encrypted_text += reversed_alphabet[index]
        else:
            encrypted_text += char


    return encrypted_text


def decryptAtbashCipher(encrypted_text):
    reversed = 'abcdefghijklmnopqrstuvwxyz'
    normal  = reversed[::-1]
    decypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            index = reversed.index(char)
            decypted_text += normal[index]
        else:
            decypted_text += char
    return decypted_text

enc = encryptAtbashCipher(text)
print("encrypted: " + encryptAtbashCipher(text))
dec = decryptAtbashCipher(enc)
print("decrypted " + decryptAtbashCipher(enc))
