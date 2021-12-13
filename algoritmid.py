def FCFS(jarjend): 
    valjund = []
    counter = 1
    järg = 0
    kogu_ooteaeg = 0
    # paneb protsesse vajalikku järjekorda
    for p in jarjend:
        saabumine = p[0]
        kestus = p[1]
        if saabumine > (järg):
                # kui kahe protsessi vahel on "auk", siis jäetakse sinna delay näitamiseks õige pikkusega tühik
                valjund.append([" ", saabumine-järg])
                valjund.append(["P" + str(counter), kestus])
                järg = saabumine + kestus
                counter+=1
        else:
            # vaatab, kui kaua konkreetne protsess oma järge ootas
            if saabumine < järg:
                kogu_ooteaeg += järg - saabumine
            # väljundlisti kirjutatakse protsess koos nime ja kestusega
            valjund.append(["P" + str(counter), kestus])
            järg += kestus
            counter += 1
    # arvutan keskmise ooteaja
    keskm_ooteaeg = round(kogu_ooteaeg / len(jarjend), 2)
    return (valjund, keskm_ooteaeg)


#shortest job next: iga kord valitakse lühima pikkusega töö
def SJF(järjend): # 0 = saabumine, 1 = kestus, 2 = indeks, 3 = tehtud

    #indeks
    u = 1
    indeks = 0
    while indeks < len(järjend):
        järjend[indeks].append(u)
        u+=1
        indeks+=1
    #lisame "tehtud" välja
    indeks = 0
    while indeks < len(järjend):
        järjend[indeks].append(0)
        indeks+=1

    väljund = []
    vaadeldavad = [] # siia paneme vaadeldavad protsessid
    kogu_ooteaeg = 0
    protsesse_kokku = len(järjend)

    protsessi_indeks = 1 #iga protsessi 3. atribuut
    
    protsessist_läbitud = 0
    paus_counter = 0
    i = 0
    while i < 50: #takthaaval

        j  = 0
        while j<len(järjend): #leiame protsessid, mida hetkel vaatleme (mis on saabunud)
            if(järjend[j][0] == i):
                vaadeldavad.append(järjend[j]) ##kui protsess saabub ajal i (või saabub varem), lisame vaadeldavate hulka
            j+=1
        
        if len(vaadeldavad) != 0 and paus_counter != 0:
            #print(paus_counter, "paus")
            väljund.append([" ", paus_counter])
            #print(väljund)
            paus_counter = 0

        m = 0
        while m < len(vaadeldavad):
           
            if vaadeldavad[m][1] - vaadeldavad[m][3] == 0:
                väljund.append(["P" + str(vaadeldavad[m][2]), vaadeldavad[m][3]])
                #print("väljund",väljund)
                #print(väljund, vaadeldavad)
                if vaadeldavad[m][2] == protsessi_indeks:
                    protsessist_läbitud = 0
                    
                del vaadeldavad[m]
                protsessi_indeks +=1
                if len(vaadeldavad) != 0:
                    protsessi_indeks = vaadeldavad[0][2]
                m-=1
            m+=1

        #leiame, mitmendat elementi hetkel käsitleme
        k = 0
        while k < len(vaadeldavad):
           
            if vaadeldavad[k][2] == protsessi_indeks:
                break #jätame selle k meelde, see on "vaadeldavates" protsessi indeks
            k+=1

        if len(vaadeldavad) == 1:
            k = 0
        #kas vaadeldava protsessi kestvusest on lühema kestvusega protsessi?
        if len(vaadeldavad) != 0:
            if vaadeldavad[k][3] == 0:
                f = 0
                while f < len(vaadeldavad):
                    # kui *protsess vaadedavates* on võimalik kiiremini täita kui *vaadeldav protsess*

                    if (vaadeldavad[f][1] - vaadeldavad[f][3]) < vaadeldavad[k][1] - vaadeldavad[k][3]:

                        #break #jätame meelde, kus lühim protsess asub
                        if protsessist_läbitud != 0 : #kui oleme eelmist protsessi juba x takti täitnud
                            
                            väljund.append(["P"+str(vaadeldavad[k][2]), protsessist_läbitud])

                        protsessi_indeks = vaadeldavad[f][2]
                        k = f

                    f+=1
            #läbime 1 takti hetkel vaadelvadat protsessi
        if len(vaadeldavad) != 0: #kui meil on protsesse
            vaadeldavad[k][3] += 1
            
            if len(vaadeldavad) > 1:
                kogu_ooteaeg += 1
            protsessist_läbitud +=1

        else:
            paus_counter += 1

        i+=1
    return [väljund, round(kogu_ooteaeg / protsesse_kokku, 2)]


def RR3(järjend):
    return [["P"], 69]

def FCFS2(järjend):
    return [["P"], 69]