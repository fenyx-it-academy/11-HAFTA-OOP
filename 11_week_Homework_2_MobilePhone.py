import time
class Mobile_Phone():

    def __init__(self, brand, model, production_year, number, contact_list):
        self.brand = brand
        self.model = model
        self.production_year = production_year
        self.number = number
        self.contact_list = contact_list

    def display_info(self):
        print("""
        Mobile Phone Information:

        Brand :  {}

        Model : {}

        Production Year: {}

        Number :  {}

        Contact List: {}
        """.format(self.brand, self.model, self.production_year, self.number,self.contact_list,))
    def change_attributes(self):
        while True:
            operation = input("""Please choose a operation you would like to do;
            
To change brand of mobile phone, press            "1"
To change model of mobile phone, press            "2"
To change production year of mobile phone, press  "3"
To change your telephone number, press            "4"
To exit the attribute change, press               "q"
To exit the program, press                        "e"
""")
            if operation=="1":
                print("Your mobile phone brand is: ", mobile.brand)
                new_brand=input("Please enter the new brand of your mobile phone: ")
                print("Your mobile phone brand name is changing...")
                time.sleep(3)
                mobile.brand=new_brand
                print("The new brand name of your mobile phone is: ", mobile.brand,"\n")
            elif operation=="2":
                print("Your mobile phone model is: ", mobile.model)
                new_model=input("Please enter the new model of your mobile phone: ")
                print("Your mobile phone model is changing...")
                time.sleep(3)
                mobile.model=new_model
                print("The new model of your mobile phone is: ", mobile.model,"\n")
            elif operation=="3":
                print("The production year of your mobile phone is: ", mobile.production_year)
                key=0
                while key==0:
                    new_year=input("Please enter the new production year of your mobile phone: ")
                    if new_year.isdigit() and len(new_year)==4:
                        print("The production year is changing...")
                        time.sleep(3)
                        mobile.production_year=new_year
                        print("The new production year of your mobile phone is: ", mobile.production_year,"\n")
                        key=1
                    else:
                        print("You entered an incorrect production year. Please check and enter correct year!!!\n")
                        x = 0
                        while x == 0:
                            q = input("To continue the change of production year, please press: 'ENTER'\nTo exit the changing, please press: 'q'\n")
                            if not q:
                                x = 1
                                continue
                            elif q.lower() == "q":
                                print("Changing terminated!!!\n")
                                x = 1
                                key = 1
                            else:
                                print("You entered an incorrect code. Please check and read instructions!!!\n")
                                continue
            elif operation == "4":
                print("Your telephone number is: ", mobile.number)
                key=0
                while key==0:
                    new_number = input("Please enter your new telephone number: ")
                    if new_number.isdigit():
                        print("Your telephone number is changing...")
                        time.sleep(3)
                        mobile.number = new_number
                        print("Your new telephone number is: ", mobile.number,"\n")
                        key=1
                    else:
                        print("You entered an incorrect telephone number. Please check and enter correct number!!!\n")
                        x = 0
                        while x == 0:
                            q = input("To continue the change of your telephone number, please press: 'ENTER'\nTo exit the changing, please press: 'q'\n")
                            if not q:
                                x = 1
                                continue
                            elif q.lower() == "q":
                                print("Changing terminated!!!\n")
                                x = 1
                                key=1
                            else:
                                print("You entered an incorrect code. Please check and read instructions!!!\n")
                                continue

            elif operation.lower() == "q":
                print("Attribute change terminated.\n")
                break
            elif operation.lower() == "e":
                print("The program terminated.")
                quit()
            else:
                print("You made an incorrect code. Please check and read instructions!!!\n")

    def operation_contact(self):
        while True:
            operation=input("""This is a contact list program.
Please choose a operation you would like to do;
To add a contact, press                     "1"
To delete a contact, press                  "2"
To update the contact list, press           "3"
To list the contact list, press             "4"
To call someone in the contact list, press  "5"
To exit the contact list, press             "q"
To exit the program, press                  "e"
""")
            if operation == "1":
                name=input("Please enter name and surname you would like to add.\n").lower()
                key=0
                while key==0:
                    number=input("Please enter phone number you would like to add.\n")
                    if number.isdigit():
                        if self.contact_list=={}:
                            self.contact_list[name]=number
                            key=1
                            print("New contact has been successfully added.")
                            print("Your contact list is: ",self.contact_list,"\n")
                        else:
                            for k,v in self.contact_list.items():
                                if k==name and v==number:
                                    print("The contact is already in the contact list. Please check the information!!!")
                                    key=1
                                else:
                                    self.contact_list[name]=number
                                    print("New contact has been successfully added.")
                                    print("Your contact list is: ",self.contact_list,"\n")
                                    key=1
                                    break
                    else:
                        print("Phone number must consists of only numbers!!!. Please check.")
                        x=0
                        while x==0:
                            q=input("To continue the addition, please press: 'ENTER'\nTo exit the addition, please press: 'q'\nTo exit the program, please press:'e'\n")
                            if not q:
                                x=1
                                continue
                            elif q.lower()=="q":
                                print("Addition operation terminated!!!\n")
                                x=1
                                key=1
                            elif q.lower()=="e":
                                print("Program terminated!!!\n")
                                exit()
                            else:
                                print("You entered an incorrect code. Please check and read instructions!!!\n")
                                continue
                        continue
            elif operation == "2":
                print("Your contact list is: ",self.contact_list,"\n")
                x=0
                while x==0:
                    name=input("Please enter name and surname you would like to delete.\n").lower()
                    for i in self.contact_list.keys():
                        if i == name:
                            self.contact_list.pop(name)
                            print("The name you entered has been successfully deleted.")
                            print(self.contact_list)
                            x=1
                            break
                        else:
                            print("The name you entered is not in the contact list. Please check the information!!!\n")
                            key=0
                            while key==0:
                                q=input("To continue the deletion, please press: 'ENTER'\nTo exit the deletion, please press: 'q'\nTo exit the program, please press:'e'\n")
                                if not q:
                                    key=1
                                    break
                                elif q.lower()=="q":
                                    print("Deletion operation terminated!!!\n")
                                    key=1
                                    x=1
                                    break
                                elif q.lower()=="e":
                                    print("Program terminated!!!\n")
                                    exit()
                                else:
                                    print("You entered an incorrect code. Please check and read instructions!!!\n")
                                    continue
            elif operation == "3":
                while True:
                    new=input("To update name and surname, please press '1'\nTo update phone number, please press   '2'\nTo exit the updating, please press: 'q'\nTo exit the program, please press:'e'\n")
                    try:
                        if new.lower()=="q":
                            print("Updating operation terminated!!!\n")
                            break
                        elif new.lower()=="e":
                            print("Program terminated!!!\n")
                            exit()
                        elif new == "1":
                            print("Your contact list is: ",self.contact_list,"\n")
                            name=input("Please enter name and surname you would like to update.\n").lower()
                            new_name=input("Please enter updated name and surname.\n").lower()
                            self.contact_list[new_name] = self.contact_list.pop(name)
                            print("The contact list has been successfully updated.")
                            print("Your updated contact list is:",self.contact_list,"\n")
                            continue
                        elif new=="2":
                            print("Your contact list is: ",self.contact_list,"\n")
                            name=input("Please enter name and surname you would like to update.\n").lower()
                            for i in self.contact_list.keys():
                                if i == name:
                                    new_number=input("Please enter updated phone number.\n")
                                    self.contact_list[name]=new_number
                                    print("The contact list has been successfully updated.")
                                    print("Your updated contact list is:",self.contact_list,"\n")
                                    break
                                else:
                                    print("The contact name and surname you entered is not in contact list. Please check!!!")
                                    continue
                        else:
                            print("You made an incorrect code. Please check and read instructions!!!\n")
                            continue
                    except KeyError:
                        print("The contact name and surname you entered is not in contact list. Please check!!!")
                        continue
            elif operation=="4":
                for k,v in self.contact_list.items():
                    print(f'{k}:{v}.\n')
            elif operation=="5":
                for k,v in self.contact_list.items():
                    print(f'{k}:{v}.\n')
                exit_main=0
                while exit_main==0:
                    call=input("To call by phone number, please press '1'\nTo call by name and surname '2'\n")
                    if call=="1":
                        key=0
                        while key==0:
                            call_number=input("Please enter phone number you would like to call.\n")
                            if call_number.isdigit():
                                call_number=int(call_number)
                                key = list(self.contact_list.keys())
                                value = list(self.contact_list.values())
                                if call_number in value:
                                    print(key[value.index(call_number)],"\n",call_number,"\nCalling")
                                    time.sleep(10)
                                    print(key[value.index(call_number)],"\n",call_number,"\nNot answered")
                                    call_exit = 0
                                    while call_exit == 0:
                                        q = input("To make a another phone call, please press: 'ENTER'\nTo exit the phone call, please press: 'q'\n")
                                        if not q:
                                            call_exit = 1
                                            key = 0
                                        elif q.lower() == "q":
                                            print("Phone Call terminated!!!\n")
                                            call_exit = 1
                                            key = 1
                                            exit_main=1
                                        else:
                                            print("You entered an incorrect code. Please check and read instructions!!!\n")
                                            continue
                                else:
                                    print("The phone number is not in contact list. Please check!!!")
                                    call_exit = 0
                                    while call_exit == 0:
                                        q = input("To continue the phone call, please press: 'ENTER'\nTo exit the phone call, please press: 'q'\n")
                                        if not q:
                                            call_exit = 1
                                            key=0
                                        elif q.lower() == "q":
                                            print("Phone Call terminated!!!\n")
                                            call_exit = 1
                                            key=1
                                            exit_main=1
                                        else:
                                            print("You entered an incorrect code. Please check and read instructions!!!\n")
                                            continue
                            else:
                                print("The phone number you entered is not correct. Please check!!!")
                                call_exit = 0
                                while call_exit == 0:
                                    q = input("To continue the phone call, please press: 'ENTER'\nTo exit the phone call, please press: 'q'\n")
                                    if not q:
                                        call_exit = 1
                                        key = 0
                                    elif q.lower() == "q":
                                        print("Phone Call terminated!!!\n")
                                        call_exit = 1
                                        key = 1
                                        exit_main=1
                                    else:
                                        print("You entered an incorrect code. Please check and read instructions!!!\n")
                                        continue
                    elif call=="2":
                        key=0
                        while key==0:
                            name=input("Please enter name and surname you would like to call.\n").lower()
                            key = list(self.contact_list.keys())
                            if name in key:
                                print(name,"\n",self.contact_list[name],"\nCalling")
                                time.sleep(10)
                                print(name,"\n",self.contact_list[name],"\nNot answered")
                            else:
                                print("The contact name and surname you entered is not in contact list. Please check!!!")
                            call_exit = 0
                            while call_exit == 0:
                                q = input("To continue the phone call or to make another phone call, please press: 'ENTER'\nTo exit the phone call, please press: 'q'\n")
                                if not q:
                                    call_exit = 1
                                    key = 0
                                elif q.lower() == "q":
                                    print("Phone Call terminated!!!\n")
                                    call_exit = 1
                                    key = 1
                                    exit_main=1
                                else:
                                    print("You entered an incorrect code. Please check and read instructions!!!\n")
                                    continue
                    else:
                        print("You entered an incorrect code. Please check and read instructions!!!\n")
                        call_exit=0
                        while call_exit == 0:
                            q = input("To continue the phone call, please press: 'ENTER'\nTo exit the phone call, please press: 'q'\n")
                            if not q:
                                call_exit = 1
                                exit_main = 0
                            elif q.lower() == "q":
                                print("Phone Call terminated!!!\n")
                                call_exit = 1
                                exit_main = 1
                            else:
                                print("You entered an incorrect code. Please check and read instructions!!!\n")
                                continue

            elif operation.lower() == "q":
                print("Contact list terminated.")
                break
            elif operation.lower() == "e":
                print("Program terminated.")
                exit()
            else:
                print("You made an incorrect code. Please check and read instructions!!!\n")
mobile=Mobile_Phone("Iphone","X",2017,6586445,{"ufuk doymaz":123456,"a rıza":789456,"f kesir":546151,"f yılmaz":845431})
while True:
    operation=input("""This is a mobile phone program.
Please choose a operation you would like to do;

To display the attributes of mobile phone, press    "1"
To change the attributes of mobile phone, press     "2"
For contact list operation, press                   "3"
To exit the program, press                          "e"
""")
    if operation=="1":
        mobile.display_info()
        continue
    elif operation=="2":
        mobile.change_attributes()
    elif operation=="3":
        mobile.operation_contact()
    elif operation.lower() == "e":
        print("Program terminated.")
        break
    else:
        print("You made an incorrect code. Please check and read instructions!!!\n")
