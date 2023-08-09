a = '          abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$%^&*()_+=-}{[]|"";/\><.,'
o = 1
print("======== Password Encryptor & Decryptor ========")
print(" ********** README.TXT = \*"
      "In encryption The number part is hash if you want to decrypt you have to write number parts to decrypt./")
while True:
    print(
        "If you want to Ecrytp a text press 1 and enter. \nif you want to Decrypt Hash to a text press 2 and enter.  \nIf you want to end program press 0 and enter.")
    x = int(input("\nPlease enter your choice : "))
    if x == 0:
        break
    if x == 1:
            b = input("Please write a string : ")
            c = ''
            d = 0
            for i in b:
                for j in a:
                    d = a.find(i)
                    if d == 0:
                        d = '01'
                    d = str(d)
                    c = c + d
                    break
            print("Encryption = $$%a",end=c) , print('$')
            print("\n\*********************************************/")

    if x == 2:
        k = -1
        y = ''
        z =''
        b = input("Please enter numbers : ")
        c = len(b)//2
        for i in range(0,c) :
            y = b[0:2]
            b = b[2:]
            y = int(y)
            for i in a:
                k = k + 1
                if k == y:
                    if k == '01':
                        z = z + ' '
                    z = z + i
                    k = -1
                    break
        print("Decryption = ",end=z)
        print("\n\*********************************************/")
