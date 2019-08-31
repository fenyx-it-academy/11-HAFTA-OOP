# 11. Hafta Odev 2:
# Bir cep telefonu objesi yapmanizi istiyoruz.
# Telefonun marka, model, uretim yili, tel nosu ve rehber
# ozelliklerinin(class attributes) olmasini bekliyoruz.
# Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme,
# rehberden secilen bir noyu arama(gostermelik) gibi ozelliklerinin


class telephone():
    def __init__(self, mark, model, man_date, tel_num, tel_list):
        self.mark = mark
        self.model = model
        self.man_date = man_date
        self.tel_num = tel_num
        self.tel_list = tel_list

    def add_sb(self, name, number):
        name = name.lower()
        self.tel_list.append([name, number])
        print('{} Added...'.format(name))
    def rem_list(self,name):
        name = name.lower()
        for i in self.tel_list:
            if name in i:
                self.tel_list.remove(i)
                print('Removed...')
                break
            else:
                print('Can`t Find')
                break

    def view_list(self):
        if len(self.tel_list) == 0:
            print('List Empty..')
        else:
            for i in self.tel_list:
                print("""
                      Name : {}                
                      Number : {}               
                      -----------
                      """.format(i[0], i[1]))
    def search_num(self, name):
        name = name.lower()
        for i in self.tel_list:
            if name in i:
                print('{} Calling...'.format(name))
            else:
                print('Not registered!')
                
my_telephone = telephone('Samsung', 'Note5', '2015', '06543210',[])
print('''
My telephone is created..
Mark: {}
Model: {}
Manufactured Date: {}
Number: {}
Telephone List: {}
'''.format(my_telephone.mark, my_telephone.model, my_telephone.man_date,
           my_telephone.tel_num, my_telephone.tel_list))

while True:
    print('Telephone List\n 1.Add to List\n' ' 2.Remove from the List\n', '3.Call theNumber\n',
           '4.View the Telephone List\n',  '5. Cikis icin "q" ya basin!')

    operation = input('Please choose your options:')

    if operation == '1':
        name = input('Add a name: ')
        number = input('Add a number: ')
        if number.isdigit() == True:
            my_telephone.add_sb(name, number)
        else:
            print('Please just write number!')
    elif operation == '2':
        name = input('Please write the name who you want: ')
        my_telephone.rem_list(name)
    elif operation == '3':
        name = input('Please write the name of who you call: ')
        my_telephone.search_num(name)
    elif operation == '4':
        my_telephone.view_list()
    elif operation == 'q':
        print('See you later..')
        break
    else:
        print('Ooppss.. Please try again..') 
