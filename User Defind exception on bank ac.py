#1User_defined_exception.py

 

class InsufficientBalException(Exception):

    def __init__(self):

        self.message1 = 'Balance is not sufficient'

        self.message2 = 'Min Balance must be 1000'

    def disp(self):

        print ('--------------Message -------- ')       

        print (self.message1)

        print (self.message2)

        print ('--------------xxxxxxx----------')

       

sb_bank = dict()

ca_bank = dict()

#    KEY        <--- VALUES ----->

#  acc number , name , balance

sb_bank.update({1000:['Shekar Kumar',25000]})

sb_bank.update({2000:['Ananth Narayana',57000]})

sb_bank.update({3000:['Ruben Daniel',4000]})

 

print ('---main block-----')

print ('BEFORE THE TRANSACTION ')

print (sb_bank)

acc= int(input('enter the account number '))

if acc in sb_bank:

    try:

        details = sb_bank.get(acc)

        name  = details[0]

        balance = details[1]

        print ('name is ',name)

        print ('Balance is INR ',balance)

        amt = int(input('enter the amount to withdraw '))

        new_balance = balance - amt

        if (new_balance < 1000):

        #print ('balance is not sufficient ')

            raise InsufficientBalException()

        else:

            print ('TRANSACTION successful ')       

            print (new_balance)

            details[1] = new_balance

            sb_bank.update({acc:details})

    except InsufficientBalException as i:

            i.disp()

else:

    print ('no')   

 

print ('AFTER  THE TRANSACTION ')

print (sb_bank)   

 