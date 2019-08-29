from random import randint
from time import sleep
class Muzik_calar():
#classimiin icine butun fonsiyonlarin ulasabilmesi icin init de listemizi olusturduk
# ve listeden istenilen sarkinin calinabilmesini saglmasi icin sayacimizi da burada olusturduk

    def __init__(self):
        self.muzik_list=[]
        self.sira = 0
    def ekleme(self,parca_adi):
        self.parca_adi=parca_adi
        self.muzik_list.append(parca_adi)
        sleep(1)
        print('Guncel listeniz :')
        self.goruntule()
# ekleme fonksiyonu ile listemize parcalari ekledik
#burda kullanicidan sinirsiz sayida parca girebilmesi icin
# *args yapmayi  dusunduk fakat bunu liste icinde tup olarak
#olusturdugu icin basarili olamadik
    def silme(self,parca_adi):
        self.parca_adi=parca_adi
        self.yer=self.muzik_list.index(parca_adi)
        del self.muzik_list[self.yer]
        sleep(2)
        self.goruntule()
#kullanicinin silmek istedigi parca adini aldik ve bunu listenen
#kaldirdiktan sinra kullaniciya guncel listeyi gosterdik
    def goruntule(self):
        self.sayac=0
        for i in self.muzik_list :
            print(self.sayac+1,*i,sep='')
            self.sayac+=1
        sleep(3)
#listemizi her goruntulemek istedigimizde fonksiyonu dongu kurmamak icin
#bu fonksiyonu kurduk
    def temizleme(self):
        self.muzik_list.clear()
        print('Listeniz silindi !')
        sleep(2)

    def istek_parca(self):
        self.goruntule()
        self.istek=int(input('Calmasini istediginiz parcayi numarasini giriniz :'))
        print(f'{self.muzik_list[self.istek-1]} parcasi oynatiliyor...')
        sleep(2)
#istek parca fonksiyonu kullanicidan parcanin sira numarasini alarak
#ona gore lstedeki parcayi ekrana getiriyor
    def parca_cal(self):
        print(f'{self.muzik_list[self.sira]} parcasi oynatilyor...')
        self.sira+=1
#bu fonksiyon en son kalinan parcayi caliyor program ilk acildiginda
#devreye girebilir
    def siradaki_parca(self):
        self.sira+=1
        print(f'{self.muzik_list[self.sira]},parcasi oynatiliyor...')
        sleep(2)
#kullanicinin siradaki parcaya gecmesini sagliyoruz
#ve bi onceki parcaya gecmesini sagliyoruz
    def onceki_parca(self):
        self.sira-=1
        print(f'{self.muzik_list[self.sira]} parcasi caliniyor...')
        sleep(2)
    def karisik(self):
        self.karisik=randint(1,len(self.muzik_list))
        print(f'{self.muzik_list[self.karisik-1]} parcasi caliniyor...')
        sleep(2)
#karisik fonksiyonunda randint yardimiyla listeden rasgele bi
#parcanin calinmasini sagliyoruz



# x=Muzik_calar()
# x.ekleme('Kum gibi')
# x.ekleme('Islak Islak')
# x.ekleme('Duurt Te Lang')
# x.ekleme('Leef')
# # x.goruntule()
# # x.parca_cal()
# # x.siradaki_parca()
# x.onceki_parca()
# x.karisik()
# x.istek_parca()
print(dir(Muzik_calar))