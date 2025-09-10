
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(word,shift):
    new_word =""
    for letter in word:
        #print(alphabet.index(letter))
        shifted_index =alphabet.index(letter) + shift

        shifted_index = shifted_index % len(alphabet)
        new_letter = alphabet[shifted_index]

        new_word+=(new_letter)
    print(new_word)

def decrypt(word,shift):
    new_word =""
    for letter in word:
        #print(alphabet.index(letter))
        shifted_index =alphabet.index(letter) - shift

        shifted_index = shifted_index % len(alphabet)
        new_letter = alphabet[shifted_index]

        new_word+=(new_letter)
    print(new_word)


def caesar(word,shift,encode_or_decode):
    new_word =""
    if encode_or_decode == "decode":
        shift *= -1
    for letter in word:
        #print(alphabet.index(letter))


        shifted_index =alphabet.index(letter) + shift

        shifted_index = shifted_index % len(alphabet)
        new_letter = alphabet[shifted_index]

        new_word+=(new_letter)
    print(new_word)

encrypt(word = "aaa", shift=3)
decrypt(word = "aaa", shift=3)
direction = input("decode/encode")
word = input("What word?")
shift = input("What shift?")

caesar(word = word, shift=shift,encode_or_decode=direction)
