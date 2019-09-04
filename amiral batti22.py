#    ODEV: AMIRAL BATTI

## zamanlamayi calistirmak icin time fonksiyonunu import ediyoruz
from time import sleep
import time
## gemileri farkli duzende yerlestirmek icin random import ediyoruz
import random
print()
print("""Asagidaki tablodan uygun alani secerek yer ismini belirtiyorsunuz,
dogru hamleler 'x' ile yanlis hamleler '-' ile isaretlenecektir. \n""")
print('Her basarili hamlede oyun sirasi sizde kalir.')
print()
sleep(5)

w =   ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10',
       'b1','b2','b3','b4','b5','b6','b7','b8','b9','b10',
       'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10',
       'd1','d2','d3','d4','d5','d6','d7','d8','d9','d10',
       'e1','e2','e3','e4','e5','e6','e7','e8','e9','e10',
       'f1','f2','f3','f4','f5','f6','f7','f8','f9','f10',
       'g1','g2','g3','g4','g5','g6','g7','g8','g9','g10',
       'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10',
       'k1','k2','k3','k4','k5','k6','k7','k8','k9','k10',
       'l1','l2','l3','l4','l5','l6','l7','l8','l9','l10']

print("Gemilerimiz:", "2 tane Amiral (4'lu)", "2 tane Kruvazor (3'lu)", "2 tane Muhrip (2'li)", "2 tane (1'li)",sep='\n')
sleep(5) 
print()
z=[]

havuz1 =   ['','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','']

k = '[x]'
m ='[]'

yasak1 =    ['a8','b8','c8','d8','e8','f8','g8','h8','l8','k8']
yasak2 =    ['a9','b9','c9','d9','e9','f9','g9','h9','l9','k9']
yasak3 =    ['a10','b10','c10','d10','e10','f10','g10','h10','l10','k10']
yasak4 =    ['l8','l9','l10']
yasak5 =    ['h1','h2','h3','h4','h5','h6','h7','h8','h9','h10',
             'k1','k2','k3','k4','k5','k6','k7','k8','k9','k10',
             'l1','l2','l3','l4','l5','l6','l7','l8','l9','l10']

def amiral1():
    global havuz1
    while True:
        secim1 = random.choice(w)
        yer1 = w.index(secim1)
        if secim1 in havuz1:
            secim1 = random.choice(w)
        else:
            break
    if secim1 in yasak4:
        yerd = int(yer1) -5
        havuz1.insert(yerd,(w[yerd]))
        havuz1.insert(yerd+1,w[yerd+1])
        havuz1.insert(yerd+2,w[yerd+2])
        havuz1.insert(yerd+3,w[yerd+3])
    elif secim1 in yasak1: 
        yerd = int(yer1) +3
        havuz1.insert(yerd,(w[yerd]))
        havuz1.insert(yerd+1,w[yerd+1])
        havuz1.insert(yerd+2,w[yerd+2])
        havuz1.insert(yerd+3,w[yerd+3])
    elif secim1 in yasak2:
        yerd = int(yer1) +2
        havuz1.insert(yerd,(w[yerd]))
        havuz1.insert(yerd+1,w[yerd+1])
        havuz1.insert(yerd+2,w[yerd+2])
        havuz1.insert(yerd+3,w[yerd+3])
    elif secim1 in yasak3:
        yerd = int(yer1) +1
        havuz1.insert(yerd,(w[yerd]))
        havuz1.insert(yerd+1,w[yerd+1])
        havuz1.insert(yerd+2,w[yerd+2])
        havuz1.insert(yerd+3,w[yerd+3])
    else:
        yerd = int(yer1)
        havuz1.insert(yerd,(w[yerd]))
        havuz1.insert(yerd+1,w[yerd+1])
        havuz1.insert(yerd+2,w[yerd+2])
        havuz1.insert(yerd+3,w[yerd+3])
amiral1()

