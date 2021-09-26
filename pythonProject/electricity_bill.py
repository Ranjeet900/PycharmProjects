# write a program to calculate the electricity_bill
'''
Service Number
Customer Name
Old Reading
New Reading
To find units amount
using the following conditions :-

Units           Rate                 Subcharge
<=100           0.90                 25
>100 and <=300  1.50                 35
>300 and <=500  2.75                 45
>500            4.50                 100

'''

Sno = int(input('Enter  service Number: '))
Cname = input('Enter Customer name: ')
Ore = int(input('Enter old reading: '))
Nre = int(input('Enter New reading: '))
units = int(Nre - Ore)
if units <= 100:
    amount = units*0.90
    subcharge = 25
elif units > 100 and units <= 300:
    amount = units*1.50
    subcharge = 35
elif units > 300 and units <= 500:
    amount = units*4.50
    subcharge = 45
elif units >500:
    amount = units*4.50
    subcharge = 100
net_amount  = amount + subcharge
print('Electricity Information is: ')
print('Meter no.', Sno)
print('Name of the customer:', Cname)
print('Old reading: ',Ore)
print('New reading: ',Nre)
print('Total number of units = ', units)
print('Net payable Amount: ', net_amount)






















