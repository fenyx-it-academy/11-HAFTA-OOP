import time
class mobilePhone:

    def __init__(self, brand, model, imei, phone_no, ph_book):
        self.brand = brand
        self.model = model
        self.imei = imei
        self.phone_no = phone_no
        self.ph_book = ph_book

    def ShowPhoneInfo(self):
        print('Phone Brand:', self.brand, '\nPhone Model:', self.model,
              '\nIMEI No:\t', self.imei, '\nPhone No:\t', self.phone_no)

    def AddNumber(self, new_name, new_number):
        self.ph_book.update({new_name:new_number})

    def DeleteNumber(self, name):
        self.ph_book.pop(name)

    def ShowPhoneBook(self):
        print('\n')
        print('Name'.center(15), 'Phone Number'.center(20),
              '\n', f'{("-"*15)}', f'{"-"*20}')
        for k, v in self.ph_book.items():
            print('|', k.center(15), '|', v.center(20), '|', sep='')
            print(' ', f'{("-" * 15)}', ' ', f'{"-" * 20}', sep='')

    def CallNumber(self, name):
        print('Calling', f'{name}...')


phone1 = mobilePhone('Apple', 'iPhoneX', '34567812345689', '+31630564975', {})
phone2 = mobilePhone('Samsung', 'Galaxy S9', '76891278397635', '+31630830380', {})
phone3 = mobilePhone('HTC', 'One', '23456893456781', '+31630755649', {})

message1 = '\nYou have the following phones:\n\n' + \
           'p1. ' + f'{phone1.phone_no}' + '\n' + \
           'p2. ' + f'{phone2.phone_no}' + '\n' + \
           'p3. ' + f'{phone3.phone_no}' + '\n' + \
           'q   to quit.\n'
message2 = """

What would you like to do:
    1. Show phone info
    2. Show the phone book
    3. Add a phone number to the phone book 
    4. Delete a phone number from the phone book
    5. Call a number from the phone book
    6. Change phone
       Press q to quit."""
change_phone = 'n'
action = ''
while change_phone == 'n' and action != 'q':
    print(message1)
    phone = input('Please select the phone you want to proceed: ')

    if phone == 'p1':
        phone = phone1
    elif phone == 'p2':
        phone = phone2
    elif phone == 'p3':
        phone = phone3
    elif phone == 'q':
        print('\nExiting the program...')
        time.sleep(3)
        print('\nGood Bye!')
    else:
        print('Please select phone from the menu!')
        break

    while True:
        print(message2)
        action = input("\nSelect an action from the menu: ")
        if action == '1':
            phone.ShowPhoneInfo()
        elif action == '2':
            phone.ShowPhoneBook()
        elif action == '3':
            new_name = input('Enter the name of the person you want to add to the phone book: ')
            new_number = input('Enter the phone number you want to add to the phone book: ')
            phone.AddNumber(new_name, new_number)
            print('Adding', f'{new_name}', 'to the phone book...')
            time.sleep(2)
            print('Done.')
        elif action == '4':
            try:
                name_to_delete = input("Enter the name you want to delete from the phone book: ")
                phone.DeleteNumber(name_to_delete)
                print('Deleting', f'{name_to_delete}', 'from the phone book...')
                time.sleep(2)
                print('Done.')
            except KeyError:
                print('\nPlease type the name exactly you see in the phone book!')
                time.sleep(5)
        elif action == '5':
                name_to_call = input('Enter the name of the person you want to call to the phone book: ')
                phone.CallNumber(name_to_call)
                time.sleep(5)
        elif action == '6':
            change_phone = input('Would you like to change phone? ("y" for Yes, "n" for No): ').lower()
            time.sleep(1)

        elif action == 'q':
            print('\nExiting the program...')
            time.sleep(3)
            print('\nGood Bye!')
            break
