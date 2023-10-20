import hashlib

def getNonce(inputString, leadingZeroes):

    target = "0"*leadingZeroes

    nonce = 0

    while(True):

        inStr = inputString + str(nonce)
        hashobj = hashlib.sha256()

        hashobj.update(inStr.encode())

        hashstr = hashobj.hexdigest()

        if(hashstr[:leadingZeroes] == target):
            print(hashstr)
            return nonce
        
        nonce = nonce +1


inputString = input("enter the string: ")

print(getNonce(inputString, 6))


