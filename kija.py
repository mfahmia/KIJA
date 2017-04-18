import sys
import math
import binascii


k='31415926'

k0=int(binascii.hexlify(k[:4]),16)
k1=int(binascii.hexlify(k[4:8]),16)

def encrypt(message):
    hexa=int(binascii.hexlify(message),16)
    enc=hexa^k0
    enc=enc+k1
    enc=enc%pow(2,32)
    return binascii.unhexlify('%x' %enc)

def decrypt(encrypted):
    dec=int(binascii.hexlify(encrypted),16)
    dec-=k1
    dec%=pow(2,32)
    dec=dec^k0
    return binascii.unhexlify('%x' %dec)

def read4char(message,type):
    counter=0
    hasil=''
    while counter<len(message):
        if(type=='encrypting'):
            hasil+=encrypt(message[counter:counter+4])
            counter+=4
        elif(type=='decrypting'):
            hasil+=decrypt(message[counter:counter+4])
            counter+=4
    return hasil

oaeo=raw_input('String : ')

encrypted=read4char(oaeo,'encrypting')
print 'Encrypted : ' + encrypted
print len(encrypted)

print 'Decrypted : ' + read4char(encrypted,'decrypting')
