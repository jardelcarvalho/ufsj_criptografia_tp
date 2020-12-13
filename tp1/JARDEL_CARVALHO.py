from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Random.random import getrandbits, randint
from Crypto.Util.Padding import pad

if __name__ == '__main__':
    print('Gerador 1')
    key = get_random_bytes(16)
    m = 2 ** 128
    x = getrandbits(128)
    for _ in range(10):
        cipher = AES.new(key, AES.MODE_CBC)
        Ekx = cipher.encrypt(pad(bytes(str(x).encode()), 16)) 
        x = (x + 1) % m
        print(b64encode(Ekx).decode('utf-8'))

    print('\nGerador 2')
    key = get_random_bytes(16)
    x = get_random_bytes(16 * 3)
    for _ in range(10):
        cipher = AES.new(key, AES.MODE_CBC)
        Ekx = cipher.encrypt(x)
        x = Ekx
        print(b64encode(Ekx).decode('utf-8')) 