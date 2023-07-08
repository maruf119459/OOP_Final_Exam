class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.list_user = []
        self.balance = 0
        self.lon = 0
        self.lon_status = 'yes'

        self.admin_list = []
        pass

    def add_blance(self, amount):
        self.balance += amount
    
    def view_user(self):
        for user in self.list_user:
            print(user)   

class User:
    def __init__(self, name) -> None:
        self.name = name
        self.primary_blance = 0
        self.user_blance = 0
        self.lon = 0
        self.Transaction_history = []
    
    def create_an_account(self,phone,address,amount,Bank):
        self.phone = phone
        self.address = address
        self.user_blance += amount
        self.primary_blance += amount
        Bank.balance += amount
        self.id = len(Bank.list_user) + 2023100
        man = {'Name':self.name, 'Id':self.id, 'Phone':self.phone, 'Address':self.address,'Primary_blance':self.primary_blance,'Blance':self.user_blance,'Lon':self.lon,}
        Bank.list_user.append(man)
        history = {'1st_Deposit':amount}
        self.Transaction_history.append(history)
        print('Congratulations! Your account creation is complete. Your 1st deposit amount : ',amount)

    def deposit(self,amount,Bank):
        if amount > 0:
            self.user_blance += amount
            self.primary_blance += amount
            for user in Bank.list_user:
                if user['Name'] == self.name:
                    user['Primary_blance'] += amount
                    user['Blance'] += amount
            Bank.balance += amount
            history = {'Deposit':amount}
            self.Transaction_history.append(history)
            print('Thanks for deposit.You diposot amount : ',amount)
        
        else:
            print('Invalid amount!  Please enter valid amount.')

    def withdrawal(self,amount,Bank):
        if Bank.balance >= amount:
            if amount > 0 and self.user_blance > 0 and self.user_blance >= amount:
                if self.primary_blance > 0 and self.primary_blance >= amount:
                    self.primary_blance -= amount
                    self.user_blance -= amount
                    for user in Bank.list_user:
                        if user['Name'] == self.name:
                             user['Primary_blance'] -= amount
                             user['Blance'] -= amount
                    print('Thanks for withdrawal.You withdrawal amount : ',amount,'\nYour Blance: ',self.user_blance)
                    
                elif self.user_blance >= amount:
                    self.user_blance -= amount
                    for user in Bank.list_user:
                        if user['Name'] == self.name:
                            user['Blance'] -= amount
                    print('Thanks for withdrawal.You withdrawal amount : ',amount,'\nYour Blance: ',self.user_blance)
                       
                Bank.balance -= amount
                history = {'Withdrawal':amount}
                self.Transaction_history.append(history)
            else:
                print('Invalid amount! Please enter valid amount.')
        else:
            print('The bank is bankrupt')


    def available_balance(self):
        print(f'Available Primary Balance:    {self.primary_blance}\nAvailable Balance        :    {self.user_blance}')
    

    def transfer_amount(self,to_user2, Bank , amount):
        if amount > 0 and (self.user_blance >= amount or self.primary_blance >= amount):
            if self.primary_blance >= amount:
                self.user_blance -= amount
                self.primary_blance -= amount

                to_user2.user_blance += amount
                to_user2.primary_blance += amount
                for user in Bank.list_user:
                    if user['Name'] == self.name:
                        user['Blance'] -= amount
                        user['Primary_blance'] -= amount
                for user in Bank.list_user:
                    if user['Name'] == to_user2.name:
                        user['Primary_blance'] += amount
                        user['Blance'] += amount
                print('Complete transfer amount!')
                history = {'transfer_amount':amount}
                self.Transaction_history.append(history)
            elif self.user_blance >= amount:
                self.user_blance -= amount

                to_user2.user_blance += amount
                to_user2.primary_blance += amount
                for user in Bank.list_user:
                    if user['Name'] == self.name:
                        user['Blance'] -= amount
        
                for user in Bank.list_user:
                    if user['Name'] == to_user2.name:
                        user['Primary_blance'] += amount
                        user['Blance'] += amount
                print('Complete transfer amount!')
                history = {'transfer_amount':amount}
                self.Transaction_history.append(history)
            else:
                print('Sorr! Can not transfer amount')
        else:  
            print('Sorr! Can not transfer amount')      
            
    def take_loan(self, amount, Bank): #lon status niye kahini
        if amount <= self.primary_blance*2 and Bank.lon_status == 'yes' and amount > 0:
            self.user_blance += amount
            self.lon += amount
            Bank.lon += amount
            Bank.balance -= amount
            for user in Bank.list_user:
                if user['Name'] == self.name:
                    user['Blance'] += amount
                    user['Lon'] += amount
            history = {'Lon':amount}
            self.Transaction_history.append(history)
            print('Your lon activet.You get ',amount,' lon.')
        elif Bank.lon_status == 'no':
            print('lon Status: Off.')
        else:
            print('You are not able to get lon')
    
    def pay_lon(self,amount,Bank):
        if amount > 0 :
            self.lon -= amount
            Bank.lon -= amount
            for user in Bank.list_user:
                if user['Name'] == self.name:
                    user['Lon'] -= amount
            history = {'Pay_Lon':amount}
            self.Transaction_history.append(history)
            print('Thanks for pay lon. Your remaining lon: ',self.lon)
        else:
            print('Invalid amount!\n Please enter valide amount.')

    def transaction_history(self):
        print('Your transaction history: ')
        for history in self.Transaction_history:
            print(history)

class Admin:
    def __init__(self,name) -> None:
        self.name = name

    def create_admin_account(self,phone,address,Bank):
        self.phone = phone
        self.address = address
        self.id = len(Bank.admin_list) + 2023501
        admin = {'Name':self.name, 'Id':self.id,'Phone':self.phone,'Address':self.address}
        Bank.admin_list.append(admin)
    
    def available_balance(sel,Bank):
        print(f'Available balance in bank:   {Bank.balance}')
    
    def total_loan(self,Bank):
        print(f'Total Loan amount: {Bank.lon}')

    def on_loan_feature(self,Bank):
        Bank.lon_status = 'yes'
    
    def off_lon_feature(self,Bank):
        Bank.lon_status = 'no'

from User import User
from Admin import Admin
from Bank import Bank

def main():
    city_bank = Bank('City Bank')
    Maruf = User('Maruf')
    Maruf.create_an_account(8801716534217,'Dhaka Bangladesh',1000,city_bank)
    Maruf.deposit(10000,city_bank)
    Sakib = User('Sakib')
    Sakib.create_an_account(8801827183421, 'Pabna Bangladesh', 500, city_bank)
    Sakib.deposit(50000,city_bank)
    Sakib.take_loan(1000,city_bank)

    Maruf.withdrawal(500,city_bank)
    Maruf.take_loan(1000,city_bank)
    Maruf.take_loan(1000000,city_bank)

    Sun = Admin('Sun')
    Sun.create_admin_account(8801302033512,'Pabna Bangladesh',city_bank)
    Sun.available_balance(city_bank)

    Don = User('Don')
    Don.create_an_account(8801374023487,'London England',5000,city_bank)

    Sun.off_lon_feature(city_bank)

    Don.take_loan(2000,city_bank)

    Sakib.pay_lon(500,city_bank)

    Sakib.transfer_amount(Don,city_bank,5000)
    
    Sakib.transaction_history()

    Sun.total_loan(city_bank)


    #-------------------------------------------------------
    city_bank.view_user()


if __name__ == '__main__':
    main()
