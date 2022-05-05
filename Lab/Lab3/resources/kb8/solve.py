import binascii

binary= ""
with open("LoveLetter.txt","r") as file:
    print(file)
    for char in file.read():
        if char == ' ':
            binary = binary + "0"
        if ord(char) == 160:
            binary = binary + "1"

print("Binary result: " + binary)

bin_form = '0b' + binary # Convert to binary format
dec_form = int(bin_form, 2) # Prepare for unhexlify
decoded_result = binascii.unhexlify('%x' % dec_form)

print(decoded_result)