def Amiral2():
    global havuz1
    while True:
        secim5 = random.choice(w)
        yer5 = w.index(secim5)
        if secim5 in havuz1:
             secim5 = random.choice(w)
        else:
            break
    
    if secim5 in yasak5:
        yerd = int(yer5) +3
        havuz1.insert(yerd-40,w[yerd-40])
        havuz1.insert(yerd-30,w[yerd-30])
        havuz1.insert(yerd-20,w[yerd-20])
        havuz1.insert(yerd-10,w[yerd-10])     
    else:
        yerd = int(yer5) +1
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+10,w[yerd+10])
        havuz1.insert(yerd+20,w[yerd+20])
        havuz1.insert(yerd+30,w[yerd+30]) 
        
Amiral2()

def Kruvazor1():
    global havuz1
    while True:
        secim2 = random.choice(w)
        yer2 = w.index(secim2) 
        if secim2 in havuz1:
            secim2 = random.choice(w)
        else:
            break
    if secim2 in yasak4:
        yerd = int(yer2) -97
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+1,w[yerd+1])
        havuz1.insert(yerd+2,w[yerd+2])
    elif secim2 in yasak2:
        yerd = int(yer2) +2
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+1,w[yerd+1])
        havuz1.insert(yerd+2,w[yerd+2])
    elif secim2 in yasak3:
        yerd = int(yer2) +1
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+1,w[yerd+1])
        havuz1.insert(yerd+2,w[yerd+2])
    else:
        yerd = int(yer2)
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+1,w[yerd+1])
        havuz1.insert(yerd+2,w[yerd+2])
                
Kruvazor1()

def Kruvazor2():
    global havuz1
    while True:
        secim6 = random.choice(w)
        yer6 = w.index(secim6)
        if secim6 in havuz1:
            secim6 = random.choice(w)
        else:
            break
    if yer6>=80:
        yerd = int(yer6) -20
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+10,w[yerd+10])
        havuz1.insert(yerd+20,w[yerd+20])
    else:
        yerd = int(yer6)
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+10,w[yerd+10])
        havuz1.insert(yerd+20,w[yerd+20])
Kruvazor2()

def Muhrip1():
    global havuz1
    while True:
        secim3 = random.choice(w) 
        yer3 = w.index(secim3)
        if secim3 in havuz1:
            secim3 = random.choice(w) 
        else:
            break
    if secim3 in yasak4:
        yerd = int(yer3) -97
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+1,w[yerd+1])
    elif secim3 in yasak3:
        yerd = int(yer3) +1    
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+1,w[yerd+1])
    else:
        yerd = int(yer3)    
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+1,w[yerd+1])  
Muhrip1()

def Muhrip2():
    global havuz1
    while True:
        secim7 = random.choice(w)
        yer7 = w.index(secim7)
        if secim7 in havuz1:
            secim7 = random.choice(w)
        else:
            break
    if yer7>=90:
        yerd = int(yer7) -10
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+10,w[yerd+10])
    elif secim7 in yasak5:
        yerd = int(yer7) +1    
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+10,w[yerd+10])
    else:
        yerd = int(yer7)    
        havuz1.insert(yerd,w[yerd])
        havuz1.insert(yerd+10,w[yerd+10])
Muhrip2()


secim4 = random.choice(w)  
yer4 = w.index(secim4)
Denizalti1 = [w[yer4]]
havuz1.insert(yer4,w[yer4])

secim8 = random.choice(w)    
yer8 = w.index(secim8)
Denizalti2 = [w[yer8]]
havuz1.insert(yer8,w[yer8])


#print("z...",z)       

