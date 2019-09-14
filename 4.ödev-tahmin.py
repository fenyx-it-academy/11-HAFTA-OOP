dhakkı=5
sayı=6
while dhakkı>0:
    tahmin=int(input("lütfen 1 ile 10 arasında bir sayı giriniz"))
    if tahmin!=sayı:
        dhakkı=dhakkı-1
        print("bilemediniz kalan tahmin hakkınız{}".format(dhakkı))
    elif tahmin==sayı:
        if dhakkı==5:
            print("tebrikler *** kazandınız")
            break
        elif dhakkı==4 or dhakkı==3:
            print("tebrikler ** kazandınız")
            break
        elif dhakkı==2 or dhakkı==1:
            print("tebrikler * kazandınız")
            break
