'''
Created on Apr 25, 2017

@author: duncan
'''
import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def encrypt(stringToEncrypt):
    x=str(stringToEncrypt)
    encryptedValue=x[0]
    
    for y in range(1,len(x)):
        if(x[y]==x[y-1]):
            logger.debug("Equal to previous")
            encryptedValue=encryptedValue+chr(ord(x[y])+1)
            print(x[y]," --> ", chr(ord(x[y])+y))
        else:
            encryptedValue=encryptedValue+chr(ord(x[y])+y)      
            print(x[y]," --> ", chr(ord(x[y])+y))
    print("Encryption fineshed")
    return encryptedValue
        

''' 
deCrypted valuein referene to ascii table
'''

def deCrypt(stringToDecrypt):
    x=str(stringToDecrypt)
    decryptedValue=x[0]
    
    for y in range(1,len(x)):
        if(x[y]==x[y-1]):
             decryptedValue=decryptedValue+chr(ord(x[y])-1)
        else:
            decryptedValue=decryptedValue+chr(ord(x[y])-y)    
    print("Decryption finished")
    return decryptedValue