q =   {'a1':'[ ]','a2':'[ ]','a3':'[ ]','a4':'[ ]','a5':'[ ]','a6':'[ ]','a7':'[ ]','a8':'[ ]','a9':'[ ]','a10':'[ ]',
       'b1':'[ ]','b2':'[ ]','b3':'[ ]','b4':'[ ]','b5':'[ ]','b6':'[ ]','b7':'[ ]','b8':'[ ]','b9':'[ ]','b10':'[ ]',
       'c1':'[ ]','c2':'[ ]','c3':'[ ]','c4':'[ ]','c5':'[ ]','c6':'[ ]','c7':'[ ]','c8':'[ ]','c9':'[ ]','c10':'[ ]',
       'd1':'[ ]','d2':'[ ]','d3':'[ ]','d4':'[ ]','d5':'[ ]','d6':'[ ]','d7':'[ ]','d8':'[ ]','d9':'[ ]','d10':'[ ]',
       'e1':'[ ]','e2':'[ ]','e3':'[ ]','e4':'[ ]','e5':'[ ]','e6':'[ ]','e7':'[ ]','e8':'[ ]','e9':'[ ]','e10':'[ ]',
       'f1':'[ ]','f2':'[ ]','f3':'[ ]','f4':'[ ]','f5':'[ ]','f6':'[ ]','f7':'[ ]','f8':'[ ]','f9':'[ ]','f10':'[ ]',
       'g1':'[ ]','g2':'[ ]','g3':'[ ]','g4':'[ ]','g5':'[ ]','g6':'[ ]','g7':'[ ]','g8':'[ ]','g9':'[ ]','g10':'[ ]',
       'h1':'[ ]','h2':'[ ]','h3':'[ ]','h4':'[ ]','h5':'[ ]','h6':'[ ]','h7':'[ ]','h8':'[ ]','h9':'[ ]','h10':'[ ]',
       'k1':'[ ]','k2':'[ ]','k3':'[ ]','k4':'[ ]','k5':'[ ]','k6':'[ ]','k7':'[ ]','k8':'[ ]','k9':'[ ]','k10':'[ ]',
       'l1':'[ ]','l2':'[ ]','l3':'[ ]','l4':'[ ]','l5':'[ ]','l6':'[ ]','l7':'[ ]','l8':'[ ]','l9':'[ ]','l10':'[ ]',}  

for i in w:
    if i not in havuz1:
        z = dict.fromkeys(w,m)
    else:
        break
for i in havuz1:
    if i in z:
        z[i]=k   


print("""Gemilerin yerlestirildigi tablomuz;
      
    1    2    3    4    5    6    7    8    9   10 
a [a1] [a2] [a3] [a4] [a5] [a6] [a7] [a8] [a9] [a10]
b [b1] [b2] [b3] [b4] [b5] [b6] [b7] [b8] [b9] [b10] 
c [c1] [c2] [c3] [c4] [c5] [c6] [c7] [c8] [c9] [c10]
d [d1] [d2] [d3] [d4] [d5] [d6] [d7] [d8] [d9] [d10]
e [e1] [e2] [e3] [e4] [e5] [e6] [e7] [e8] [e9] [e10]
f [f1] [f2] [f3] [f4] [f5] [f6] [f7] [f8] [f9] [f10]
g [g1] [g2] [g3] [g4] [g5] [g6] [g7] [g8] [g9] [g10]
h [h1] [h2] [h3] [h4] [h5] [h6] [h7] [h8] [h9] [h10]
k [k1] [k2] [k3] [k4] [k5] [k6] [k7] [k8] [k9] [k10]
l [l1] [l2] [l3] [l4] [l5] [l6] [l7] [l8] [l9] [l10] \n""")

print()
print('Hazirsaniz basliyoruz..')
sleep(3)
print()
print('B', 'A', 'S', 'A', 'R', 'I', 'L', 'A', 'R', '.', '.' ,'.',sep='  ')

print()
print("Bilgisayar gemilerini yerlestiriyor..")
print()
sleep(5)
print('Bilgisayar gemilerini yerlestirdi simdi sira sizde..')
sleep(5)
ww =   ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10',
       'b1','b2','b3','b4','b5','b6','b7','b8','b9','b10',
       'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10',
       'd1','d2','d3','d4','d5','d6','d7','d8','d9','d10',
       'e1','e2','e3','e4','e5','e6','e7','e8','e9','e10',
       'f1','f2','f3','f4','f5','f6','f7','f8','f9','f10',
       'g1','g2','g3','g4','g5','g6','g7','g8','g9','g10',
       'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10',
       'k1','k2','k3','k4','k5','k6','k7','k8','k9','k10',
       'l1','l2','l3','l4','l5','l6','l7','l8','l9','l10']
zz=[]

havuz11 =   ['','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','',
            '','','','','','','','','','']

k = '[x]'
m ='[]'


