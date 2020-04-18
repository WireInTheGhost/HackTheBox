#This is the process we need to undo
"""
def encrypt(text, key):
    keylen = len(key)
    keyPos = 0
    encrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr + ord(keyChr)) % 255)
        encrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen
    return encrypted
"""

#We need a cipher text with its plain text counterpart
cFile = 'out.txt'
pFile = 'check.txt'

#Read the files in
with open(cFile, encoding = 'UTF-8') as f:
    cText = f.read()
with open(pFile, encoding = 'UTF-8') as f:
    pText = f.read()

key = ""

i = -1 #index for plain text char start at -1 for increment

try:
    #Loop each character in cipher text
    for cChar in cText:
        #Convert char to ASCII code
        aChar = ord(cChar)
        i += 1#increment index (start at 0)
        #Loop likely ASCII codes
        for ac in range(33,127):
            #Reverse enc process
            testChar = chr((aChar - ac) % 255)
            #Check if they match
            if testChar == pText[i]:
                #If they match print
                key += chr(ac)
                break

    print(key)
except Exception as e:
    message = f"""
    The following error occured: {e}
    The key may be: {key}
    """
    print(message)
