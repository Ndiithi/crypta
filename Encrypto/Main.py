'''
Created on Apr 25, 2017

@author: duncan
'''

import Encrypto.Crypto as crypt

if __name__== '__main__':
    print("Starting Crypto")
    
    while(1):
        stringToProcess=str(raw_input("Enter String to process: "))
        choice=int(raw_input("chose 1 for encrypt or 2 for decrypt: "))
        
        
    
        if(choice==1):
            st=crypt.encrypt(stringToProcess)
            print("The encrypted value is: ",st)
        elif(choice==2):
            print("The de-crypted value is: ",crypt.deCrypt(stringToProcess))
        else:
            print("Wrong selection, please try again");
        