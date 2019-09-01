'''Bir cep telefonu objesi yapmanizi istiyoruz.
~~Telefonun marka, model, uretim yili, tel nosu ve rehber gibi obje ozelliklerinin(instance attributes) olmasini bekliyoruz.

Ayrica bu objenin :
~~rehbere no ekleme, silme, rehberi goruntuleme, rehberden secilen bir noyu arama(gostermelik)
gibi ozelliklerinin olmasini istiyoruz.'''

import time

class Telefon():
    telefon_listesi=[]

    def __init__(self,tel_isim='isimsiz',tel_marka='marka belirlenmemis',tel_model='model belirlenmemis',uretim_yili=2010,imei=123456):
        self.tel_isim=tel_isim
        self.tel_marka =tel_marka
        self.tel_model = tel_model
        self.uretim_yili = uretim_yili
        self.imei = imei

        self.rehber_isimler=[]
        self.rehber_numaralar=[]
        self.telefon_rehberi = []

    def telefon_kaydi(self):
        while True:
            cihaz_ad=input("cihaza bir isim giriniz(cihaz1 gibi):")
            if cihaz_ad=="q" or cihaz_ad=='':
                print("bos veya q disinda bir ad giriniz")
            elif cihaz_ad in Telefon.telefon_listesi:
                print("bu isimde bir telefon zaten kayitli.yeni bir isim seciniz")
            else:
                Telefon.telefon_listesi.append(cihaz_ad)
                cihaz_marka = input(f"{cihaz_ad} nin markasini giriniz:")
                cihaz_model = input(f"{cihaz_ad} nin modelini giriniz:")
                cihaz_uretimyil = input(f"{cihaz_ad} nin uretim yilini giriniz:")
                cihaz_imei = input(f"{cihaz_ad} nin imei numarasini giriniz:")
                self.tel_isim = cihaz_ad
                self.tel_marka = cihaz_marka
                self.tel_model = cihaz_model
                self.uretim_yili = cihaz_uretimyil
                self.imei = cihaz_imei
                print("Kayit yapiliyor...")
                time.sleep(2)
                print("""
                {} isimli telefonun:
                    Markasi:        {},
                    Modeli:         {},
                    Uretim Yili:    {},
                    Imei No:        {}
                olarak kaydedildi.
                """.format(cihaz_ad, cihaz_marka, cihaz_model, cihaz_uretimyil, cihaz_imei))
                break
    def tel_rehbergor(self):
        print("Telefon rehberi goruntuleniyor...")
        time.sleep(2)
        for i in range(len(self.telefon_rehberi)):
            print(self.telefon_rehberi[i])


    def no_ekle(self,isim,numara):
        veri= isim+":"+numara
        print('Kaydediliyor..')
        self.rehber_isimler.append(isim)
        self.rehber_numaralar.append(numara)
        self.telefon_rehberi.append(veri)
        time.sleep(1)
        print(f'{veri} telefon rehberine eklenmistir')

    def yeni_kayitkontrol(self,isim):
            while True:
                print("""bu kisi daha once kaydedilmistir
                                   (1)     Varolan kisinin numarasini degistir
                                   (2)     anamenu""")
                tercih = input("isleminizi giriniz:")
                if tercih not in ("1","2"):
                    print("Gecerli islem numarasi girilmedi.Tekrar deneyiniz")

                elif tercih=="2":
                    return False
                elif tercih=="1":
                    a=list(i for i in range(len(self.rehber_isimler)) if (self.rehber_isimler)[i]==isim )
                    #isimlerden olusan listenin eleman sayisi kadar i yi dondur
                    #girilen isim isimler listesindeyse kacinci sirada
                    #bu listede 1 eleman bulunur.bu ismin index numarasini verir

                    numara=input("yeni numarayi giriniz:")

                    self.rehber_numaralar[a[0]]=numara
                    #isimler listesinde ismin indeksi a[0] ise bu kisinin numarasinin numara listesindeki yeri a[0]dir

                    print("{} kisinin numarasi {} olarak degistirildi".format(isim,numara))
                    return False

    def anamenu(self):
        print('''
           1   Yeni kayit/numara degistirme
           2   Telefon numarasi sorma
           3   Telefon Rehberine Git
           4   Kisi silme
           q   cikis''')
        return input("Yapmak istediginiz islemi girin:")  # kullanici islem yapmak istemezse

    def rehber(self):
        while True:
            anamenu = Telefon.anamenu(self)
            if anamenu == "q":
                break
            elif anamenu not in ("1", "2", "3", "4"):
                print("Gecerli islem numarasi girilmedi.Tekrar deneyiniz")
            elif anamenu == "3":
                Telefon.tel_rehbergor(self)
            elif anamenu == "1":
                isim = input("yeni kisi eklemek icin isim giriniz:")
                if isim in self.rehber_isimler:
                    Telefon.yeni_kayitkontrol(self, isim)
                else:
                    numara = input("Telefon numarasi:")
                    Telefon.no_ekle(self, isim, numara)
            elif anamenu=="2":
                sorgu=input("numarasini ogrenmek istediginiz kisinin adini giriniz:")
                if sorgu in self.rehber_isimler:
                    a=list(i for i in range(len(self.rehber_isimler)) if self.rehber_isimler[i] == sorgu)
                    telnumara=self.rehber_numaralar[a[0]]
                    print(f"""
        {sorgu} isimli kisinin telefon numarasi:
        {telnumara}""")
                else:
                    print("Var olmayan kisi sorgusu.")
            else:
                sorgu = input("numarasini silmek istediginiz kisinin adini giriniz:")
                if sorgu in self.rehber_isimler:
                    a = list(i for i in range(len(self.rehber_isimler)) if self.rehber_isimler[i] == sorgu)
                    telnumara = self.rehber_numaralar[a[0]]
                    self.rehber_isimler.remove(sorgu)
                    self.rehber_numaralar.remove(telnumara)
                    self.telefon_rehberi.remove(f"{sorgu}:{telnumara}")
                    print(f"""
                {sorgu}:{telnumara} kaydi silindi""")



