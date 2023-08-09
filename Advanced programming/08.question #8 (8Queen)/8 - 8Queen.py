"In barname baraye gharar dadan N vazir dar yek safheye N*N shatranj be goneyi ke hich kodam hamdigar ra tahdid nakonand neveshte shode ast."\
    """
    harekat vazir dar shatranj bala, payin, chap, rast va zarb dari ast.            
    
     ========================= |Nahveye kar barname| =========================
     *dar in barname az nahveye backtrack estefade shode
     az chaptarin soton va avalin satr shoro be harekat mikonim va khane hara barasi mikonim age
      tahdidi nabod vazir ro gharar midim mirim satr bad dobare az avalin soton dar satr badd harekat mikonim va khoneyi ke tahdid
      nadashte bashe vazir ro dar on gharar midim agar be soton akhar residim va natonestim to hich khoneyi gharar bedim yek satr
      be aghab barmigardim va vazir ro dar on satr yek khone be jolo mibarim alabate age natonim dar on satr ham in karo bokonim va vazir tavashot
      vazir haye satr ghabl tahdid beshe baz ye satr miyaym aghab va vazir on satr ro dar sorat emkan mibarim yek soton be jolo ta vaghti ke hameye
      vazir ha dar khoneyi gharar begiran ke dige hich vaziri onaro tahdid nakone
      $$$ TAVAJOH : dar har sattr fght ye vazir mitone gharar begire
    """
def chessboard(n):
    "mohasebe safheye N*N shatranj ke hame ozv hayash 0 ast"\
    "fght N ra az user be onan vorodi migirad "
    b = []
    for i in range(n):
        for j in range(n):
            b.append(0)
            if j == n-1:
                a.append(b)
                b = []
