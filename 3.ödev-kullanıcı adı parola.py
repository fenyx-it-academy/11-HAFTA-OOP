while True:
    kadı=input("3-18 karakter aralığında kullanıcı adı giriniz:")
    if len(kadı)>18 or len(kadı)<3:
        print("lütfen istenen karakter aralığında kullanıcı adı giriniz.")
    elif ("0" in kadı) or ("1" in kadı) or ("2" in kadı) or ("3" in kadı) or ("4" in kadı) or ("5" in kadı) or ("6" in kadı) or ("7" in kadı) or ("8" in kadı) or ("9" in kadı):
        print("lütfen rakam kullanmayınız")
    elif len(kadı)<=18 and len(kadı)>=3:
        print("kullanıcı adınız",kadı)
        break
while True:
    parola=input("lütfen6-12 karakter uzunluğunda parola giriniz")
    if len(parola)>12 or len(parola)<6:
        print("lütfen istenen karakter aralığında parola giriniz")
    elif len(parola)<=12 and len(parola)>=6:
        print("parolanız",parola)
        break
f=open("giriş_bilgi.txt","w")
print("kullanıcı adı:",kadı,"\nparola:",parola,file=f)
f.close()

