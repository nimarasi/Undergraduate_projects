a = input("Please write a text : ")
k = 0
for i in a:
    if (i == 'a' or i == 'A'):
        k = k + 1
    if (i == 'e' or i == 'E'):
        k = k + 1
    if (i == 'i' or i == 'I'):
        k = k + 1
    if (i == 'o' or i == 'O'):
        k = k + 1
    if (i == 'u' or i == 'U'):
        k = k + 1

print("Number of vowels : " , k)