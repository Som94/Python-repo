#Demo_concepts.py

 

class Calc:

    def __init__(self,n,m):

        self.n = n

        self.m = m

    def get_total(self):

        return self.n + self.m

    def print_total(self):

        t = self.get_total()

        print ('Total of ',self.n,' and ',self.m,' is ',t)

       

class ApplyBussRule:

    def __init__(self,n,m):

        self.n = n

        self.m = m

       

    def do_validation(self):

        number_n_IS_NOT_IN_RANGE=(n > 999 or n < 100)

        number_m_IS_NOT_IN_RANGE=(m > 999 or m < 100)

           

        if (number_n_IS_NOT_IN_RANGE):

            return 1

        elif  (number_m_IS_NOT_IN_RANGE):

            return 2

        else:

            return 3

           

class NonThreeDigitNumberException(Exception):

    def __init__(self,numb):

        self.numb=numb

       

    def err_msg(self):       

        print ('it is not THREE digit number. You inputted ',self.numb)

 

tup1 = ((45,256),(232,27),('13',424),(890,'125'),(500,400))       

#tup1 = ((145,256),(232,227),('130',424),(890,'125'),(500,400))       

#n,m  = input ('any 2 THREE digit number to be inputted ').split(',')

for i in tup1:

    n = i[0]

    m = i[1]

    try:

        n = int(n)

        m = int(m)

        try:

            obj_buss_rule = ApplyBussRule(n,m)

            there_is_issue = obj_buss_rule.do_validation()

            if (there_is_issue==1):

                objMsg = NonThreeDigitNumberException(n)

                raise objMsg

            elif (there_is_issue==2):

                objMsg = NonThreeDigitNumberException(m)

                raise objMsg

               

            obj_calc = Calc(n,m)

            obj_calc.print_total()

            ttl = obj_calc.get_total()

            print ('Brother total of the numbers is ',ttl)

            print ('---------')

        except NonThreeDigitNumberException:

            objMsg.err_msg()

       

    except  ValueError:

        print ('Hello friend you have inputted a NON-NUMERIC value')

        print ('Please input proper value')

    finally:

        pass

#        print ("---------------------****-----------------")       

#        print ("thank you for using this program. Have a good day.")

#        print ("---------------------****-----------------")       

# want to the THREE digit numbers and display the total

# raise an exception if it is not THREE digit number