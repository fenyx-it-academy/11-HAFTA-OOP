# 11-HAFTA-OOP
Odev 1: Gecen hafta basladigimiz amiral batti oyununu gelistirecegiz. 
Bu hafta kodunuzu Object Oriented sekline cevirmenizi istiyoruz.
 Ayrica randomsuz yapanlarin random gemi yerlestirme ozelligini eklemelerini bekliyoruz. 
Bonus ozellik olarak oyunun bilgisayara karsi oynanan iki kisilik versiyonunu yapabilirsiniz. 

Odev 2:
Bir cep telefonu objesi yapmanizi istiyoruz. 
Telefonun marka, model, uretim yili, tel nosu ve rehber 
ozelliklerinin(class attributes) olmasini bekliyoruz. 
Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme, 
rehberden secilen bir noyu arama(gostermelik) gibi ozelliklerinin 
(class methods) olmasini istiyoruz. 

Odev 3:
Bir muzik calar objesi yapmanizi istiyoruz. Class attribute olarak bos bir sarki listesi 
 olusturun. Class methods olarak sarki listesini sifirlama, listeyi goruntuleme, sarki ekleme, 
sarki silme, sonraki parcayi cal, onceki parcayi cal, karisik cal ozelliklerini ekleyin.

 ship_coord_board =[["___", "___", "___", "___", "___", "___", "___", "___", "___", "_X_"],
#                    ["___", "___", "___", "___", "___", "___", "___", "___", "___", "_X_"],
#                    ["___", "_X_", "___", "___", "_X_", "_X_", "_X_", "___", "___", "___"],
#                    ["___", "_X_", "___", "___", "___", "___", "___", "___", "___", "___"],
#                    ["___", "___", "___", "_X_", "___", "___", "___", "_X_", "___", "___"],
#                    ["___", "___", "___", "_X_", "___", "___", "___", "___", "___", "___"],
#                    ["___", "___", "___", "_X_", "___", "___", "___", "___", "___", "___"],
#                    ["___", "___", "___", "_X_", "___", "___", "_X_", "_X_", "_X_", "_X_"],
#                    ["_X_", "_X_", "_X_", "___", "___", "___", "___", "___", "___", "___"],
#                    ["___", "___", "___", "___", "_X_", "___", "___", "___", "___", "___"]]


ship_coord_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 'X' ],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 'X' ],
                    [0, 'X', 0, 0, 'X', 'X', 'X', 0, 0, 0 ],
                    [0, 'X', 0, 0, 0, 0, 0, 0, 0, 0 ],
                    [0, 0, 0, 'X', 0, 0, 0, 'X', 0, 0 ],
                    [0, 0, 0, 'X', 0, 0, 0, 0, 0, 0 ],
                    [0, 0, 0, 'X', 0, 0, 0, 0, 0, 0 ],
                    [0, 0, 0, 'X', 0, 0, 'X', 'X', 'X', 'X' ],
                    ['X', 'X', 'X', 0, 0, 0, 0, 0, 0, 0 ],
                    [0, 0, 0, 0, 'X', 0, 0, 0, 0, 0 ]]


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]]
