import random
def tablo(a):      #10 x 10 a listesi  ekrana bastırılır
    satırayır=[[str(i+1),"\t"]+a[i]+["\n"] for i in range (0,10)]
    satır=["".join(satırayır[i]) for i in range(10)]
    print("\n",*satır,"\t 1  2  3  4  5  6   7  8  9  10","\n")
    print(puan)
    return

def gemi1yer(DoluAlan):
    while True:
        x = (random.randint(0, 9), random.randint(0, 9))
        if x in DoluAlan:
            continue
        else:
            DoluAlan += [x]
            return DoluAlan
            break


def gemi2yer(DoluAlan):
    while True:
        x = (random.randint(0, 9), random.randint(0, 9))
        if x in DoluAlan:
            continue
        else:
            poz = random.choice(["yatay", "dikey"])  # geminin yatay mı dikey mi olacağı rastgele belirleniyor
            if poz == "yatay":
                if (x[0] + 1 in DoluAlan) or (x[0] + 1 > 9):
                    continue
                else:
                    DoluAlan += [x, (x[0] + 1, x[1])]
                    return DoluAlan
                    break
            if poz == "dikey":
                if (x[1] + 1 in DoluAlan) or (x[0] + 1 > 9):
                    continue
                else:
                    DoluAlan += [x, (x[0], x[1] + 1)]
                    return DoluAlan
                    break


def gemi3yer(DoluAlan):
    while True:
        x = (random.randint(0, 9), random.randint(0, 9))
        if x in DoluAlan:
            continue
        else:
            poz = random.choice(["yatay", "dikey"])  # geminin yatay mı dikey mi olacağı rastgele belirleniyor
            if poz == "yatay":
                if (x[0] + 1 in DoluAlan) or (x[0] + 1 > 9) or (x[0] + 2 in DoluAlan) or (x[0] + 2 > 9):
                    continue
                else:
                    DoluAlan += [x, (x[0] + 1, x[1]), (x[0] + 2, x[1])]
                    return DoluAlan
                    break
            if poz == "dikey":
                if (x[1] + 1 in DoluAlan) or (x[1] + 1 > 9) or (x[1] + 2 in DoluAlan) or (x[1] + 2 > 9):
                    continue
                else:
                    DoluAlan += [x, (x[0], x[1] + 1), (x[0], x[1] + 2)]
                    return DoluAlan
                    break


def gemidortyer(DoluAlan):
    while True:
        x = (random.randint(0, 9), random.randint(0, 9))
        if x in DoluAlan:
            continue
        else:
            poz = random.choice(["yatay", "dikey"])  # geminin yatay mı dikey mi olacağı rastgele belirleniyor
            if poz == "yatay":
                if (x[0] + 1 in DoluAlan) or (x[0] + 1 > 9) or (x[0] + 2 in DoluAlan) or (x[0] + 2 > 9) or (
                        x[0] + 3 in DoluAlan) or (x[0] + 3 > 9):
                    continue
                else:
                    DoluAlan += [x, (x[0] + 1, x[1]), (x[0] + 2, x[1]), (x[0] + 3, x[1])]
                    return DoluAlan
                    break
            if poz == "dikey":
                if (x[1] + 1 in DoluAlan) or (x[1] + 1 > 9) or (x[1] + 2 in DoluAlan) or (x[1] + 2 > 9) or (
                        x[1] + 3 in DoluAlan) or (x[1] + 3 > 9):
                    continue
                else:
                    DoluAlan += [x, (x[0], x[1] + 1), (x[0], x[1] + 2), (x[0], x[1] + 3)]
                    return DoluAlan
                    break
            return


def gemiyerleştir (DoluAlan,boscizgi):  # gemilerin yerlerini gösteren fonksiyon
    for i in DoluAlan:
        dolu = [i[0], i[1]]
        boscizgi[i[1]][i[0]] = " * .|"


def gemigizle(DoluAlan,boscizgi):  # gemilerin yerlerini gizleyen fonksiyon
    for i in DoluAlan:
        boscizgi[i[1]][i[0]] = "__|"

