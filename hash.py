import hashlib


def convertHash(inputString):

    hashobject = hashlib.sha256()

    hashobject.update(inputString.encode())

    hashString = hashobject.hexdigest()

    return hashString

str = input("enter the string: ")
print(convertHash(str))