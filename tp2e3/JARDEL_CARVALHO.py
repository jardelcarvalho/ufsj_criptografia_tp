from Crypto.Util import number
from Crypto.Random.random import getrandbits

def exp_rapida(a, x, p):
    resultado = 1
    fator = a
    while x > 0:
        if x % 2 == 1:
            resultado = (resultado * fator) % p
        fator *= fator % p
        x = x // 2
    return resultado

def euc_estendido(a, b):
    ra, r = a, b
    sa, s = 1, 0
    ta, t = 0, 1
    while r != 0:
        q = ra // r
        ra, r = r, ra - q * r
        sa, s = s, sa - q * s
        ta, t = t, ta - q * t
    return sa, ta

def mdc(a, b):
    alfa, beta = euc_estendido(a, b)
    return alfa * a + beta * b

def ch_publica(phi_N):
    e = 3
    while mdc(e, phi_N) != 1:
        if e == phi_N:
            print('e == phi(N)')
            exit(0)
        e += 1
    return e

def ch_secreta(e, phi_N):
    d, _ = euc_estendido(e, phi_N)
    return d % phi_N

def rsa_encriptar(m, e, N):
    c = exp_rapida(m, e, N)
    return c

def rsa_decriptar(c, d, N):
    md = exp_rapida(c, d, N)
    return md


if __name__ == '__main__':

    p = number.getPrime(512)
    q = number.getPrime(512)

    N = p * q
    phi_N = (p - 1) * (q - 1)
    
    e = ch_publica(phi_N)
    d = ch_secreta(e, phi_N)

    m = getrandbits(64) #mensagem
    print('Mensagem:', m)
    c = rsa_encriptar(m, e, N)
    print('Mensagem encriptada:', c)
    md = rsa_decriptar(c, d, N)
    print('Mensagem decriptada:', md)
    print('Mensagem == Mensagem decriptada:', m == md)

    