def decode_morse_code():
    value = input("Enter the morse code to decipher: ")
    decode_morse = { '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H', '..':'I',
                    '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R',
                    '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z', '.----':'1',
                    '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':',', '.-.-.-':'.', '..--..':'?', '-..-.':'/', '-....-':'-', '-.--.':'(', '-.--.-':')', ' ':' ' }
    for letter in value:
        print(decode_morse[letter], end='')

def encode_morse_code():
    value = input("Enter a string of text: ")
    value = value.upper()
    morse_code = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
                    'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
                    'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----',
                    '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ':' ' }
    for letter in value:
        print(morse_code[letter], end='')

def main():
    while True:
        print("\n1. Decode Morse Code")
        print("2. Encode Morse Code")
        print("3. Exit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            decode_morse_code()
        elif choice == '2':
            encode_morse_code()
        elif choice == '3':
            break
        else:
            print("\nInvalid choice!\n")

if __name__ == '__main__':
    main()
    