def AtısYap(sırano,satırno,DoluAlan,boscizgi,hak,puan,atısyerleri):
    if [sırano,satırno] not in atısyerleri:  # yapacağımız yer daha önceden atışyaptığımız yer mi diye atışyerleri listesinden kontrol edilir
        print(sırano, ".ncı sıra", satırno, ". ncı satır atışınız")
        if (sırano - 1,satırno - 1) in DoluAlan:  # eğer atış yerimiz dolu alan da ise isabet etmiş demektir. ve puan 1 artar hak 1 azalır x işareti konur
            print("isabet ettiniz")
            boscizgi[satırno - 1][sırano - 1] = "x.|"
            hak -= 1
            tablo(boscizgi)
            print(hak, "  hakkınız kaldı")
            atısyerleri += [[sırano, satırno]]
            puan += 1
        elif (sırano - 1, satırno - 1) not in DoluAlan:
            print("Atış boşa gitti")
            hak -= 1
            boscizgi[satırno - 1][sırano - 1] = " o|"
            atısyerleri += [[sırano, satırno]]
            tablo(boscizgi)
            print(hak, "  hakkınız kaldı")
    else:
        print("Bu noktaya daha önce atış yaptınız..")


print(""" Oyun Başlıyor
*Oyunda çıkmak için 'q' tuşuna,
*Atış yapmak için önce sıra numarası, ardından sütün numarasını aralarına virgül girerek yazınız.
*Gemilerin yerlerini görmek için göster yazın ve enter a basın
*Gemileri gizlemek için gizle yazın ve enter a basın""")


atısyerleri=[]      #bizim atış yaptığımız yerlerin listesi
atısyerleri_bil=[]   #bilgisayarın atış yaptığı yerlerin listesi
puan=0
puan_bil=0
DoluAlan=[]     #gemilerin yerlerinin koordinatlarının olduğu liste
DoluAlan_bil=[]
boscizgi=[["__|" for i in range(10)] for j in range(10)]            #10 arlı 10 adet toplam 100 cizgiden oluşan liste oluşur
boscizgi_bil=[["__|" for i in range(10)] for j in range(10)]

#1,2,3,4 karelik gemiler rastgele sıralanıyor
gemidortyer(DoluAlan)
gemidortyer(DoluAlan)
gemi3yer(DoluAlan)
gemi3yer(DoluAlan)
gemi2yer(DoluAlan)
gemi2yer(DoluAlan)
gemi1yer(DoluAlan)
gemi1yer(DoluAlan)
sıra="x"        #hangi değerin (oyun alanı x-y koordinatı) girileceği ön tanımlanmış
sırano=0    #atış yapacağımız sıra
satırno=0   #atış yapacağımız sütün
sırano_bil=0
satırno_bil=0
hak=15
hak_bil=15
puan=0
puan_bil=0

tablo(boscizgi)  #tablo görüntülenir,, atış yapılınca tabloda isabetli yada isabetsiz atışlar her seferinde yenilenir
tablo(boscizgi_bil)

while hak > 0 and hak_bil > 0:
    if puan == 20:
        print("Tebrikler sen kazandın:)  ")
    if puan_bil == 20:
        print("Bilgisayar kazandı:)  ")
    a = input("")
    if a == "q":
        print("Oyun bitti")
        break
    elif a == "göster" or a == "Göster" or a == "GÖSTER":
        gemiyerleştir(DoluAlan,boscizgi)  # gemilerin hepsi sırayla yerleştirilir..
        tablo(DoluAlan,boscizgi)
        gemiyerleştir(boscizgi_bil)  # gemilerin hepsi sırayla yerleştirilir..
        tablo(DoluAlan_bil,bosciDoluAlan_bil,zgi_bil)
        continue

    elif a == "gizle" or a == "Gizle" or a == "GİZLE":
        gemigizle(DoluAlan,boscizgi)  # gemilerin hepsi sırayla yerleştirilir..
        tablo(DoluAlan,boscizgi)
        gemigizle(DoluAlan_bil,bosciDoluAlan_bil,zgi_bil)  # gemilerin hepsi sırayla yerleştirilir..
        tablo(DoluAlan_bil,bosciDoluAlan_bil,zgi_bil)
        continue
    try:
        if int(a) in range(1, 11):
            if sıra == "x":
                sırano = int(a)
                sıra = "y"
                continue
            else:
                satırno = int(a)
                sıra = "x"
                print("OYUNCU KİŞİ")
                AtısYap(sırano, satırno, DoluAlan, boscizgi,hak,puan,atısyerleri)
                sırano_bil=random.randint(1,10)
                satırno_bil=random.randint(1,10)
                print("OYUNCU BİLGİSAYAR")
                AtısYap(sırano_bil,satırno_bil,DoluAlan_bil,boscizgi_bil,hak_bil,puan_bil,atısyerleri_bil)
                continue
        else:
            print("Lütfen 1-10 aralığında değer giriniz")
            continue
    except ValueError:
        print("Lütfen doğru değer giriniz")
        continue













