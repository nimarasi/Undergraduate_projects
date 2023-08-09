def Hanoitower (n , A , B , C): # jabe ja kardan disc az A be C ba estefade az B
    if n == 1:
        print("Move disc 1 from " ,end=str(A)),print(end=" to "),print(end=str(C))
    else:
        Hanoitower(n-1,A , C , B)# jabe ja kardan disc az A be B ba estefade az C
        print()
        print("Move disc ",end=str(n)),print(" from ",end=str( A)),print(end=" to "),print(str(C))
        Hanoitower(n-1,B,A,C)# jabe ja kardan disc az B be C ba estefade az A

print("========== Hanoi Tower ==========")
while True:
    n = int(input("please enter number of disc: "))
    Hanoitower(n,'A','B','C')
    print("\nIf you want to countinue press any button else press 0 to exit from programm")
    a = int(input("please choose to continue or to exit : "))
    if a == 0:
        print("Good Luck")
        break
    print("-----------------------------")