while True: # halgeye binahayat baraye tekrar barname
    while True: # halgeye binahayat baraye in ke az barname kharej shavad ya edame dahad
        e = input("If you want to Continue type 'C' and then press enter if you want to Exit the programm type 'E' and then press enter : ")
        if e == 'E' or e == 'e':# agar E ya e vared kard az barname kharej sho
            exit(0)
        if e == 'C' or e == 'c':# age C ya c zad barname ro edame bede va az in halghe kharej sho
            break
        elif e != 'C' or e != 'c' or e == int:# age add ya har characteri be gheyr az C ya c vared kard payam zir ra nomayesh bede
                print("********Payattention please type 'E' or 'C' Not anything else********")

    while True:# halgeye binahayat baraye try except ke agar user add vared nakard
        try:
            while True:
                n = int(input("Please Enter the chessboard size : ")) #agar user add vared kard az halghe kharej sho va edame bede
                "Agar user 2 ya 3 ra be onvan andaze safhe shatranj vared kard payam haye zir ra omyaesh bede chon dar in halat emkan pazir nistand"
                if n == 2:
                   print(
                        "This mode is impossible And there is no way to put two Queen Such a way that Do not threaten eachother")
                if n == 3:
                    print(
                        "This mode is impossible And there is no way to put three Queen Such a way that Do not threaten eachother")
                elif n != 2 and n != 3:# agar input 2 ya 3 nabood az halghe kharej sho
                    break
            break
        except:# agar user add vared nakard payam zir ra nomayesh bede
            print("Please enter a number :)")

    a = []
    chessboard(n) # tabe chessborad ra seda mizam ta safheye shatranj ra ijad konad ( hame ozv hayash 0 ast )
    x = 0
    y = 0
    k = 0
    i = 0 # satr
    j = 0 # soton
    while i < n : # halheye asli baraye entexab khane harekat bar roye khane ha be shekl satri
        while i < n: # halheye asli baraye entexab khane harekat bar roye khane ha be shekl satri
            for jc in range(j,n): # tashkhis vojod Queen dar soton mored nazar
                for ic in range (0,n): # tashkhis vojod Queen dar soton mored nazar
                    if a[ic][jc] != 0: # agar dar soton Queen vojod dasht be K ezafe konad va break konad ta j + 1 shavad va yek soton be jolo beravad
                        k = k + 1
                        break
                if k != 0: # baraye raftan yek soton be jolo dar haman satr bayad be J ke dar halgeye asli ast yek vahed ezafe shavad pas bayad az halgheye fari khaerj shod
                    k = 0
                    break
                else:
                    iminusGA = i #harekat i dar ghotr asli be samt bala
                    jminusGA = j #harekat j dar ghotr asli be samt aghab
                    while iminusGA >= 1 and jminusGA >= 1 and iminusGA >= 1 and jminusGA >= 1:# harekat dar gotr asli be samt "bala" ta vaghti ke i ya j be sefr beresad
                            iminusGA = iminusGA - 1
                            jminusGA = jminusGA - 1
                            if a[iminusGA][jminusGA] != 0: # agar dar gotr asli be samt "bala" harekat kard va Queeni vojod dasht bayad yek soton be jolo beravad
                                k = k + 1
                                break
                if k != 0: # baraye raftan yek soton be jolo dar haman satr bayad be J ke dar halgeye asli ast yek vahed ezafe shavad
                    k = 0
                    break

                else:
                    iplusGA = i #harekat i dar ghotr asli be samt payin
                    jplusGA = j #harekat j dar ghotr asli be samt jolo
                    while iplusGA <= n - 2 and jplusGA <= 1  : # harekat dar gotr asli be samt "payin" ta vaghti ke i ya j be n beresad
                                iplusGA = iplusGA + 1
                                jplusGA = jplusGA + 1
                                if a[iplusGA][jplusGA] != 0:  # agar dar gotr asli be samt "payin" harekat kard va Queeni vojod dasht bayad yek soton be jolo beravad
                                    k = k + 1
                                    break

                if k != 0: # baraye raftan yek soton be jolo dar haman satr bayad be J ke dar halgeye asli ast yek vahed ezafe shavad
                    k = 0
                    break
                else:
                    iplusGF = i #harekat i dar ghotr fari be samt payin-chap(be samt i bishtar)
                    jminusGF = j #harekat j dar ghotr fari be samt aghab
                    while iplusGF <= n - 2 and jminusGF >= 1 and iplusGF >= 1 and jminusGF >= 1: # harekat dar gotr fari be samt "payin" ta vaghti ke ya i be n bersad ya j be 0
                        if i == 0 or j == 0:
                            break
                        iplusGF = iplusGF + 1
                        jminusGF = jminusGF - 1
                        if a[iplusGF][jminusGF] != 0: # agar dar gotr fari be samt "payin" harekat kard va Queeni vojod dasht bayad yek soton be jolo beravad
                            k = k + 1
                            break
                if k != 0: # baraye raftan yek soton be jolo dar haman satr bayad be J ke dar halgeye asli ast yek vahed ezafe shavad
                    k = 0
                    break

                else:
                    iminusGF = i #harekat i dar ghotr fari be samt bala-rast(be samt i kamtar)
                    jplusGF = j   # harekat j da gotr fari be samt jelo
                    while iminusGF >= 1 and jplusGF <= n - 2 and iminusGF >= 1 :# harekat dar gotr fari be samt "bala" ta vaghti ke ya i be 0 bersad ya j be n
                        if i == 0 and j == 0:
                            break
                        iminusGF = iminusGF - 1
                        jplusGF = jplusGF + 1
                        if a[iminusGF][jplusGF] != 0:# agar dar gotr fari be samt "bala" harekat kard va Queeni vojod dasht bayad yek soton be jolo beravad
                            k = k + 1
                            break

                if k != 0: # baraye raftan yek soton be jolo dar haman satr bayad be J ke dar halgeye asli ast yek vahed ezafe shavad
                    k = 0
                    break

                else:
                    a[i][j] = 1 # agar hich kodam az shart haye bala nashod pas khane safe ast va Queen ra dar haman khane a[i][j] gharar bede
                break
            if a[i][j] == 1: # agar Queen chap shod boro be satr baad va az avalin soton shoro be harekat kon
                i = i + 1
                j = 0
                break
            else:# agar Queen chap nashod boro be soton baad dar hamn satr va khaneye jadid ra check bokon
                j = j + 1

            if j > n - 1:# agar be soton akhar dar haman satr residi bargard aghab va vazir satr ghabl ra yek soton be jolo harekat bede dar haman satr
                i = i - 1 # bargasht be satr aghab
                y = i + 1
                for i in range(i,y): # baraye harekat dar satr i (y = i + 1 --> agar i = 1 bashad y = 2 mishavad va fght bar royr satr ghabli ke mored nazar ast harekat mikonad
                    for j in range(0,n):# in halghe baraye harekat bar roye soton dar satr i ast
                        if a[i][j] == 1:# Queen ra peyda mikonad va be jayash 0 gharar midahad
                            "soton Queen dar motaghayer 'x' zaxire mishavad ta soton badi dar haman satr barasi shavad ke mitavan Queen ra yek khane be jolo bord ya na" \
                            "agar in kar ra nemikardin az avalin soton harekat ra aghaz mikard va Queen ra dar haman khaneyi ke vojod dasht dobare gharar midad"
                            x = j
                            a[i][j] = 0
                j = 0
                j = x + 1
                x = 0
                while j >= n:# agar dobare besoton akhar residim yek bar digar be aghab bargard ta vaghti ke niyaz ast
                    i = i - 1
                    y = i + 1
                    for i in range(i, y):
                        for j in range(0, n):
                            if a[i][j] == 1:
                                x = j
                                a[i][j] = 0
                    j = 0
                    j = x + 1
                    x = 0

    "halghe haye zir Queen hara ke meghdareshan 1 ast ra peyda mikonan va be jaye on Q gharar midahand "
    for i in range(0,n):# 2 halgheye for baraye harekat bar rooye ozv haye list a neveshte shode ta 1 hara ba |Q va 0 hara ba |_ ja be ja konad
        for j in range(0,n):
            if a[i][j] == 1:# agar meghdar 1 bood pas Queen ast va 1 ra ba |Q avaz kon
                str(a[i][j])
                a[i][j] = "|Q"
            if a[i][j] == 0:# agar 0 bood pas be jaye 0 |_ ra gharar bede
                str(a[i][j])
                a[i][j] = "|_"
            print(end = str(a[i][j]))
            print(end=(" "))
            if j == n - 1: # agar be akharin soton residi boro satr baad
                print()
                break
    print("=======================================================")