kul1=input("""Oyundaki gemilerinizin; 
bilgisayar tarafindan dagitilmasini istiyorsaniz '1' e, 
kendiniz yerlestirmek istiyorsaniz '2'ye basiniz :..""" )
print()
if kul1=='1':
    print('Lutfen bekleyiniz gemileriniz en uygun sekilde yerlestiriliyor..')
    def amiral1():
        global havuz11
        while True:
            secim1 = random.choice(w)
            yer1 = w.index(secim1)
            if secim1 in havuz11:
                secim1 = random.choice(w)
            else:
                break
        if secim1 in yasak4:
            yerd = int(yer1) -5
            havuz11.insert(yerd,(w[yerd]))
            havuz11.insert(yerd+1,w[yerd+1])
            havuz11.insert(yerd+2,w[yerd+2])
            havuz11.insert(yerd+3,w[yerd+3])
        elif secim1 in yasak1: 
            yerd = int(yer1) +3
            havuz11.insert(yerd,(w[yerd]))
            havuz11.insert(yerd+1,w[yerd+1])
            havuz11.insert(yerd+2,w[yerd+2])
            havuz11.insert(yerd+3,w[yerd+3])
        elif secim1 in yasak2:
            yerd = int(yer1) +2
            havuz11.insert(yerd,(w[yerd]))
            havuz11.insert(yerd+1,w[yerd+1])
            havuz11.insert(yerd+2,w[yerd+2])
            havuz11.insert(yerd+3,w[yerd+3])
        elif secim1 in yasak3:
            yerd = int(yer1) +1
            havuz11.insert(yerd,(w[yerd]))
            havuz11.insert(yerd+1,w[yerd+1])
            havuz11.insert(yerd+2,w[yerd+2])
            havuz11.insert(yerd+3,w[yerd+3])
        else:
            yerd = int(yer1)
            havuz11.insert(yerd,(w[yerd]))
            havuz11.insert(yerd+1,w[yerd+1])
            havuz11.insert(yerd+2,w[yerd+2])
            havuz11.insert(yerd+3,w[yerd+3])
    amiral1()
    
    def Amiral2():
        global havuz11
        while True:
            secim5 = random.choice(w)
            yer5 = w.index(secim5)
            if secim5 in havuz11:
                 secim5 = random.choice(w)
            else:
                break
        
        if secim5 in yasak5:
            yerd = int(yer5) +3
            havuz11.insert(yerd-40,w[yerd-40])
            havuz11.insert(yerd-30,w[yerd-30])
            havuz11.insert(yerd-20,w[yerd-20])
            havuz11.insert(yerd-10,w[yerd-10])     
        else:
            yerd = int(yer5) +1
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+10,w[yerd+10])
            havuz11.insert(yerd+20,w[yerd+20])
            havuz11.insert(yerd+30,w[yerd+30]) 
            
    Amiral2()
    
    def Kruvazor1():
        global havuz11
        while True:
            secim2 = random.choice(w)
            yer2 = w.index(secim2) 
            if secim2 in havuz11:
                secim2 = random.choice(w)
            else:
                break
        if secim2 in yasak4:
            yerd = int(yer2) -97
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+1,w[yerd+1])
            havuz11.insert(yerd+2,w[yerd+2])
        elif secim2 in yasak2:
            yerd = int(yer2) +2
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+1,w[yerd+1])
            havuz11.insert(yerd+2,w[yerd+2])
        elif secim2 in yasak3:
            yerd = int(yer2) +1
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+1,w[yerd+1])
            havuz11.insert(yerd+2,w[yerd+2])
        else:
            yerd = int(yer2)
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+1,w[yerd+1])
            havuz11.insert(yerd+2,w[yerd+2])
                    
    Kruvazor1()
    
    def Kruvazor2():
        global havuz11
        while True:
            secim6 = random.choice(w)
            yer6 = w.index(secim6)
            if secim6 in havuz11:
                secim6 = random.choice(w)
            else:
                break
        if yer6>=80:
            yerd = int(yer6) -20
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+10,w[yerd+10])
            havuz11.insert(yerd+20,w[yerd+20])
        else:
            yerd = int(yer6)
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+10,w[yerd+10])
            havuz11.insert(yerd+20,w[yerd+20])
    Kruvazor2()
    
    def Muhrip1():
        global havuz11
        while True:
            secim3 = random.choice(w) 
            yer3 = w.index(secim3)
            if secim3 in havuz11:
                secim3 = random.choice(w) 
            else:
                break
        if secim3 in yasak4:
            yerd = int(yer3) -97
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+1,w[yerd+1])
        elif secim3 in yasak3:
            yerd = int(yer3) +1    
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+1,w[yerd+1])
        else:
            yerd = int(yer3)    
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+1,w[yerd+1])  
    Muhrip1()
    
    def Muhrip2():
        global havuz11
        while True:
            secim7 = random.choice(w)
            yer7 = w.index(secim7)
            if secim7 in havuz11:
                secim7 = random.choice(w)
            else:
                break
        if yer7>=90:
            yerd = int(yer7) -10
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+10,w[yerd+10])
        elif secim7 in yasak5:
            yerd = int(yer7) +1    
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+10,w[yerd+10])
        else:
            yerd = int(yer7)    
            havuz11.insert(yerd,w[yerd])
            havuz11.insert(yerd+10,w[yerd+10])
    Muhrip2()
    
    
    secim4 = random.choice(w)  
    yer4 = w.index(secim4)
    Denizalti1 = [w[yer4]]
    havuz11.insert(yer4,w[yer4])
    
    secim8 = random.choice(w)    
    yer8 = w.index(secim8)
    Denizalti2 = [w[yer8]]
    havuz11.insert(yer8,w[yer8])
    sleep(3)
