# tehtud Sten-Oliver Salumaa LIFO näidise põhjal
# FCFS
# protsesse ei katkestata
def FCFS(jarjend):   
    valjund = []
    loendur = 1
    järg = 0
    ooteaeg = 0

    # protsesside järjendi täitmine
    for i in jarjend:
        saabumine = i[0]
        kestus = i[1]

        if saabumine > (järg):
                # kui kahe protsessi vahele jääb paus, siis pannakse sinna n-ö "tühi" protsess
                valjund.append([" ", saabumine-järg])
                valjund.append(["P" + str(loendur), kestus])
                järg = saabumine + kestus
                loendur+=1
        else:
            # vaatab, kui kaua käsitletav protsess oma järge ootas
            if saabumine < järg:
                ooteaeg += järg - saabumine
            # väljundlisti kirjutatakse protsess koos nime ja kestusega
            valjund.append(["P" + str(loendur), kestus])
            järg += kestus
            loendur += 1
    # arvutan keskmise ooteaja
    keskmine_ooteaeg = round(ooteaeg / len(jarjend), 2)
    return (valjund, keskmine_ooteaeg)

# Väljutatõrjuv SJF (lühend: SRTF)
# kui saabub väiksema protsessoriajasooviga protsess, siis käimas olev katkestatakse
# kui saabub protsess, mille kestus on identne juba käiva protsessiga, eelistatakse käimas olevat protsessi
def SJF(jarjend):
    #print(jarjend)
    ooteajad = []
    valjund = []
    protsessid = []
    aktiivsed = [] # jarjendi indeks, p[4]

    for p in range(len(jarjend)): # 0 algusaeg 1 kestus 2 protsessoriaega järel 3 lõpetamisaeg 4 indeks
        protsessid.append([jarjend[p][0], jarjend[p][1], jarjend[p][1], 0, p+1])
        ooteajad.append(0)
    #print(protsessid)

    def find_shortest_active():
        shortest_time = 100
        indeks = []

        for p in protsessid:
            if p[2] < shortest_time and p[4] in aktiivsed:
                shortest_time = p[2]

        for p in protsessid:
            if p[2] == shortest_time and p[4] in aktiivsed:
                indeks.append(p[4])

        indeks.sort()
        return indeks[0]


    for i in range(50):
        #print("AJAHETK: " + str(i))

        for p in range(len(protsessid)): # lisame aktiivseid protsesse
            #print("PROTSESS " + str(p+1))

            if protsessid[p][2] != 0: # käib, kui protsessoriaeg pole nulli jooksnud

                if protsessid[p][0] == i and protsessid[p][4] not in aktiivsed: # lisa aktiivsete hulka, kui praegune ajamoment on protsessi algusaeg ja see pole juba aktiivne
                    #print("P" + str(protsessid[p][4]) + " lisatud aktiivsete hulka")
                    aktiivsed.append(protsessid[p][4])
                      
    
        if len(aktiivsed) > 0:
            #print("AKTIIVSED: " + str(aktiivsed))
            #print("P" + str(find_shortest_active()) + " oli lühim ning jookseb")
            protsessid[find_shortest_active() - 1][2] = protsessid[find_shortest_active() - 1][2] - 1
            #print("PROTSESSIL " + str(find_shortest_active()) + " jäi aega alles " + str(protsessid[find_shortest_active() - 1][2]) + " sekundit")
            valjund.append(["P" + str(find_shortest_active()), 1])

            if protsessid[find_shortest_active() - 1][2] == 0:
                #print("P" + str(find_shortest_active()) + " protsessoriaeg jõudis nulli ning eemaldati aktiivsete hulgast")
                protsessid[find_shortest_active() - 1][3] = i+1
                protsessid[find_shortest_active() - 1][2] = 0
                aktiivsed.remove(find_shortest_active())
        else:
            #print("protsesse ei jooksnud, lisame pausi")
            valjund.append([" ", 1])

                
    # arvutan ooteajad ning selle põhjal keskmise ooteaja
    keskmine_ooteaeg = 0
    for i in range(len(protsessid)):
        ooteajad[i] = protsessid[i][3] - (protsessid[i][1] + protsessid[i][0])
        keskmine_ooteaeg = keskmine_ooteaeg + ooteajad[i]
    keskmine_ooteaeg = round(keskmine_ooteaeg / len(protsessid), 2)

    #print(protsessid)
    #print("keskmine ooteaeg " + str(keskmine_ooteaeg))
    return [valjund, keskmine_ooteaeg]

