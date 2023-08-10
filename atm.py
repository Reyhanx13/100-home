class Atm:
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
        

    def withdrawl(self):
        print("enter amount")

    def BalanceEnquiry(self):
        print("your current balance is :")

    def Chequedeposits(self):
        print("enter amount in recreipt")

    def Transferfunds(self):
        print("fund is transfer")
    
atm=Atm("0921 5988 8626 8518","7645") 
print(atm.Chequedeposits)   

    
