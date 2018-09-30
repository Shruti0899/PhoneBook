
print("______________________________________MY OWN PHONEBOOK_________________________________________________")

class phnbook:

    def __init__(self):
        self.phnbk={}
        self.menu()

    def delc(self,phnbk):
        self.name=input("Name:")
        if self.name not in self.phnbk:
            print("Contact does not exit or already has been deleted\n")
        else:
            del self.phnbk[self.name]
            print("\n Contact deleted")
            print("\n Want to delete more contacts?Y/N")
            ch=input()
            if ch=="y":
                  self.delc(phnbk)
            elif ch=='n':
                  print("Phonebook",self.phnbk)
            else:
                pass

    def searchc(self,phnbk):
        print("Enter the name:\n")
        self.contact=input()
        if self.contact in self.phnbk:
            print(self.phnbk[self.contact])
        else:
            print("\nContact not found")

    def editc(self,phnbk):
        self.name=input("Name:")
        if self.name in self.phnbk:
            del self.phnbk[self.name]
            print("\nRe-enter the deatils\n")
            self.adc(self.phnbk)
        else:
            print("\n Contact not found")
            
    def adc(self,phnbk):
        self.name=input("Name:")
        self.phno=input("Phone Number:")
        self.id=input("Email id")
        
        if self.name not in self.phnbk:
            print("hi")
            self.phnbk[self.name]={}
            if len(self.phno)==10 and "@" in self.id:
                self.phnbk[self.name]["Number"]=self.phno
                self.phnbk[self.name]["Email id"]=self.id
                print("\nPhone Book",self.phnbk)
            else:
                print("\nInvalid Entries.\nRe-enter the details\n")
                self.adc(phnbk)
            print("\n Want to add more contacts?Y/N")
            ch=input()
            if ch=="y":
                  self.adc(phnbk)
            elif ch=='n':
                  print("Phonebook",self.phnbk)
        else:
            print("\n Contact already exists.\n")
            print(self.phnbk[self.name])
            print("Do you want to edit or delete this contact? D/E")
            ch=input()
            if ch=='d':
                self.delc(phnbk)
            elif ch=='e':
                self.editc(phnbk)
            else:
                pass
                
                   
    def menu(self):
        
        print("\n Choose an option from below\n")
        print("\n 1.Add a Contact\n2.Delete a Contact\n3.Search a Contact\n4.Edit a Contact\n5.Exit\n")
        op=input()
        if op=="1":
            self.adc(self.phnbk)
            self.menu()
        elif op=="2":
            self.delc(self.phnbk)
            self.menu()
        elif op=="3":
            self.searchc(self.phnbk)
            self.menu()
        elif op=='4':
            self.editc(self.phnbk)
            self.menu()
        elif op=='5':
            exit()

        else:
            print("Invalid option")
myob=phnbook()
            
        
        