print()
sleep(2)
if kul1=='2':
    print("Gemilerinizi tablodaki alan adlarina gore tek tek yerlestiriniz.(ornegin; a1 veya k5 vs..")
    print()
    def amiral1():
        global havuz11
        havuz11.append(input("Amiral1 icin yer secin :"))
        havuz11.append(input("Amiral1 icin yer secin :"))
        havuz11.append(input("Amiral1 icin yer secin :"))
        havuz11.append(input("Amiral1 icin yer secin :"))
        return havuz11
    amiral1()
    
    def Amiral2():
        global havuz11
        havuz11.append(input("Amiral2 icin yer secin :"))
        havuz11.append(input("Amiral2 icin yer secin :"))
        havuz11.append(input("Amiral2 icin yer secin :"))
        havuz11.append(input("Amiral2 icin yer secin :"))
        return havuz11
            
    Amiral2()
    
    def Kruvazor1():
        global havuz11
        havuz11.append(input("Kruvazor1 icin yer secin :"))
        havuz11.append(input("Kruvazor1 icin yer secin :"))
        havuz11.append(input("Kruvazor1 icin yer secin :"))
        return havuz11            
    Kruvazor1()
    
    def Kruvazor2():
        global havuz11
        havuz11.append(input("Kruvazor2 icin yer secin :"))
        havuz11.append(input("Kruvazor2 icin yer secin :"))
        havuz11.append(input("Kruvazor2 icin yer secin :"))
        return havuz11
    Kruvazor2()
    
    def Muhrip1():
        global havuz11
        havuz11.append(input("Muhrip1 icin yer secin :"))
        havuz11.append(input("Muhrip1 icin yer secin :"))
        return havuz11
    Muhrip1()
    
    def Muhrip2():
        global havuz11
        havuz11.append(input("Muhrip2 icin yer secin :"))
        havuz11.append(input("Muhrip2 icin yer secin :"))
        return havuz11
    Muhrip2()
    
    havuz11.append(input("Denizalti1 icin yer secin :"))
    
    havuz11.append(input("Denizalti2 icin yer secin :")) 

#print(havuz1)
print(havuz11)
#print("zz ...",zz)       

