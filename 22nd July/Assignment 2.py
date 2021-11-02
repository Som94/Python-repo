'''

if the user logs in with user id and pwd - it should allow successful login


  if user id OR pwd is wrong - then display incorrect user id or pwd

 

  if a user say a valid one - tries to login and fails for 2 times - then lock that user

 

  abc1 - user , pwd hello1 ....   abc1/ hello5  - wrong 1 attempt

                                  abc1/ xyz     - wrong 2 attempt  ....abc1 user is locked

 

  abc1 - user is locked , msg 'contact the Cust supp dept'

'''

 

def login(dict1):

    print ('enter the login id or type -1 to stop ')

    while True:

        id=int(input('login id .... '))

        if (id != -1):

            if ( id in dict1):

                pwd=input('enter the pwd ... ')

                if(dict1[id]==pwd):

                    print ('login successful ')

                else:

                    print ('login failed ...')

        else:

            break                   

                            

                

 

 

print ('i am in main BLOCK')

users = {1000: 'hello1', 2000: 'hello2', 3000:'hello3'}

print (users)

login(users)