cihaz1=Telefon()
cihaz2=Telefon()
cihaz3=Telefon()
c4=Telefon()
c5=Telefon()
c6=Telefon()
c7=Telefon()
#simdilik 7 telefon kaydedecek yer olusturduk.bunu otomatik olarak nasil yapacagimi hala bilmiyorum.
#for dongusuyle bir listenin ustunden gidemiyorum.listenin elemanlari string oldugu icin kabul etmiyor
telefonlar=[cihaz1,cihaz2,cihaz3,c4,c5,c6,c7]




while True:
    print("Burada birkac telefon ve bunlarin telefon rehberlerini olusturmaktasiniz")
    print("Kayitli cihazlar:")
    print(list(Telefon.telefon_listesi))
    print("""
    (1)  yeni cihaz ekle
    (2)  varolan cihazin rehberine git
    (q)  cikis
    """)
    tercih = input("Islem numarasi:")
    if tercih == 'q':
        break
    elif tercih not in ("1", "2"):
        print("gecersiz islem numarasi")
    else:
        if tercih == "1":
            sira = len(Telefon.telefon_listesi)
            # telefon_listesinde kac tane eleman varsayeni eklenecek cihaz icin sira +1
            # fakat index icin -1 yapilacagi icin ayni sayi kullanilir

            Telefon.telefon_kaydi(telefonlar[sira])
            # telefonlar listesindeki kayitli olan telefonlarin ozelliklerini, telefon ekledikce yeniliyor

        elif tercih == '2':
            while True:
                print("Kayitli cihazlar:")
                print(list(Telefon.telefon_listesi))
                cihaz = input("Rehberine gitmek istedigin cihazin ismini gir. (cikis icin q)")
                if cihaz=="q":
                    break
                elif cihaz not in Telefon.telefon_listesi:
                    print("bu isimde bir cihaz kayitli degil.tekrar deneyiniz")
                else:

                    for i in range(len(Telefon.telefon_listesi)):
                        if Telefon.telefon_listesi[i]==cihaz: #telefon listesi kullanicinin gordugu cihaz isimleri
                            chz=telefonlar[i]               #telefonlar ,Telefon classina kayitli objectler listesi
                            Telefon.rehber(chz)
                            print("""
                                            {} isimli telefonun:
                                                Markasi:        {},
                                                Modeli:         {},
                                                Uretim Yili:    {},
                                                Imei No:        {}
                                            olarak kaydedildi.
                                            """.format(cihaz, chz.tel_marka, chz.tel_model, chz.uretim_yili, chz.imei))
                            print("{} cihazinin anamenusune yonlendiriliyorsunuz...".format(cihaz))












