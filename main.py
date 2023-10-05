from morse_translation import translation_dict

word = input("Enter the word you would like to translate to morse code: ").upper()

word_in_morse = ""

for letter in word:
    letter_in_morse = translation_dict.get(letter)
    word_in_morse = word_in_morse + " " + letter_in_morse
print(f"Translation to morse code: {word_in_morse}