# RR ajakvandi pikkusega 3 (lühend RR3)
# RR realiseerimisel täidame igal ajahetkel uued saabuvad protsessid alati enne kui järjekorda kogunenud vanad
# protsessid (enne täidame kõik selleks hetkeks saabunud uued protsessid saabumise järjekorras ja alles siis
# hakkame vanade protsesside järgmisi ajakvante täitma, ehk siis vanad lähevad pärast töötamist oma uue
# ajakvandi saamiseks "järjekorra lõppu").
def RR3(jarjend):
    #print(jarjend)
    ajahetk = 0
    ooteajad = []
    valjund = []
    protsessid = []
    aktiivsed = []
    jarjekord = [] # jarjendi indeks, p[4]

    for p in range(len(jarjend)): # 0 algusaeg 1 kestus 2 protsessoriaega järel 3 lõpetamisaeg 4 indeks
        protsessid.append([jarjend[p][0], jarjend[p][1], jarjend[p][1], 0, p+1])
        ooteajad.append(0)
    #print(protsessid)

    while ajahetk < 50:
        kestus = 0
        #print("AJAHETK: " + str(ajahetk))

        for p in range(len(protsessid)): # lisame aktiivseid protsesse
            #print("PROTSESS " + str(p+1))

            if protsessid[p][2] != 0: # käib, kui protsessoriaeg pole nulli jooksnud

                if protsessid[p][0] == ajahetk and protsessid[p][4] not in aktiivsed: # lisa aktiivsete hulka, kui praegune ajamoment on protsessi algusaeg ja see pole juba aktiivne
                    #print("P" + str(protsessid[p][4]) + " lisatud aktiivsete hulka")
                    aktiivsed.append(protsessid[p][4])

                    if protsessid[p][2] >= 3:
                        kestus = 3
                    else:
                        kestus = protsessid[p][2]

                    for x in range(kestus):
                        jarjekord.append(protsessid[p][4])
                    
                    break
        
        if len(jarjekord) > 0:
            #print("JÄRJEKORD: " + str(jarjekord))           
            #print("P" + str(jarjekord[0]) + " oli järjekorras esimene ning jookseb")
            protsessid[jarjekord[0] - 1][2] = protsessid[jarjekord[0] - 1][2] - 1
            #print("PROTSESSIL " + str(jarjekord[0]) + " jäi aega alles " + str(protsessid[jarjekord[0] - 1][2]) + " sekundit")
            valjund.append(["P" + str(protsessid[jarjekord[0] - 1][4]), 1])


            if protsessid[jarjekord[0] - 1][2] == 0:
                #print("P" + str(jarjekord[0]) + " protsessoriaeg jõudis nulli ning eemaldati aktiivsete hulgast")
                protsessid[jarjekord[0] - 1][3] = ajahetk + 1
                protsessid[jarjekord[0] - 1][2] = 0
                aktiivsed.remove(jarjekord[0])
                
            jarjekord.pop(0)
        else:
            k = 0

            if len(aktiivsed) == 0:
                #print("protsesse ei jooksnud, lisame pausi")
                valjund.append([" ", 1])
            else:
                #print("järjekord on tühi, kuid aktiivseid on")
                #print("AKTIIVSED: " + str(aktiivsed))
                aktiivsed.sort

                if len(aktiivsed) > 1 and int(valjund[-1][0].replace('P', '')) == aktiivsed[0]: # vältimaks, et sama protsess saab üle 3 sekundi käia, kui on teisigi aktiivseid protsesse
                    k = aktiivsed[0]
                    aktiivsed.pop(0)

                if protsessid[aktiivsed[0] - 1][2] >= 3:
                        kestus = 3
                else:
                    kestus = protsessid[aktiivsed[0] - 1][2]

                for x in range(kestus):
                    jarjekord.append(protsessid[aktiivsed[0] - 1][4])

                #print("JÄRJEKORD: " + str(jarjekord))           
                #print("P" + str(jarjekord[0]) + " oli järjekorras esimene ning jookseb")
                protsessid[jarjekord[0] - 1][2] = protsessid[jarjekord[0] - 1][2] - 1
                #print("PROTSESSIL " + str(jarjekord[0]) + " jäi aega alles " + str(protsessid[jarjekord[0] - 1][2]) + " sekundit")
                valjund.append(["P" + str(protsessid[jarjekord[0] - 1][4]), 1])


                if protsessid[jarjekord[0] - 1][2] == 0:
                    #print("P" + str(jarjekord[0]) + " protsessoriaeg jõudis nulli ning eemaldati aktiivsete hulgast")
                    protsessid[jarjekord[0] - 1][3] = ajahetk + 1
                    protsessid[jarjekord[0] - 1][2] = 0
                    aktiivsed.remove(jarjekord[0])
                
                jarjekord.pop(0)
                if k != 0:
                    aktiivsed.append(k)
        
        ajahetk = ajahetk + 1

    # arvutan ooteajad ning selle põhjal keskmise ooteaja
    keskmine_ooteaeg = 0
    for i in range(len(protsessid)):
        ooteajad[i] = protsessid[i][3] - (protsessid[i][1] + protsessid[i][0])
        keskmine_ooteaeg = keskmine_ooteaeg + ooteajad[i]
    keskmine_ooteaeg = round(keskmine_ooteaeg / len(protsessid), 2)


    #print(protsessid)
    #print("keskmine ooteaeg " + str(keskmine_ooteaeg))
    return [valjund, keskmine_ooteaeg]

