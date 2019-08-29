from time import sleep
class Telefon:


    # try:

    marka='RTS'
    def __init__(self,model,uretim_yili,tel_no):
        self.model=model
        self.uretim_yili=uretim_yili
        self.tel_no=tel_no
        self.rehber={}
# instance methot olarak telefon ozelliklerini aliyoruz ve rehber adli
#sozlgumu burada olsturdum

    def goruntuleme(self):
        for x, y in self.rehber.items():
            print(f'{x}={y}')
#goruntuleme fonksiyonu ile ileride rehberin her goruntulenmesi
#durumunda kullanmak icin olusturduk
    def kontrol(self,isim):
        self.isim=isim
        if self.isim in self.rehber.keys():
            print('Ayni isimde birden fazla kayit yapilamaz!')
#kontrol fonksiyonumuz girilen bir isimin rehberde olup
#olmama durumunu inceliyor
    def ekleme(self,isim,numara):
        self.isim=isim
        self.numara=numara
        self.kontrol(self.isim)
        self.rehber[self.isim]=self.numara
        print('Rehberiniz :')
        self.goruntuleme()
        sleep(1)
#ekleme fonksiyonu ile rehbere yeni isim ve numaralari
#ekledik bunu yapmadan once yukaridaki kontrol fonksiyonunu kullandik
    def silme(self,isim):
        self.isim=isim
        if self.isim in self.rehber.keys():
            del self.rehber[self.isim]
            print(f'{self.isim} siliniyor...')
        else:
            print('Bu isimde bir kayit bulunamadi!')
        sleep(1)
#rehberde ki bir ismi del ile sildik olmamasi durumunda hata
#mesajini veriyor
    def arama(self,isim):
        self.isim=isim
        if self.kontrol(self.isim) :
            print(f'{self.isim} araniyor ...')
            sleep(2)
        else:
            print(f'{self.isim} adli kayit bulunamadi !')
            sleep(1)
#gostermelik olarak rehberde kayitli bir kisiyi ariyor
#bu fonksiyonlarimin tamamini kapsayan bir try except
#olusturmak istedim fakat olmadi her fonksiyonada
#tek tek yazmadim bu ileride degistirelebilir
    # except NameError:
    #     print('Lutfen fonksiyon girislerinde ipuclari bolumune bakiniz')

x=Telefon('x1',2019,456846)
x.ekleme('ali',546846)
x.ekleme('vel',5454)
x.ekleme('cd',545)
x.ekleme('ali',54546)



