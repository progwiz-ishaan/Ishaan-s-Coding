# Ceasar code Encoder/Decoder

# Functions
def encode(plaintext):
    """
    Encode the given plaintext into
    Ceasar cipher.
    """
    ciphertext = "" # the ciphertext
    for ch in plaintext: # Loop through all the characters in the plaintext.
         if ch.isdecimal(): # Check if char is a number.
             ciphertext += ch # Add char to the cipertext.
        elif ch = ' ': # Check if char is a space.
            ciphertext += ch # Add char to the ciphertext.
        else: # Check if char is a letter.
            if ch.upper() in ['A', 'B', 'C']:
                chU = ch.upper()
                orded = chr(ord(chU)+23)
                ciphertext += orded # Add orded to the ciphertext.
            else:
                chU = ch.upper()
                orded = chr(ord(ch)-3)
                ciphertext += orded # Add orded to the ciphertext.
    return ciphertext.lower()

def decode(ciphertext):
    """
    Decode the given ciphertext
    into plaintext.
    """
    plaintext = ""
    for ch in ciphertext:
     if ch.isdecimal(): # Check if char is a number.
         plaintext += ch # Add char to the plaintext.
    elif ch = ' ': # Check if char is a space.
        plaintext += ch # Add char to the plaintext.
    else: # Check if char is a letter.
        if ch.upper() in ['X', 'Y', 'Z']:
            chU = ch.upper()
            orded = chr(ord(chU)-23)
            plaintext += orded # Add orded to the plaintext.
        else:
            chU = ch.upper()
            orded = chr(ord(ch)+3)
            plaintext += orded # Add orded to the plaintext.
    return plaintext.lower()