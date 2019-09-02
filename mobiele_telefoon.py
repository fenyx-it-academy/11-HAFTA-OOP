# coding=utf-8
class mobiele_telefoon:
    # sınıf tanımlama
    def __init__(self):
        # class attribute tanımlama
        self.merk=''
        # telefon markası
        self.model=''
        # telefon modeli
        self.productiejaar=''
        # telefon üretim yılı
        self.telefoon_nr=''
        # telefon numarası
        self.telefoonboek={}
        # telefon rehberi-sözlük

    def telefon_gebruikersinformatie(self):
        self.merk = input('Typ uw telefoonmerk.')
        # telefon markası
        self.model = input('Typ uw telefoonmodel.')
        # telefon modeli
        self.productiejaar = input('Typ het productiejaar uw telefoon.')
        # telefon üretim yılı
        self.telefoon_nr = input('Typ uw telefoon nummer.')
    def toevoegen(self):
        # rehbere isim-no ekleme modülü
        self.naam=input('Typ de naam.')
        self.nr=input('Typ de nummer.')
        self.telefoonboek[self.naam]=self.nr

    def verwijderen(self):
        # rehberden veri silme modlü        l
        self.naam=input('Typ de naam om te verwijderen.')
        self.telefoonboek.pop(self.naam,'De informatie die u wilt verwijderen, staat niet in de contacten.')
        # pop metodu ile veri silme,silinecek veri listede yoksa uyarı verme

    def bekijken(self):
        # telefon listesini gorüntüleme
        for sleutel,waarde in self.telefoonboek.items():
            # anahtar ve deger icin sozlükte dongu
            print(f"{sleutel} = {waarde}")
            # isim ve numaranın ekrana yazdırılması

    def bellen(self):
        #arama modulu
        self.naam=input('Typ de naam om te bellen.')
        # aranacak isim girisi
        if self.naam in self.telefoonboek:
            # girilen ismin telefon rehberinde aranması
            print(f'{self.naam} {self.telefoonboek[self.naam]} bellen...')
        else:
            print('De naam die u wilt bellen, staat niet in de contacten.')

t1=mobiele_telefoon()
t1.bellen()
# instance atama ve programı calıstırma