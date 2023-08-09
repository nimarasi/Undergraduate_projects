def reverseStr(a):
    b = []
    k = 0
    for i in a:
        c = a.find('-')
        if i == '-':
            d = a[0:c]
            b.append(d)
            a = a[c + 1:]
            k = k + 1
        if c == -1:
            d = a[:]
            b.append(d)
            a = ''
            k = k + 1
            break
    b.sort()
    for i in range(0, k):
        if i == k-1:
            a = a + b[i]
            break
        else:
            a = a + b[i] + "-"
    return a
print("===== please after writing each word put ((-)) ===== ")
print("Example : white-black-yellow")
a = input("Please write a string : ")
print("First string : ", a)
a = reverseStr(a)
print("second string : ",a)
