import time

class Mytel:

    def __init__(self, brand, model, prodate, imei, contacts):
        self.brand = brand
        self.model = model
        self.prodate = prodate
        self.imei = imei
        self.contacts = contacts
        self.contacts = {}

    def showInfo(self):
        print("""
    MyTel Information:
    Brand   : {}
    Model   : {}
    Pro Date: {}
    Imei No : {}
    Contacts: {}
    """.format(self.brand, self.model, self.prodate, self.imei, self.contacts))

    def contactsAdd(self, name, tel):
        print("Adding your contacttt")
        self.contacts[name] = tel
        time.sleep(1)
        print("Your contact addedd\n")
        time.sleep(1)

    def showContacts(self):
        for name, tel in self.contacts.items():
            print("Your contacts list")
            print(name, ':', tel)
            time.sleep(2)

    def contactsDelete(self, sel):
        sel = input("Name of the contact to delete:")
        if sel in self.contacts:
            print("Deletinggg..")
            self.contacts.pop(sel)

            time.sleep(1)
            print("Deleteddd\n")
            time.sleep(1)
        else:
                print("Name is not in contact list\n")
                time.sleep(1)

    def dial(self):
        for name, tel in self.contacts.items():
            print(name, ':', tel)
        name = input('Enter contact name to dial\n')
        if name in self.contacts:
            print(f'{self.contacts[name]} dialinggg....\n')
            time.sleep(3)
            print(f'{self.contacts[name]} is not available or outof coverage\n')
        else:
            print("please check your contact's name\n")

telim = Mytel("LaCasa", "Black", "August 2019", 123456789, ["233"])
print("Welcome To Telephone Book Trials")

while True:
    sel = input(" ____Please choose your transaction___ \n"
                "*View your phone info...1\n"
                "*Add new contact    ....2\n"
                "*Browse contacts    ....3\n"
                "*Dial contact       ....4\n"
                "*Delete contact     ....5\n"
                "*Save&Exit       *anykey*\n")
###########################################################
    if sel == '1':
        telim.showInfo()
        time.sleep(2)
###########################################################
    elif sel == '2':
        name = input('New contact name: ')
        tel = input('New contact number: ')
        telim.contactsAdd(name, tel)
###########################################################
    elif sel == '3':
        telim.showContacts()
###########################################################
    elif sel == '4':
        telim.dial()
###########################################################
    elif sel == '5':

        telim.contactsDelete(sel)
###########################################################
    else:
        print('Please wait shutting down!')
        time.sleep(1)
        print("Goodbye!!!")
        quit()
