import string
import random
from base64 import b64encode, b64decode

FLAG = open("ciphertext.txt").read()
dec_ciphers = ['rot13', 'b64d', 'caesard']

def rot13(s):
	_rot13 = string.maketrans( 
    	"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    	"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	return string.translate(s, _rot13)

def b64d(s):
	return b64decode(s)

def caesar(plaintext, shift=3):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def caesard(ciphertext, shift=3):
	return caesar(ciphertext, shift=-shift)

def decode(ct):
    while True:
        try:
            i = int(ct[0]) - 1 
            i = i % 3
        except:
            print(ct)
            exit(0)
        ct = ct[1:]
        c = dec_ciphers[i]
        _ct = globals()[c](ct)
        ct = _ct
    
    

if __name__ == '__main__':
	decode(FLAG)