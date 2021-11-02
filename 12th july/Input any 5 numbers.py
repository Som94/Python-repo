'''
1.
Input any 5 numbers
Check whether the number is prime or not prime

Find the count of prime numbers and non prime numbers

Example

  29

  It is prime

  36

It is not prime

And so on 5 times
'''
count_prime=0
count_not_prime=0

for i in range(5):
    
    number=int(input("Enter any number : "))
    if number >0:
        for num in range(2,number):
            if number%num==0:
                print(number,'It is not Prime')
                count_not_prime += 1
                break
        else:
            print(number,'It is Prime')
            count_prime += 1
    else:
        print("Please Enter a +ve number only ..")
        break
            
print("Inputed prime numbers are : ",count_prime, "and not prime numbers are : ",count_not_prime)






print(50*'_')

#Another way


count = 0
primeCount = 0
nonPrimeCount = 0

while True:
    if(count < 3):
        num = int(input("Enter the Number: "))
        flag = 1
        #i = 2
        if (num!= 1 and num!= 2):
            for i in range(2,num):
                if(num % i == 0):
                    flag = 0
                    break

            if(flag == 1):
                print(num,"its prime number")
                primeCount = primeCount + 1
            else:
                nonPrimeCount = nonPrimeCount + 1
                print(num,"its not prime number")
        count += 1
    else:
        break