#Odev 2: Bir cep telefonu objesi yapmanizi istiyoruz.
# Telefonun marka, model, uretim yili, tel nosu ve rehber ozelliklerinin(class attributes) olmasini bekliyoruz.
# Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme, rehberden secilen bir noyu arama(gostermelik)
# gibi ozelliklerinin (class methods) olmasini istiyoruz.

class Handy:


    def __init__(self, mark=" ", model=" ", productyear=0, serialnumber="", phone_book={}):
        self.mark=mark
        self.model=model
        self.productyear=productyear
        self.serialnumber=serialnumber
        self.phone_book=phone_book
        self.add={}
        self.delete={}
        print("Mark is:", self.mark,", Model is:", self.model,", Product Year Is:", self.productyear,", Serial Number is:", self.serialnumber,", Guide is:", self.phone_book)

    def addcontack(self,contac="",number="0"):
        self.contact=input("Please enter The name You Add: ")
        self.number =input("Please enter number you Add: ")
        self.add[self.contact]=self.number
        self.phone_book.update(self.add)
        print(self.phone_book)

    def deletecontact(self):
        self.contact = input("Please enter The name You Delete: ")
        if self.contact in self.phone_book:
            self.phone_book.pop(self.contact)
            print(self.phone_book)
        else:
            print("The Person You Delete Is not in the Guide")

    def show_phone_book(self):
        print(self.phone_book)

    def calling(self):
        self.contact = input("Please enter The name You Call: ")
        if self.contact in self.phone_book:
            print("Calling",self.contact, self.phone_book[self.contact])
        else:
            print("The Person is not in Guide!!!!")


Phone1=Handy()
"""Phone1=Handy("Apple","6S",2016,'01234',{'fikret': 4455})
Phone2=Handy("Samsung","S7",2017,'4321',{'yilmaz': 5544})
Phone1.addcontack()
Phone1.addcontack()
Phone1.deletecontact()
Phone1.show_phone_book()
Phone1.calling()
"""

print("""Welcome to the Phohe Class Application:
    1-Add a New Contact
    2-Delete a Contact
    3-Show Phonebook
    4-Calling
    0-Quit      
    """)

while True:

    answer = input("Please make your choice:  ")
    if answer == "1":
        Phone1.addcontack()

    elif answer == "2":
        Phone1.deletecontact()

    elif answer == "3":
        Phone1.show_phone_book()

    elif answer == "4":
        Phone1.calling()

    elif answer == "0":
        break