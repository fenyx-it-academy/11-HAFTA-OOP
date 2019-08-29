
#Programi direk calistirip deneyebilirsiniz..

import time

class telefon():
    def __init__(self,marka,model,uretim_yili,tel_no):
        self.marka = marka
        self.model = model
        self.uretim_yili = uretim_yili
        self.rehber = tel_no


    def rehber_goruntuleme(self):
        print("Rehber Goruntuleniyor ..")
        time.sleep(2)
        print("""
        Rehber Numaralari\n
        {}
        """.format(self.rehber))

    def NoEkleme(self,ekleneceknumara):
        print("Numara Ekleniyor...")
        time.sleep(2)
        self.rehber.append(ekleneceknumara)

    def NoSilme(self, silineceknumara):
        print("Numara siliniyor...")
        time.sleep(2)
        self.rehber.remove(silineceknumara)

    def NoArama(self):      #parantez icine aranacak no deyip te de olabilir..
        print("""
                Rehber Numaralari\n
                {}
                """.format(self.rehber))
        secim = int(input("Lutfen aramak istediginiz telefonun sira numarasini giriniz :"))
        print("""
        {} numarali telefon araniyor...""".format(self.rehber[secim-1]))
        time.sleep(2)

#Asagidaki kodlarin hepsini ayni anda aktif hale getirip programi deneyebilirsiniz..

nokia3310 = telefon("nokia",3310,2015,["063443433"])    #Ornekleme yaptik

nokia3310.NoEkleme("024243343")

nokia3310.rehber_goruntuleme()

nokia3310.NoSilme("024243343")

nokia3310.rehber_goruntuleme()

nokia3310.NoArama()

