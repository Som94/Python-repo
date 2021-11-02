'''

4.

Accept the start range and end value , use for loop to display all the number.
Except the last 20 and the first 10 (if applicable)

Example

Start number is 60

End number is 100

Then it should display from 70 to 80   (ignore the first 10 and the last 20 numbers)

 

Once 4 is working change then change it like this.

 

First 10% of the numbers of the range should not be displayed and the last 20% range of numbers should not be displayed.

Meaning convert into percentage.
'''
start_range=int(input("Enter Start range value : "))
end_range=int(input("Enter end range value : "))

for number in range(start_range+10,end_range-19):
    print(number)
    
    
total_numbers=end_range-start_range
ten_percent=total_numbers*10/100
print(10*('_'))
for number in range(start_range+int(ten_percent),end_range+1-int(ten_percent*2)):
    print(number)
    