#hafta 11 odev 1#
#class rehber#

import random 

class cep():

  def __init__(self,marka,model,yil,no,rehber=[]):#ortak ozellikler#
    self.marka=marka
    self.model=model
    self.yil=yil
    self.no=no
    self.rehber=[]

  def ekle(self,ad,no):#ilk parametre herzaman self#
    self.rehber.append([ad,no])
    print("rehbere eklenen:   ",ad,no)

  def sil(self,ad):
    for i in self.rehber:
      if i[0]==ad:
        self.rehber.pop(self.rehber.index(i))#ilk eleman isme esit oldugunda rehber icindeki bolumden kaldiriyoruz#
        print(*i, "kisisi rehberden silinmistir")

  def bastir(self):
    for i in self.rehber:
      print(*i)

  def bul(self,isim):
    for i in self.rehber:
         print(i[0], " araniyor...")
         if i[0]==isim:
             print(i[0], "bulundu")
         
      

tel1= cep("samsung","J7","2009","216 565 2061")  #olusturgumuz objeyi class a esitliyoruz#
tel2=cep("iphone","s5","2014","985 55 66 ")  #parantez icin fonksiyon parametresi kadar eleman ekliyoruz, rehber ayrica belirtildigi icin parntez icinde gerek yoktur#
tel1.ekle("Emrah","1907 19 07")
tel1.ekle("Bro","123 45 67")
tel1.ekle("Kayinco","57 22 00")
tel1.sil("Bro")
tel1.bastir()
tel1.bul("Emrah")
tel1.bul("superman")
