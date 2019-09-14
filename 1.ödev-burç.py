print("hangi burç olduğunuzu öğrenmek için bilgilerinizi giriniz...")
dgünü=int(input("lütfen sadece doğduğunuz günün tarihini giriniz:"))
day=input("lütfen doğduğunuz ayı giriniz:")
a=["ocak","şubat","mart","nisan","mayıs","haziran",
   "temmuz","ağustos","eylül","ekim","kasım","aralık"]
if 22<=dgünü<=31 and day==a[11] or 21>=dgünü>=1 and day==a[0]:
    print("burcunuz: oğlak")
elif 22<=dgünü<=31 and day==a[0] or 19>=dgünü>=1 and day==a[1]:
    print("burcunuz: kova")
elif 20<=dgünü<=29 and day==a[1] or 20>=dgünü>=1 and day==a[2]:
    print("burcunuz: balık")
elif 21<=dgünü<31 and day==a[2] or 20>=dgünü>=1 and day==a[3]:
    print("burcunuz: koç")
elif 21<=dgünü<=30 and day==a[3] or 21>=dgünü>=1 and day==a[4]:
    print("burcunuz: boğa")
elif 22<=dgünü<=31 and day==a[4] or 22>=dgünü>=1 and day==a[5]:
    print("burcunuz: ikizler")
elif 23<=dgünü<=30 and day==a[5] or 22>=dgünü>=1 and day==a[6]:
    print("burcunuz: yengeç")
elif 23<=dgünü<=31 and day==a[6] or 22>=dgünü>=1 and day==a[7]:
    print("burcunuz: aslan")
elif 23<=dgünü<=31 and day==a[7] or 22>=dgünü>=1 and day==a[8]:
    print("burcunuz: başak")
elif 23<=dgünü<=30 and day==a[8] or 22>=dgünü>=1 and day==a[9]:
    print("burcunuz: terazi")
elif 23<=dgünü<=31 and day==a[9] or 21>=dgünü>=1 and day==a[10]:
    print("burcunuz: akrep")
elif 22<=dgünü<=30 and day==a[10] or 21>=dgünü>=1 and day==a[11]:
    print("burcunuz: yay")
else:
    print("lütfen bilgilerinizi doğru giriniz...")
