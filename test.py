"""
Leaf Year Conditions :
01. Year Divide by 400
02. Year cannot Divide by 100 and divide by 4
"""
print('Enter your year :')

year = int(input())
status = 'null'

if year % 400 == 0:
    status = 'true'
elif year % 100 > 0 and year % 4 == 0:
    status = 'true'
else:
    status = 'false'

if status == 'true':
    print('Leaf Year')
else:
    print('Not Leaf Year')





