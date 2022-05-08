def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    counter = 0;
    for c in letters:
        key[c] = letters[(counter + n) % len(letters)]
        counter += 1
    return key

def encrypter(key, msg):
    cipher = ""
    for c in msg:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher;

def getDecrypterKey(key):
    dKey = {}
    for c in key:
        dKey[key[c]] = c
    return dKey

key = generate_key(3)
print(key)

a = encrypter(key, "YOU ARE AWESOME")
print(a)
b = encrypter(getDecrypterKey(key), a)
print(b)    