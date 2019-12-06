def caesarCipher(s, k):
    result = ''
    for i in range(len(s)):
        char = s[i]
        if 65<=ord(char)<=90:
            result += chr((ord(char) + k-65) % 26 + 65)
        elif 97<=ord(char)<=122:
            result += chr((ord(char) + k - 97) % 26 + 97)
        else:
            result += char
    return result
s = input('Enter the Statement')
k = int(input('Enter the number of rotation'))
print (caesarCipher(s, k))