p =   {'a1':'[ ]','a2':'[ ]','a3':'[ ]','a4':'[ ]','a5':'[ ]','a6':'[ ]','a7':'[ ]','a8':'[ ]','a9':'[ ]','a10':'[ ]',
       'b1':'[ ]','b2':'[ ]','b3':'[ ]','b4':'[ ]','b5':'[ ]','b6':'[ ]','b7':'[ ]','b8':'[ ]','b9':'[ ]','b10':'[ ]',
       'c1':'[ ]','c2':'[ ]','c3':'[ ]','c4':'[ ]','c5':'[ ]','c6':'[ ]','c7':'[ ]','c8':'[ ]','c9':'[ ]','c10':'[ ]',
       'd1':'[ ]','d2':'[ ]','d3':'[ ]','d4':'[ ]','d5':'[ ]','d6':'[ ]','d7':'[ ]','d8':'[ ]','d9':'[ ]','d10':'[ ]',
       'e1':'[ ]','e2':'[ ]','e3':'[ ]','e4':'[ ]','e5':'[ ]','e6':'[ ]','e7':'[ ]','e8':'[ ]','e9':'[ ]','e10':'[ ]',
       'f1':'[ ]','f2':'[ ]','f3':'[ ]','f4':'[ ]','f5':'[ ]','f6':'[ ]','f7':'[ ]','f8':'[ ]','f9':'[ ]','f10':'[ ]',
       'g1':'[ ]','g2':'[ ]','g3':'[ ]','g4':'[ ]','g5':'[ ]','g6':'[ ]','g7':'[ ]','g8':'[ ]','g9':'[ ]','g10':'[ ]',
       'h1':'[ ]','h2':'[ ]','h3':'[ ]','h4':'[ ]','h5':'[ ]','h6':'[ ]','h7':'[ ]','h8':'[ ]','h9':'[ ]','h10':'[ ]',
       'k1':'[ ]','k2':'[ ]','k3':'[ ]','k4':'[ ]','k5':'[ ]','k6':'[ ]','k7':'[ ]','k8':'[ ]','k9':'[ ]','k10':'[ ]',
       'l1':'[ ]','l2':'[ ]','l3':'[ ]','l4':'[ ]','l5':'[ ]','l6':'[ ]','l7':'[ ]','l8':'[ ]','l9':'[ ]','l10':'[ ]',}  


for i in ww:
    if i not in havuz11:
        zz = dict.fromkeys(ww,m)
        
for i in havuz11:  
    if i in zz:
        zz[i]=k         
    
sleep(5)

