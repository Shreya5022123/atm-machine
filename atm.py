import time
print("please enter your card details")
time.sleep(5)
password=12345
pin=int(input("enter your atm card pin"))
balance =5000
def main_menu():
    print("""
          1==balance
          2==withdraw balance
          3==deposit balance
          4==exit""")
if pin==password:
    while True:
        main_menu()

        try:
            option=int(input("enter your choice : "))
        except ValueError:
            print("please enter valid option")
            
        if option==1:
                print(f"your current balance is {balance}")
        if option==2:
                try:
                    withdraw_amount=int(input("Please enter the withdrawal amount "))
                except:
                     print("please enter valid amount")
                     continue
                if balance>=withdraw_amount:
                    balance=balance-withdraw_amount
                    print(f"{withdraw_amount} is debited from your account")
                    print(f"your current balance is {balance}")
                else:
                    print(f"you dont have {withdraw_amount} in your account\n PLease check your acount balance")    
        if option==3:
                 try:
                    deposit_amount=int(input("Please enter the amount to deposit"))
                 except:
                      print("please enter valid amount")
                      continue
                 balance=balance+deposit_amount
                 print(f"{deposit_amount} is credited to your account")
                 print(f"your current balance is {balance}")
        if option==4:
                 break            
        
else:
    print("invalid pin.Please try again!!")
