shift = int(input())
text = input().lower()
cipher = ""
for letter in text:
    if letter != ' ':
        cipher += chr((ord(letter) - shift - 97) % 26 + 97)
    else:
        cipher += letter

print(cipher)