# Kahe prioriteediga FCFS (two-level FCFS scheduling)
# Kui protsessi kestus on <=3 ajaühikut, pannakse protsess kõrge prioriteediga FCFS järjekorda, kõik üle 3 ühiku kestusega madalasse FCFS järjekorda.
# madala prioriteetsusega FCFS järjekorda täidetakse ainult siis, kui kõrge prioriteediga protsesse ootejärjekorras pole
# Kui saabub kõrge prioriteegiga töö katkestatakse madala prioriteediga järjekorra täitmine (protsess) (erinev klassikalisest FCFS algoritmist).
def FCFS2(jarjend):
    #print(jarjend)
    high = []
    low = []
    ooteajad = []
    valjund = []
    protsessid = []
    aktiivne = 100 # aktiivse protsessi indeks indeks, p[4]

    for p in range(len(jarjend)): # 0 algusaeg 1 kestus 2 protsessoriaega järel 3 lõpetamisaeg 4 indeks
        protsessid.append([jarjend[p][0], jarjend[p][1], jarjend[p][1], 0, p+1])
        ooteajad.append(0)

    for ajahetk in range(50):
        breaker = False
        #print("AJAHETK: " + str(ajahetk))

        for p in range(len(protsessid)): # lisame aktiivseid protsesse
            #print("PROTSESS " + str(p+1))

            if protsessid[p][2] != 0: # käib, kui protsessoriaeg pole nulli jooksnud

                if protsessid[p][0] == ajahetk: # lisan prtosessi õigesse listi
                    if protsessid[p][1] <= 3 and protsessid[p][4] not in high:
                        #print("P" + str(protsessid[p][4]) + " lisatud HIGH hulka")
                        aktiivne = protsessid[p][4]
                        breaker = True # suurema prioriteediga protsess katkestab madalama
                        high.append(protsessid[p][4])
                    else:
                        if protsessid[p][4] not in low:
                            #print("P" + str(protsessid[p][4]) + " lisatud LOW hulka")
                            low.append(protsessid[p][4])
                    
                    break

        
        if len(high) > 0 or len(low) > 0:
            muudetav = 0
            #print("HIGH: " + str(high))
            #print("LOW: " + str(low))

            if len(high) > 0:
                muudetav = high[0]
            else:
                muudetav = low[0]

                if breaker:
                    muudetav = aktiivne

            #print("P" + str(muudetav) + " oli prioriteedi järgi esimene ning jookseb")
            protsessid[muudetav - 1][2] = protsessid[muudetav - 1][2] - 1
            #print("PROTSESSIL " + str(muudetav) + " jäi aega alles " + str(protsessid[muudetav - 1][2]) + " sekundit")
            valjund.append(["P" + str(protsessid[muudetav - 1][4]), 1])

            if protsessid[muudetav - 1][2] <= 3 and protsessid[muudetav - 1][4] not in high:
                high.append(protsessid[muudetav - 1][4])

                if protsessid[muudetav - 1][4] in low:
                    low.remove(protsessid[muudetav - 1][4])
            elif protsessid[muudetav - 1][2] == 0:
                #print("P" + str(muudetav) + " protsessoriaeg jõudis nulli ning eemaldati aktiivsete hulgast")

                if protsessid[muudetav - 1][4] in low:
                    low.remove(protsessid[muudetav - 1][4])
                if protsessid[muudetav - 1][4] in high:
                    high.remove(protsessid[muudetav - 1][4])

                protsessid[muudetav - 1][3] = ajahetk + 1
                protsessid[muudetav - 1][2] = 0               
        else:
            #print("protsesse ei jooksnud, lisame pausi")
            valjund.append([" ", 1])

    # arvutan ooteajad ning selle põhjal keskmise ooteaja
    keskmine_ooteaeg = 0
    for i in range(len(protsessid)):
        ooteajad[i] = protsessid[i][3] - (protsessid[i][1] + protsessid[i][0])
        keskmine_ooteaeg = keskmine_ooteaeg + ooteajad[i]
    keskmine_ooteaeg = round(keskmine_ooteaeg / len(protsessid), 2)

    #print(protsessid)
    #print("keskmine ooteaeg " + str(keskmine_ooteaeg))
    return [valjund, keskmine_ooteaeg]

#FCFS([[1,10],[3,3],[4,1],[8,6],[15,2]])
#SJF([[1,10],[3,3],[4,1],[8,6],[15,2]])
#RR3([[1,10],[3,3],[4,1],[8,6],[15,2]])
#FCFS2([[1,10],[3,3],[4,1],[8,6],[15,2]])