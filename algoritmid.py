def massiiviks(input_jarjend):
    valjund = []
    jupid = input_jarjend.split(";")
    for i in range(len(jupid)):
        hakkliha = jupid[i].split(",")
        saabumine = int(hakkliha[0])
        kestus = int(hakkliha[1])
        valjund.append([saabumine, kestus])
    return valjund

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
    print(jarjend)
    ooteajad = []
    valjund = []
    protsessid = []
    aktiivsed = [] # jarjendi indeks, P(x)

    for p in range(len(jarjend)): # 0 algusaeg 1 kestus 2 protsessoriaega järel 3 lõpetamisaeg 4 indeks
        protsessid.append([jarjend[p][0], jarjend[p][1], jarjend[p][1], 0, p+1])
        ooteajad.append(0)
    print(protsessid)

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
        # print("find_shortest_active() SISU: " + str(indeks))
        return indeks[0]


    for i in range(50):
        print("AJAHETK: " + str(i))

        for p in range(len(protsessid)): # lisame aktiivseid protsesse
            print("PROTSESS " + str(p+1))

            if protsessid[p][2] != 0: # käib, kui protsessoriaeg pole nulli jooksnud

                if protsessid[p][0] == i and protsessid[p][4] not in aktiivsed: # lisa aktiivsete hulka, kui praegune ajamoment on suurem kui protsessi algusaeg ja see pole juba aktiivne
                    print("P" + str(protsessid[p][4]) + " lisatud aktiivsete hulka")
                    aktiivsed.append(protsessid[p][4])
                      
    
        if len(aktiivsed) > 0:
            print("AKTIIVSED: " + str(aktiivsed))
            print("P" + str(find_shortest_active()) + " oli lühim ning jookseb")
            protsessid[find_shortest_active() - 1][2] = protsessid[find_shortest_active() - 1][2] - 1
            print("PROTSESSIL " + str(find_shortest_active()) + " jäi aega alles " + str(protsessid[find_shortest_active() - 1][2]) + " sekundit")
            valjund.append(["P" + str(find_shortest_active()), 1])

            if protsessid[find_shortest_active() - 1][2] == 0:
                # print("AKTIIVSED: " + str(aktiivsed))
                print("P" + str(find_shortest_active()) + " protsessoriaeg jõudis nulli ning eemaldati aktiivsete hulgast")
                protsessid[find_shortest_active() - 1][3] = i+1
                protsessid[find_shortest_active() - 1][2] = 0
                aktiivsed.remove(find_shortest_active())
        else:
            print("protsesse ei jooksnud, lisame pausi")
            valjund.append([" ", 1])

                
    # arvutan ooteajad ning selle põhjal keskmise ooteaja
    keskmine_ooteaeg = 0
    for i in range(len(protsessid)):
        ooteajad[i] = protsessid[i][3] - (protsessid[i][1] + protsessid[i][0])
        keskmine_ooteaeg = keskmine_ooteaeg + ooteajad[i]
    keskmine_ooteaeg = round(keskmine_ooteaeg / len(protsessid), 2)

    print(protsessid)
    print("keskmine ooteaeg " + str(keskmine_ooteaeg))
    return [valjund, keskmine_ooteaeg]





SJF(massiiviks("1,10;3,3;4,1;8,6;15,2"))


aktiivsed = [16,3,6,9,2,34,65,7]














def RR3(jarjend):
    return [["P"], 69]

def FCFS2(jarjend):
    return [["P"], 69]