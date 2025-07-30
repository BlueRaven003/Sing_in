'''

'''
import random
import string



class sing_in:

    def __init__(self):
        self.User=[]

    def is_user_name(self,name):
        if name[0].isalpha():                         
            for names in self.User:
                n=names['name']
                if n.lower() == name.lower():
                    return False 
            else:
                return True
        return False        

    def is_gmail(self,gmail):
        if gmail.endswith('@gmail.com'):
            return True
        else :
            return False

    def is_password(self,password):
        if len(password) >= 8 :
            return True
        return False

    def random_string(self,length):
        characters = string.ascii_letters + string.digits
        random_string=''.join(random.choice(characters)for _ in range(length))
        return random_string
    def add_to_list(self,name,gmail,password):
        self.User.append({'name':name,'gmail':gmail,'password':password})
        print('created account succesfully!')
        
        
    def print_user_list(self):
        for account in self.User:
            print('\n name='+account['name'],  'Gmail='+account['gmail'])

sing=sing_in()

while True:
    command=input('1.sing_in 2.exit : ')
    if command=='1':

        while True:
            name=input('Enter your user_name : ')
            if sing.is_user_name(name):
                break 
            else :
                print('this name has already been used! or name is wrong!')

        while True:       
            gmail=input('Enter your gmail : ')
            if sing.is_gmail(gmail) :
                break
            else :
                r=sing.random_string(length=8)
                txt=('Gmail is wrong!(Example: {random_str:}@gmail.com)')
                print(txt.format(random_str=r))

        while True:
            command=input('1.create_password  2.random_password : ')
            if command=='1':
                password=input('Enter your password : ')
                if sing.is_password(password):
                    break
                else:
                    print('password is wrong!')
                    continue
            elif command=='2':
                password=sing.random_string(length=10)
                print('this is your password : ',password)
                break
            else :
                print('invalid command!')

        sing.add_to_list(name,gmail,password)
        
    elif command=='2' :
        print('Exiting...')
        break
    else:
        print('invalid command!')

    
all_user=len(sing.User)
print('all_user = ',all_user)
sing.print_user_list()
                


