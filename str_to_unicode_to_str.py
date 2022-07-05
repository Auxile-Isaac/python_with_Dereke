# ask for the word to be converted

word = input("Enter the word to be converted: ")
# word = word.upper()
chr_code = ""
unicode = ""
# converting
for i in word:
    unicode += str(ord(i))
    print(unicode, end="")
    # chr_code += chr(int(unicode))

print(chr_code, end="")
