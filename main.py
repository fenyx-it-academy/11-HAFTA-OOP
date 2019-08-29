
from Oyun import *
oyuncu1 = Oyuncu()
oyuncu2=Oyuncu()
oyun=Oyun()

oyun.gemileriYerlestir_bilgi()
oyuncu2.gemileriYerlestir(4,2)
oyuncu2.gemileriYerlestir(3,2)
oyuncu2.gemileriYerlestir(2,2)
oyuncu2.gemileriYerlestir(1,2)
print("Rakibiniz icin tablonuzu doldurdurdunuz. \n...SIMDI OYUN ZAMANI...")
oyuncu1.random_gemiyerlestir(4, 2) 
oyuncu1.random_gemiyerlestir(2, 2)
oyuncu1.random_gemiyerlestir(3, 2)
oyuncu1.random_gemiyerlestir(1, 2)

oyun.bilgi()
dogruyanlis=0
sira=0
ihtimaller=[]
while True:
    print("Sizin Tablonuz:")
    oyuncu1.tablo_goster(oyuncu1.tablo)
    print("Rakibinizin Tablosu:")
    oyuncu2.tablo_goster(oyuncu2.tablo)
    if sira%2==0:                            # ciftse sira kullanicida
        print("\n...Sizin Siraniz...\n")
        try:
            satir = int(input("Satir Secimi(1-10):"))
            sutun = input("Sutun Secimi(A-J):").upper()
            if satir > 10 or satir < 1:
                print("Yanlis secim yaptiniz")
                continue
            if not sutun in "ABCDEFGHIJ":
                print("Yanlis secim yaptiniz")
                continue     
        except ValueError:
            print("Yanlis tercih yaptiniz.")
            continue

        sutun_dic = {"A": 1, "B": 2, "C": 3, "D": 4,"E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
        sutun=sutun_dic[sutun]
        if oyuncu1.tablo2[sutun][satir] == "X":     # Yani daha once isaretlenmisse
            print("Daha once bu degeri girmistiniz...")
            continue
        if oyuncu1.tablo2[sutun][satir] == 1 and oyuncu1.tablo[sutun][satir] == 0:
            oyuncu1.tablo[sutun][satir] = "+"
            oyuncu1.vurulan_gemi+=1
            print(oyuncu1.vurulan_gemi, "Gemi vuruldu...")
        if oyuncu1.tablo2[sutun][satir] == 0 and oyuncu1.tablo[sutun][satir] == 0:
            oyuncu1.tablo[sutun][satir] = "X"
            oyuncu1.tablo2[sutun][satir] = "X"
            oyuncu1.hak -= 1
            sira+=1
            print("Yanlis hamle...5 sn bekleyin..")
            if oyuncu1.hak != 0:
                print(oyuncu1.hak, "hakkiniz kaldi...")
            time.sleep(3)

        if oyuncu1.kontroll() == 20:
            print("Tebrikler....Kazandiniz..")
            oyuncu1.cozum_tablosu("...Sizin Cozum Tablonuz...")
            break
        if oyuncu1.hak == 0:
            print("Hakkiniz kalmadi oyunu kaybettiniz...")
            oyuncu1.cozum_tablosu("...Sizin Cozum Tablonuz...")
            break
    elif sira%2==1:
        print("\n...Bilgisayar Oynuyor...\n")
        time.sleep(3)
        satir = random.randint(1,10)
        sutun = random.randint(1,10)
        print("Ihtimaller",ihtimaller)
        if len(ihtimaller)!=0:
            satirsutun=random.sample(ihtimaller,1)
            satir=satirsutun[0][0]
            sutun=satirsutun[0][1]
            ihtimaller.pop(ihtimaller.index(satirsutun[0]))
        if oyuncu2.tablo2[sutun][satir] == "X":  
            continue
        if oyuncu2.tablo2[sutun][satir] == 1 and oyuncu2.tablo[sutun][satir] == 0:
            oyuncu2.tablo[sutun][satir] = "+"
            oyuncu2.vurulan_gemi+=1
            print(oyuncu2.vurulan_gemi,"Bilgisayar bir gemi vurdu...")
            ihtimaller=oyuncu2.ihtimaller(satir,sutun)

        if oyuncu2.tablo2[sutun][satir] == 0 and oyuncu2.tablo[sutun][satir] == 0:
            oyuncu2.tablo[sutun][satir] = "X"
            oyuncu2.tablo2[sutun][satir] = "X"
            oyuncu2.hak -= 1
            dogruyanlis=0
            sira+=1
            if oyuncu2.hak != 0:
                print(oyuncu2.hak, "hakki kaldi...")
        if oyuncu2.kontroll() == 20:
            print("Bilgisayar Kazandi...")
            oyuncu2.cozum_tablosu("...Bilgisayarin Cozum Tablosu...")
            break
        if oyuncu2.hak == 0:
            oyuncu2.cozum_tablosu("...Bilgisayarin Cozum Tablosu...")
            break
if oyuncu2.kontroll() != 20 or oyuncu2.kontroll()!=20:
    print("Oyun berabere bitti.. Kimse tum gemileri vuramadi...")
if oyuncu1.vurulan_gemi>oyuncu2.vurulan_gemi:
    print("Ama sizin vurdugunuz gemi sayisi fazla oldugu icin kazanan olabilirsiniz..:) Tebrikler..")
elif oyuncu2.vurulan_gemi>oyuncu1.vurulan_gemi:
    print("Ama bilgisayarin vurdugu gemi sayisi fazla oldugu icin kazanan olabilir..:)")
