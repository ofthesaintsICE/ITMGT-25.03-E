'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shift_letter(letter, shift):
    if letter == ' ':
        return letter
    return alphabet[(alphabet.find(letter) + shift) % 26]

def caesar_cipher(message, shift):
    ciphertext = ''
    for i in message:
        ciphertext += shift_letter(i, shift)
    return ciphertext

def shift_by_letter(letter, letter_shift):
    if letter == ' ':
        return letter
    return alphabet[(alphabet.find(letter) + alphabet.find(letter_shift)) % 26]

def vigenere_cipher(message, key):
    key_index = 0
    
    ciphertext = ''
    for i in message:
        ciphertext += shift_by_letter(i, key[key_index % len(key)])
        key_index += 1
    return ciphertext

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += '_' 
    
    ciphertext = ''
    for i in range(len(message)):
        ciphertext += message[(i // shift) + (len(message) // shift) * (i % shift)]
    
    return ciphertext

def scytale_decipher(message, shift):
    decoded_text = ''

    for i in range(len(message)):
        decoded_text += message[(i % (len(message) // shift)) * shift + (i // (len(message) // shift))]

    return decoded_text