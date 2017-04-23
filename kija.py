import sys
import math
import binascii


k='31415926'

k0=int(binascii.hexlify(k[:4]),16)
k1=int(binascii.hexlify(k[4:8]),16)

def encrypt(message):
    counter=0
    hasil=''
    while counter<len(message):
        hexa=int(binascii.hexlify(message[counter:counter+4]),16)
        enc=hexa^k0
        enc=enc+k1
        enc=enc%pow(2,32)
        hasil+=binascii.unhexlify('%x' %enc)
        counter+=4
    return hasil

def decrypt(encrypted):
    counter=0
    hasil=''
    while counter<len(encrypted):
        dec=int(binascii.hexlify(encrypted[counter:counter+4]),16)
        dec-=k1
        dec%=pow(2,32)
        dec=dec^k0
        hasil+=binascii.unhexlify('%x' %dec)
        counter+=4
    return hasil

input=raw_input('String : ')

encrypted=encrypt(input)
print 'Encrypted : ' + encrypted

print 'Decrypted : ' + decrypt(encrypted)
