with open('multiline.txt', 'r') as file:
    lines = file.readlines()
lines[0] = lines[0].upper()
lines[1] = ' '.join(word[::-1].capitalize() for word in lines[1].split())
lines[2] = lines[2].replace(' ', '@').replace('a', '$').replace('e', '$').replace('i', '$').replace('o', '$').replace('u', '$')
lines[3] = lines[3].lower()
with open('multiline.txt', 'w') as file:
    file.writelines(lines)
    
white_count = 0
digit_count = 0
symbol_count = 0
char_count = 0

for char in lines:
    if char.isspace():
        white_count += 1
    elif char.isdigit():
        digit_count += 1
    elif not char.isalnum():
        symbol_count += 1
    char_count += 1
    
print(f"Total characters: {char_count}")
print(f"Total white spaces: {white_count}")
print(f"Total digits: {digit_count}")
print(f"Total symbols: {symbol_count}")

