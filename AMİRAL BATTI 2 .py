import random

def tablo(a):      #10 x 10 boş kareler ekrana bastırılır 
    satırayır=[[str(i+1),"\t"]+a[i]+["\n"] for i in range (0,10)]
    satır=["".join(satırayır[i]) for i in range(10)]
    print("\n"*9,*satır,"\n","\t 1   2   3   4    5    6    7   8   9   10","\n"*4)
    print(puan)
    return 

def gemi1yer(DoluAlan):
            while True:
                x=(random.randint(0,9),random.randint(0,9))
                if x in DoluAlan:
                        continue
                else:
                        DoluAlan+=[x]
                        return DoluAlan
                        break        

def gemi2yer(DoluAlan):
                while True:
                    x=(random.randint(0,9),random.randint(0,9))
                    if x in DoluAlan:
                        continue
                    else:
                            poz=random.choice(["yatay","dikey"])          #geminin yatay mı dikey mi olacağı rastgele belirleniyor
                            if poz=="yatay":
                                if (x[0]+1 in DoluAlan) or (x[0]+1>9):
                                    continue
                                else:
                                    DoluAlan+=[x,(x[0]+1,x[1])]
                                    return DoluAlan
                                    break
                            if poz=="dikey":
                                if (x[1]+1 in DoluAlan) or (x[0]+1 >9):
                                    continue
                                else:
                                   DoluAlan+=[x,(x[0],x[1]+1)]
                                   return DoluAlan
                                   break
                                
def gemi3yer(DoluAlan):
                while True:
                    x=(random.randint(0,9),random.randint(0,9))
                    if x in DoluAlan:
                        continue
                    else:
                            poz=random.choice(["yatay","dikey"])          #geminin yatay mı dikey mi olacağı rastgele belirleniyor
                            if poz=="yatay":
                                if (x[0]+1 in DoluAlan) or (x[0]+1>9) or  (x[0]+2 in DoluAlan) or (x[0]+2>9):
                                    continue
                                else:
                                    DoluAlan+=[x,(x[0]+1,x[1]),(x[0]+2,x[1])]
                                    return DoluAlan
                                    break
                            if poz=="dikey":
                                if (x[1]+1 in DoluAlan) or (x[1]+1>9) or  (x[1]+2 in DoluAlan) or (x[1]+2>9):
                                    continue
                                else:
                                   DoluAlan+=[x,(x[0],x[1]+1),(x[0],x[1]+2)]
                                   return DoluAlan
                                   break
                                
def gemidortyer(DoluAlan):
                while True:
                    x=(random.randint(0,9),random.randint(0,9))
                    if x in DoluAlan:
                        continue
                    else:
                            poz=random.choice(["yatay","dikey"])          #geminin yatay mı dikey mi olacağı rastgele belirleniyor
                            if poz=="yatay":
                                if (x[0]+1 in DoluAlan) or (x[0]+1>9) or  (x[0]+2 in DoluAlan) or (x[0]+2>9) or (x[0]+3 in DoluAlan) or (x[0]+3>9):
                                    continue
                                else:
                                    DoluAlan+=[x,(x[0]+1,x[1]),(x[0]+2,x[1]),(x[0]+3,x[1])]
                                    return DoluAlan
                                    break
                            if poz=="dikey":                   
                                if (x[1]+1 in DoluAlan) or (x[1]+1>9) or  (x[1]+2 in DoluAlan) or (x[1]+2>9)or  (x[1]+3 in DoluAlan) or (x[1]+3>9):
                                    continue
                                else:
                                   DoluAlan+=[x,(x[0],x[1]+1),(x[0],x[1]+2),(x[0],x[1]+3)]
                                   return DoluAlan
                                   break
                            return
                        
def gemiyerleştir(k):       #gemilerin yerlerini gösteren fonksiyon
    for i in DoluAlan:
        dolu=[i[0],i[1]]
        boscizgi[i[1]][i[0]]=" * .|"

def gemigizle(k):           #gemilerin yerlerini gizleyen fonksiyon
    for i in DoluAlan:
        boscizgi[i[1]][i[0]]="__|"
        
print(""" Oyun Başlıyor
*Oyunda çıkmak için 'q' tuşuna,
*Atış yapmak için önce sıra numarası, ardından sütün numarasını girerek ayrı ayrı entera basın
*Gemilerin yerlerini görmek için göster yazın ve enter a basın
*Gemileri gizlemek için gizle yazın ve enter a basın""")


atışyerleri=[]  #atış yapılan koordinatların olduğu liste
puan=0
DoluAlan=[]     #gemilerin yerlerinin koordinatlarının olduğu liste
boscizgi=[["__|" for i in range(10)] for j in range(10)]            #10 arlı 10 adet toplam 100 cizgiden oluşan liste oluşur
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
hak=15

tablo(boscizgi)  #tablo görüntülenir,, atış yapılınca tabloda isabetli yada isabetsiz atışlar her seferinde yenilenir
while hak >0:
    if puan==20:
        print ("Tebrikler KAZANDINIZ ...:)  ")
    a=input("")
    if a =="q":
        print("Oyun bitti")
        break
    elif a=="göster" or a=="Göster" or a=="GÖSTER":
        gemiyerleştir(boscizgi)         #gemilerin hepsi sırayla yerleştirilir..
        tablo(boscizgi)
        continue
    
    elif a=="gizle" or a=="Gizle" or a=="GİZLE":
        gemigizle(boscizgi)         #gemilerin hepsi sırayla yerleştirilir..
        tablo(boscizgi)
        continue
    try:
        if int(a) in range(1,11):
            if sıra=="x":
                sırano=int(a)
                sıra="y"
                continue
            else:
                satırno=int(a)
                sıra="x"
                if [sırano,satırno] not in atışyerleri:
                    print(sırano,".ncı sıra", satırno,". ncı satır atışınız")
                    if (sırano-1,satırno-1) in DoluAlan:
                        print("isabet ettiniz")
                        boscizgi[satırno-1][sırano-1]=" x. |"
                        hak-=1
                        tablo(boscizgi)
                        print(hak,"  hakkınız kaldı")
                        atışyerleri+=[[sırano,satırno]]
                        puan+=1
                        
                        continue
                    elif (sırano-1,satırno-1) not in DoluAlan:
                        print ("Atış boşa gitti")
                        hak-=1
                        boscizgi[satırno-1][sırano-1]=" o |"
                        atışyerleri+=[[sırano,satırno]]
                        tablo(boscizgi)
                        print(hak,"  hakkınız kaldı")
                        continue
                else:
                    print("Bu noktaya daha önce atış yaptınız..")
                    continue
        else:
            print("Lütfen sizden istenilen değeri giriniz")

    except ValueError:
        print("Lütfen sizden istenilen değeri giriniz")
        continue

 
print("\n  Oyun Bitti...\n PUANINIZ  :  ", puan)




    
