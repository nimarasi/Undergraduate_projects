A = 31 #rooz haye mah haye farvardin ta shahrivar
B = 30 #rooz haye mah haye mehr ta bahman
E = 29 #tedat rooz esfand

print("--------------Read Below--------------")
print("Loftan baraye entexab mahe mored nazar az kilid vajhe haye zir estefade konid : ")
print("F = farvardin",' |','O = Ordibehesht',' |','Kh = Khordad',' |','T = Tir',' |','Mo = Mordad',' |','Sh = Shahrivar')
print("Me = Mehr",' |','Ab = Aban',' |','Az = Azar',' |','D = dey',' |','B = Bahman',' |','E = Esfand')
a = input("lotfan mahe mored nazar ra entexab konid : ")
if a == 'F' or a == 'O' or a == 'Kh' or a == 'T' or a == 'Mo' or a == 'Sh' :
    print("Tedad rooz mahe entexabi shoma barabar ast ba : ",A)

if a == 'Me' or a == 'Ab' or a == 'Az' or a == 'D' or a == 'B':
    print("Tedad rooz mahe entexabi shoma barabar ast ba : ",B)

if a == 'E':
    print("Tedad rooz mahe entexabi shoma barabar ast ba : ", E)