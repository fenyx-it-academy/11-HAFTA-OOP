hesap=("""
(1) km-mil hesabı
(2) mil-km hesabı
""")
print(hesap)
yazıcı=1
while yazıcı==1:
    soru=input("yapmak istediğiniz işlemin numarasını giriniz=(çıkmak için q)")
    if soru=="q":
        print("sistemden çıkılıyor...")
        yazıcı=0
    elif soru=="1":
        km=int(input("km'yi mile dönüştürmek için mesafeyi giriniz=."))
        print(km,"=",km*0.62137,"mil yapmaktadır.")
    elif soru=="2":
        mil=int(input("mil'i km' ye dönüştürmek için mesafeyi giriniz="))
        print(mil,"=",mil/0.62137,"km yapmaktadır.")
    elif soru=="3":
        çıkış=input("çıkış yapmak istiyorsanız q 'ye basınız...")
        print(çıkış,"programdan çıkıyorsunuz...")
        
