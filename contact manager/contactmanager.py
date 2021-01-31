class contact:
    def __init__(self,name,contactNo):
        self.name = name
        self.contactNo = [contactNo]
    
def get_name(self):
    return self.name

print('Actions')
print("1. Make new contact")
print("2. Add to existing contact")
print('3. Search a contact')
print('4. Delete a content')

contactList = []
contactList.sort()
while(1):
    action = input('Action: ')
    if int(action)==1:
        name = input("Enter Name: ")
        contactNo = input("Contact No: ")
        if(len(contactNo)!=10):
            print("The given contact number is not valid please try again")
        else:
            obj = contact(name,int(contactNo))
            contactList.append(obj)
            contactList = sorted(contactList, key=get_name)

    elif int(action)==2:
        flag =0 
        name = input("Enter Name: ")
        for obj in contactList:
            if obj.name == name:
                contactNo = input('Contact Number:')
                obj.contactNo.append(int(contactNo))
                flag = 1
                break
        if flag == 0:
            print('Contact Name does not exist')
    
    elif int(action) == 3:
        subString = input('Substring: ')
        count = 0
        contactWithSubstring = []
        for obj in contactList:
            if subString in obj.name:
                contactWithSubstring.append(obj)
                print(obj.name)
                count = count + 1
        if count > 0:
            index = input('Choose index of the required Contact: ')
            print(contactWithSubstring[int(index)].name, contactNo)

        else:
            print("The given substring was not found")
    
    elif int(action) ==4:
        flag =0 
        count =0 
        name = input("Enter the Contact name that you wish to delete: ")
        for obj in contactList:
            if obj.name == name:
                contactList.pop(count)
                flag = 1
                break
            count=count+1
        if flag == 0:
            print('Contact Name does not exist')
    else:
        break

for obj in contactList:
    print(obj.name,obj.contactNo)