#print('havuz1 :',havuz1)
#print("havuz11",havuz11)
sayac1=0
sayac2=0
basarisiz1=0
basarisiz2=0
while basarisiz1<20: 
    sleep(3)
    while True:
        sleep(2)
        kul=input("(OYUNCU) Tablo uzerindeki herhangi bir noktaya hamlede bulunun :...")
        if kul not in q:
            print("\n","Lutfen gecerli bir tahmin yapiniz!!","\n")
            pass
        if kul in z and z[kul]=='[x]':
            if q[kul] == '[x]':
                print("\n","Bu tahmini kullanmistiniz!!","\n")
                sayac1 += 1
                if sayac1==19:
                    print("""\n--------------------------------------------
    
    
         .....K A Z A N D I N I Z!!.....
    
                    
    --------------------------------------------
    
    """)       
                pass
            else:
                q[kul]='[x]'
                print("\n","Basarili hamle ","\n")
                sleep(3)
                
                
        else:
            basarisiz1+=1
            q[kul]='[0]'
            print("\n",basarisiz1,". basarisiz hamle ")
            sleep(2)
            print("\n")
            print( "......O Y U N C U  P A N O S U.......")
            print(              '   1 ',' 2 ' ,' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ',' 10 ' )
            print(         'a', q['a1'],q['a2'],q['a3'],q['a4'],q['a5'],q['a6'],q['a7'],q['a8'],q['a9'],q['a10'])
            print(         'b', q['b1'],q['b2'],q['b3'],q['b4'],q['b5'],q['b6'],q['b7'],q['b8'],q['b9'],q['b10'])
            print(         'c', q['c1'],q['c2'],q['c3'],q['c4'],q['c5'],q['c6'],q['c7'],q['c8'],q['c9'],q['c10'])
            print(         'd', q['d1'],q['d2'],q['d3'],q['d4'],q['d5'],q['d6'],q['d7'],q['d8'],q['d9'],q['d10'])
            print(         'e', q['e1'],q['e2'],q['e3'],q['e4'],q['e5'],q['e6'],q['e7'],q['e8'],q['e9'],q['e10'])
            print(         'f', q['f1'],q['f2'],q['f3'],q['f4'],q['f5'],q['f6'],q['f7'],q['f8'],q['f9'],q['f10'])
            print(         'g', q['g1'],q['g2'],q['g3'],q['g4'],q['g5'],q['g6'],q['g7'],q['g8'],q['g9'],q['g10'])
            print(         'h', q['h1'],q['h2'],q['h3'],q['h4'],q['h5'],q['h6'],q['h7'],q['h8'],q['h9'],q['h10'])
            print(         'k', q['k1'],q['k2'],q['k3'],q['k4'],q['k5'],q['k6'],q['k7'],q['k8'],q['k9'],q['k10'])
            print(         'l', q['l1'],q['l2'],q['l3'],q['l4'],q['l5'],q['l6'],q['l7'],q['l8'],q['l9'],q['l10'])
            print("\n")
            break
        
        if basarisiz1==15:
            print("""\n--------------------------------------------
    
    
         .....K A Y B E T T I N I Z!!.....
    
                    
    --------------------------------------------""")
            
        print( "......O Y U N C U  P A N O S U.......")
        print(              '   1 ',' 2 ' ,' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ',' 10 ' )
        print(         'a', q['a1'],q['a2'],q['a3'],q['a4'],q['a5'],q['a6'],q['a7'],q['a8'],q['a9'],q['a10'])
        print(         'b', q['b1'],q['b2'],q['b3'],q['b4'],q['b5'],q['b6'],q['b7'],q['b8'],q['b9'],q['b10'])
        print(         'c', q['c1'],q['c2'],q['c3'],q['c4'],q['c5'],q['c6'],q['c7'],q['c8'],q['c9'],q['c10'])
        print(         'd', q['d1'],q['d2'],q['d3'],q['d4'],q['d5'],q['d6'],q['d7'],q['d8'],q['d9'],q['d10'])
        print(         'e', q['e1'],q['e2'],q['e3'],q['e4'],q['e5'],q['e6'],q['e7'],q['e8'],q['e9'],q['e10'])
        print(         'f', q['f1'],q['f2'],q['f3'],q['f4'],q['f5'],q['f6'],q['f7'],q['f8'],q['f9'],q['f10'])
        print(         'g', q['g1'],q['g2'],q['g3'],q['g4'],q['g5'],q['g6'],q['g7'],q['g8'],q['g9'],q['g10'])
        print(         'h', q['h1'],q['h2'],q['h3'],q['h4'],q['h5'],q['h6'],q['h7'],q['h8'],q['h9'],q['h10'])
        print(         'k', q['k1'],q['k2'],q['k3'],q['k4'],q['k5'],q['k6'],q['k7'],q['k8'],q['k9'],q['k10'])
        print(         'l', q['l1'],q['l2'],q['l3'],q['l4'],q['l5'],q['l6'],q['l7'],q['l8'],q['l9'],q['l10'])
        print("\n")
        
        print("Tekrar bir hamle yapiniz..")
        sleep(3)
        
        
    print("(Hamle sirasi BILGISAYARda lutfen bekleyiniz..")    
    while True:        
        sleep(5)
        kul=random.choice(ww)
        if kul not in p:
            print("\n","Lutfen gecerli bir tahmin yapiniz!!","\n")
            pass
        if kul in zz and zz[kul]=='[x]':
            if p[kul] == '[x]':
                print("\n","Bu tahmini kullanmistiniz!!","\n")
                sayac2 += 1
                if sayac2==19:
                    print("""\n--------------------------------------------
    
    
         .....K A Z A N D I N I Z!!.....
    
                    
    --------------------------------------------
    
    """)
                pass
            else:
                p[kul]='[x]'
                print("\n","Basarili hamle ","\n")
                sleep(3)
                
                    
        else:
            basarisiz2+=1
            p[kul]='[0]'
            print("\n",basarisiz2,". basarisiz hamle ","\n")
            sleep(2)
            print( "....B I L G I S A Y A R  P A N O S U......")
            print(              '   1 ',' 2 ' ,' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ',' 10 ' )
            print(         'a', p['a1'],p['a2'],p['a3'],p['a4'],p['a5'],p['a6'],p['a7'],p['a8'],p['a9'],p['a10'])
            print(         'b', p['b1'],p['b2'],p['b3'],p['b4'],p['b5'],p['b6'],p['b7'],p['b8'],p['b9'],p['b10'])
            print(         'c', p['c1'],p['c2'],p['c3'],p['c4'],p['c5'],p['c6'],p['c7'],p['c8'],p['c9'],p['c10'])
            print(         'd', p['d1'],p['d2'],p['d3'],p['d4'],p['d5'],p['d6'],p['d7'],p['d8'],p['d9'],p['d10'])
            print(         'e', p['e1'],p['e2'],p['e3'],p['e4'],p['e5'],p['e6'],p['e7'],p['e8'],p['e9'],p['e10'])
            print(         'f', p['f1'],p['f2'],p['f3'],p['f4'],p['f5'],p['f6'],p['f7'],p['f8'],p['f9'],p['f10'])
            print(         'g', p['g1'],p['g2'],p['g3'],p['g4'],p['g5'],p['g6'],p['g7'],p['g8'],p['g9'],p['g10'])
            print(         'h', p['h1'],p['h2'],p['h3'],p['h4'],p['h5'],p['h6'],p['h7'],p['h8'],p['h9'],p['h10'])
            print(         'k', p['k1'],p['k2'],p['k3'],p['k4'],p['k5'],p['k6'],p['k7'],p['k8'],p['k9'],p['k10'])
            print(         'l', p['l1'],p['l2'],p['l3'],p['l4'],p['l5'],p['l6'],p['l7'],p['l8'],p['l9'],p['l10'])
            break
        if basarisiz2==15:
            print("""\n--------------------------------------------
    
    
         .....BILGISAYAR KAYBETTI!!.....
    
                    
    --------------------------------------------
    
    """)    
            
        print( "....B I L G I S A Y A R  P A N O S U......")
        print(              '   1 ',' 2 ' ,' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ',' 10 ' )
        print(         'a', p['a1'],p['a2'],p['a3'],p['a4'],p['a5'],p['a6'],p['a7'],p['a8'],p['a9'],p['a10'])
        print(         'b', p['b1'],p['b2'],p['b3'],p['b4'],p['b5'],p['b6'],p['b7'],p['b8'],p['b9'],p['b10'])
        print(         'c', p['c1'],p['c2'],p['c3'],p['c4'],p['c5'],p['c6'],p['c7'],p['c8'],p['c9'],p['c10'])
        print(         'd', p['d1'],p['d2'],p['d3'],p['d4'],p['d5'],p['d6'],p['d7'],p['d8'],p['d9'],p['d10'])
        print(         'e', p['e1'],p['e2'],p['e3'],p['e4'],p['e5'],p['e6'],p['e7'],p['e8'],p['e9'],p['e10'])
        print(         'f', p['f1'],p['f2'],p['f3'],p['f4'],p['f5'],p['f6'],p['f7'],p['f8'],p['f9'],p['f10'])
        print(         'g', p['g1'],p['g2'],p['g3'],p['g4'],p['g5'],p['g6'],p['g7'],p['g8'],p['g9'],p['g10'])
        print(         'h', p['h1'],p['h2'],p['h3'],p['h4'],p['h5'],p['h6'],p['h7'],p['h8'],p['h9'],p['h10'])
        print(         'k', p['k1'],p['k2'],p['k3'],p['k4'],p['k5'],p['k6'],p['k7'],p['k8'],p['k9'],p['k10'])
        print(         'l', p['l1'],p['l2'],p['l3'],p['l4'],p['l5'],p['l6'],p['l7'],p['l8'],p['l9'],p['l10'])
        
        print("Bilgisayar tekrar oynuyor..")
        sleep(3)

           
        
            


