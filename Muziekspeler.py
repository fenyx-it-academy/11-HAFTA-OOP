from time import sleep
import random
class Muziekspeler:
    # muzik calar classı tanımlama
    def __init__(self):
        self.muziek_lijst = {1:['faruk','ozturk',3.50],2:['a','b',2.3],3:['d','e',3.4],4:['f','g',4.5]}
        # müzik listesi
    def bekijk_lijst(self):
        # müzik listesi goruntuleme modulu
        for i in range(len(self.muziek_lijst)):
            # liste uzunlugunca dongu ve verilerin listelenmesi
            print(i+1,*self.muziek_lijst[i+1],sep='.')

    def lied_toevoegen(self):
        # listeye sarkı ekleme
        self.lied=input('Voer de naam van het lied in.')
        # sarkı ismi
        self.zanger=input('Voer de naam van het zanger in.')
        # sarkıcı ismi
        self.tijd=input('Voer de tijd van het lied in.')
        # sarkı suresi
        self.no=len(self.muziek_lijst)+1
        # sarkı numarası
        self.muziek_lijst[self.no]=[self.lied, self.zanger, self.tijd]
        # sozluk tipi veri olan muzık listesine verileri ekleme
        print(f'{self.lied} en {self.zanger} zijn toegevoegd aan deze lijst.')

    def lied_verwijderen(self):
        # listeden sarkı silme modulu
        self.lied_nummer=int(input('Voer het nummer in het lied dat u wilt verwijderen.'))
        # silinecek sarkının numarasını kullanıcıdan alma
        self.muziek_lijst.pop(self.lied_nummer,'U heeft een verkeerd nummer ingevoerd')
        # sozluk seklındeki müzik listesinden pop metodu ile sarkıyı silme

    def lijst_verwijderen(self):
        # listeyi tamamen sileme modulu
        self.muziek_lijst.clear()
        # clear metodu ile listeyi bosaltma
        print('De muzieklijst is volledig verwijderd')

    def lied_spelen(self):
        # müzik calma modulu
        self.y=input('Druk op 1 om achtereenvolgens naar lied te luisteren of 2 om willekeurig af te spelen.')
        #  sarkıları sırasıyla dinlemek icin 1 ,karısık dinlemek icin 2 ye basınız
        if self.y=='1':
            self.achtereenvolgens()
            # sırayla sarkıları calma modulunu calıstırma
        elif self.y=='2':
            self.willekeurig()
            # karısık calma modulu
        else:
            print('U hebt verkeerd ingevoerd')

    def achtereenvolgens(self):
        # sırayla sarkıları calma modulu
        for self.i in range(len(self.muziek_lijst)):
            # liste uzunlugunca dongu
            print(self.i + 1, *self.muziek_lijst[self.i + 1],' speelt')
            # sozluk degerleri olan sarkı bilgilerini ekrana yazdırma
            sleep(3)
            self.x = input('''Druk op 1 voor het volgende lied,
            druk op 2 voor het vorige lied,
            druk op ENTER om door te gaan.''')
            # bir sonraki sarkı icin 1 e, bir onceki sarkı icin 2 ye,sarkıyı dınlemeye devam etmek icin enter a basınız
            if self.x=='1':
                self.volgende_lied()
                # sıradakı sarkı calma modulunu calıstırma
            elif self.x=='2':
                self.vorige_lied()
                # bir onceki sarkıyı dinleme modulu
            else:
                sleep(2)

    def willekeurig(self):
        # sarkıları karısık dinleme modulu
        print(*random.choice(self.muziek_lijst.values()),' speelt')

    def volgende_lied(self,):
        # bir sonrakı sarkıyı calma modulu
        self.i+=1

    def vorige_lied(self):
        # bir onceki sarkıyı calma modulu
        self.i-=1

lied1=Muziekspeler()
lied1.lied_spelen()
# instance atama ve programı baslatma








