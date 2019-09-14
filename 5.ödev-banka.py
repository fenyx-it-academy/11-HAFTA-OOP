kullanıcı_bakiye=1000
menü=("""
(1) bakiye kontrolü
(2) para yatırma
(3) para çekme
(4) çıkış
""")
print(menü)
soru=input("yapmak isyediğiniz işlemin numarasını giriniz=")
akif=1
while akif==1:
    if soru=="1":
        print("bakiyenizde=",kullanıcı_bakiye,"£ bulunmaktadır.")
        soru=input("yapmak istediğiniz işlemin numarasını giriniz=")
    elif soru=="2":
        pyatırma=int(input("lütfen yatırmak istediğiniz tutarı giriniz="))
        kullanıcı_bakiye=kullanıcı_bakiye+pyatırma
        print("para hesabınıza yatırılmıştır.mevcut bakiyeniz=",kullanıcı_bakiye)
        soru=input("yapmak isyediğiniz işlemin numarasını giriniz=")
    elif soru=="3":
        pçekme=int(input("lütfen çekmek istediğiniz tutarı giriniz"))
        if pçekme>kullanıcı_bakiye:
            print("bakiyenizde bulunan miktardan fazla para çekemezsiniz.")
            soru=input("yapmak isyediğiniz işlemin numarasını giriniz=")
        else:
            kullanıcı_bakiye=kullanıcı_bakiye-pçekme
            print("mevcut bakiyeniz=",kullanıcı_bakiye)
            soru=input("yapmak isyediğiniz işlemin numarasını giriniz=")
    elif soru==4:
        print("bizi seçtiğiniz için teşekkür ederiz lütfen kartınızı almayı unutmayı iyi günler.")
        akif==2
    else:
        print("lütfen menüde bulunan işlemleri seçiniz")
        soru=input("yapmak isyediğiniz işlemin numarasını giriniz=")
    

   
