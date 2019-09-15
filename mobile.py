class Mobile_phone():
    def __init__(self,brand="IPhone",model="X",manufacturing=2019,mobile_no=68268262):
        self.brand = brand
        self.model = model
        self.manufacturing = manufacturing
        self.mobile_no = mobile_no
        self.directory = {}

    def add_name(self, name, number):
        word_list = name.split()
        for n in word_list:
            if n.isalpha() == False:
                print("You can add only name.")
            else:
                self.directory[name] = number
                print(f"Person {name} was added.")
                break
        
    def remove_name(self, name):
        if name in self.directory.keys():
            self.directory.pop(name)
            print(f"Person {name} was removed.")
        else:
            print(f"{name} could not be found")
            
    def show_directory(self):
        for name, number in self.directory.items():
            print(name.ljust(20),":",number)
            
    def call_number(self, name):
        if name in self.directory.keys():
            print("calling")
        else:
            print(f"{name} could not be found")
    
mobile1 = Mobile_phone()  
mobile1.add_name("123",123123)
mobile1.add_name("mehmet kurt",123123124)
mobile1.remove_name("ahmet")
mobile1.show_directory()
mobile1.call_number("mehmet yilmaz")
mobile1.call_number("mehmet kurt")

