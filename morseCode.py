#!/usr/bin/python
##
''' 
VARIABLE KEY 
'cipher' -> 'stores the morse translated form of the english string' 
'decipher' -> 'stores the english translated form of the morse string' 
'citext' -> 'stores morse code of a single character' 
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 
'''

# This is for later localisation
import gettext
gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
gettext.textdomain('myapplication')
_ = gettext.gettext

# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'*-', 'B':'-***', 
                    'C':'-*-*', 'D':'-**', 'E':'*', 
                    'F':'**-*', 'G':'--*', 'H':'****', 
                    'I':'**', 'J':'*---', 'K':'-*-', 
                    'L':'*-**', 'M':'--', 'N':'-*', 
                    'O':'---', 'P':'*--*', 'Q':'--*-', 
                    'R':'*-*', 'S':'***', 'T':'-', 
                    'U':'**-', 'V':'***-', 'W':'*--', 
                    'X':'-**-', 'Y':'-*--', 'Z':'--**', 
                    '1':'*----', '2':'**---', '3':'***--', 
                    '4':'****-', '5':'*****', '6':'-****', 
                    '7':'--***', '8':'---**', '9':'----*', 
                    '0':'-----', ',':'--**--', '.':'*-*-*-', 
                    '?':'**--**', '/':'-**-*', '-':'-****-', 
                    '(':'-*--*', ')':'-*--*-', '@':'*--*-*'} 
                    

# Function to encrypt the string 
# according to the morse code chart 
def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ': 
  
            # Looks up the dictionary and adds the 
            # correspponding morse code 
            # along with a space to separate 
            # morse codes for different characters 
            try:
                cip = MORSE_CODE_DICT[letter]
            except ValueError as v:
                print(_("ERROR: Character not found in morse code set!"))
                print(v)
                raise Exception(v)

            cipher += cip + '.'
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            cipher += '_'
  
    return cipher 

  
# Function to decrypt the string 
# from morse to english 
def decrypt(message): 
    # extra space added at the end to access the 
    # last morse code 
    message += ' '
  
    decipher = '' 
    citext = '' 

    for letter in message: 
  
        # checks for dot or underline 
        if (letter != '.' and letter !='_'): 
            # storing morse code of a single character 
            citext += letter 
  
        # in case of space 
        else: 
            # if letter is '_' that indicates a new word 
            if letter == '_':   
                 # adding space to separate words 
                decipher += ' '
            elif citext == '':
               # begining of message
               pass
            else:   
                # accessing the keys using their values (reverse of encryption)
                newLetter = ''
                try:
                    newLetter = list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                except ValueError as v:
                    print(_("ERROR: Morse code not found!"))
                    print(v)
                    raise Exception(v)
                decipher += newLetter
                citext = '' 
  
    return decipher 


# Function for file to file decryption/encryption
def file_conversion():
    # Wellcome to file conversion
    print(_("This is file converter!"))
    # First need to have input file name
    filename = raw_input(_("Give input file name: "))
    try:
        fr = open(filename, 'r')
    except IOError as io:
        print(_("ERROR: Input file not found!"))
        print(io)
        return False
    # Get content with out linechange character
    mess = fr.read().rstrip('\n')
    # Close file
    fr.close()

    #Ask out put file name
    output_filename = raw_input(_("Give out put file name: "))

    # Now... select what like to do
    print(_("If you like to convert text to morse code select: 1"))
    print(_("If you like to convert morse code to text select: 2"))
    print(_("If you like to quit select: q"))
    selection = raw_input(_("Selection: "))    

    if selection == '1':
        # Change all letters to uppercase
        # Encrypt
        # try to decrypt
        try:
            result = encrypt(mess.upper())
        except:
            # Something goes wrong
            return False

        fw = open(output_filename, 'w')
        fw.write(result)
        fw.close()
    elif selection == '2':
        # Check if there is two dots in a row
        if '..' in mess:
            print(_('ERROR: There can not be two dots in a row!'))
            return False
        # try to decrypt
        try:
            result = decrypt(mess)
        except:
            # Something goes wrong
            return False

        fw = open(output_filename, 'w')
        fw.write(result)
        fw.close()
    elif selection == 'q':
        print(_('Exit'))
        return True
    else:
        file_conversion()

    return True


# Hard-coded driver function to run the program 
def main(): 
    print(_("This is a morse code converter."))

    # We use only file read and write option
    ret = file_conversion()

    if ret:
        # no error
        print(_('PASS'))
    else:
        # some error occurs
        print(_('FAIL'))
  
# Executes the main function 
if __name__ == '__main__': 
    main() 