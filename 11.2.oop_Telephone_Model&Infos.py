print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

import time


class Telephone:

    def __init__(self, merk, model, product_year, tel_no, rehber):
        self.merk = merk
        self.model = model
        self.product_year = product_year
        self.tel_no = tel_no
        self.rehber = rehber
        self.rehber = {}

    def info(self):
        print(f'''
              Telephone Merk: {self.merk},
                       Model: {self.model},
                Product Year: {self.product_year},
Datas of the contact numbers: {self.rehber}''')

    def rehber_ekle(self, name, tel):
        self.rehber[name] = tel

    def rehber_sil(self, name):
        if name in self.rehber:
            self.rehber.pop(name)
            print(f'{name} is deleting...')
        else:
            print(f'{name} is not in Contacts!')

    def rehber_gor(self):
        for name, tel in self.rehber.items():
            print(name, ":", tel)

    def call_no(self):
        name = input("Please enter you want calling name: ")
        if name in self.rehber:
            print(f'{self.rehber[name]} is calling...')
            time.sleep(5)
            print(f'{self.rehber[name]} is not giving respond please try later...')
        else:
            print(f'{name} is not find in the Contacts!')


phone_x = Telephone("Iphone", "X+", 2018, "06 85296380", rehber={})             # Class icin telefon icerikleri girdik
phone_y = Telephone("Huawei", "P20", 2019, "06 32165480", rehber={})            #olusacak rehber bilgilerini sozluk seklinde atsin

print("Please chose one telephone model: \nphone_x \nphone_y".lower())

chose_phone = input("Chose one telephone: ")

if chose_phone == "phone_x":
    chose_phone = phone_x
else:
    chose_phone = phone_y


def menu():                                             # menu icerigini
    print("""Menu
    1. Show Phone model and merk
    2. Add new contact
    3. Show contacts
    4. Delete contact
    5. Call one number
    6. Quit""")

while True:
    menu()
    enter = input("Input one number: ")
    try:
        enter = int(enter)
        if enter == 1:                                      # secilen telefon modelini yazdirma
            chose_phone.info()
        elif enter == 2:                                    # numara ekle
            name = input("Enter name:")
            tel = input("Enter number: ")
            chose_phone.rehber_ekle(name, tel)
        elif enter == 3:                                    # rehber goster
            chose_phone.rehber_gor()
        elif enter == 4:                                    # rehber sil
            name = input("Enter name which you want to delete: ")
            chose_phone.rehber_sil(name)
        elif enter == 5:                                    # arama yap
            chose_phone.call_no()
        elif enter == 6:
            print("Exiting from Menu...")
            quit()
    except ValueError:
        print("Please enter 1,2,3,4,5,6...")
