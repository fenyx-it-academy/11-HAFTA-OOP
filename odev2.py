#hafta 11 odev 2#
#muzik listesi#


import random

class walkman():
    
  liste=[]
  def cal(self,sarki):
    if sarki in self.liste:
      print(sarki,"yurutuluyor..")
    else:
      print("Malesef repertuvarimizda mevcut degil")

  def temizle(self):
    self.liste.clear()
    print("yurutme listesi bos")
  def goruntule(self):
    print("Sarkilar:\n")
    for i in self.liste:
      print(i)
  def ekle(self,sarki):
    self.liste.append(sarki)
    print(sarki,"eklendi iyi dinlemeler..\n\n")
  def sil(self,sarki):
    self.liste.pop(self.liste.index(sarki))
    print(sarki,"listeden kaldirildi\n")
  def sonraki(self,sarki):
    x=self.liste.index(sarki)
    print("Bir sonraki parcamiz:  ")
    print(self.liste[x+1],"caliniyor...")
  def onceki(self,sarki):
    x=self.liste.index(sarki)
    print("onceki sarkimiz: \n")
    print(self.liste[x-1], "caliniyor...")
  def karisik(self):
    karisik=random.randint(0,len(self.liste))
    print(self.liste[karisik], "Caliniyor..")


repertuvar= walkman()
repertuvar.ekle("Sagopa-366. gun")
repertuvar.ekle("Hayko Cepkin-Gelin olmus")
repertuvar.ekle("Duman-Eski koprunun altinda")
repertuvar.ekle("Cem karaca-kara sevda")
repertuvar.ekle("Tarkan-Yolla")

repertuvar.goruntule()
repertuvar.sil("Hayko Cepkin-Gelin olmus")
repertuvar.sonraki("Duman-Eski koprunun altinda")
repertuvar.onceki("Sagopa-366. gun")
repertuvar.karisik() 
repertuvar.temizle()
