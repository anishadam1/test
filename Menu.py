'''while True:
    choice = eval(input("""
    1 - Option 1,
    2 - Option 2, 
    3 - Option 3, 
    Enter choice: """))
    if choice == 1:
            print ("You chose option 1.")
    elif choice == 2:
            print ("You chose option 2.")
    elif choice == 3:
            print ("You chose option 3.")
    else:
            print ("Error. Enter 1, 2, or 3.")'''



find = open('mbox.txt')
count = 0
'''for line in find:
    print(line)
    count+=1
print('Line Count:',count)'''

'''int = find.read()
print(int)
print('Number of characters:',len(int))
print(int[:20])'''

'''for line in find:
    if line.startswith('From:'):
        print(line)'''

'''for line in find:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)'''
newtotal = 0
total = 0
BEEF = 5.75
BEYOND = 6.25
DOUBLE = 2
TRIPLE = 3.5
CHEESE = 0.50
BACON = 1.25
AVOCADO = 0.75
CHILLI = 2.50
FRIES = 2
ONION_RINGS = 2.25
pattyinput = input("Please choose beef(B) or beyond beef(Y):")
while pattyinput.upper()!= 'B'and pattyinput.upper()!='Y':
    pattyinput = input("Please choose beef(B) or beyond beef(Y):")

#while True:
    #pattyinput = input("Please choose beef(B) or beyond beef(Y):")
    if pattyinput.upper()=='B' or pattyinput.upper()=='Y':
        if pattyinput.upper()=='B':
            newtotal+=BEEF+total
        if pattyinput.upper()=='Y':
            newtotal+=BEYOND+total
        additional = input("Would you like to make it a double(D) or triple(T)? or N:")
    if additional.upper()=='D' or additional.upper()=='T' or additional.upper()=='N':
        toppings = input('Would you like to add toppings? Y or N:')
        if additional.upper() == 'D':
            newtotal += DOUBLE + total
        if additional.upper() == 'T':
            newtotal += TRIPLE + total
        if additional.upper() == 'N':
            newtotal + total
    if toppings.upper() == 'Y':
        cheese = input('Would you like cheese? (Y or N):')
        if cheese.upper() == 'Y':
            newtotal += CHEESE + total
        if cheese.upper() == 'N':
            newtotal
        bacon = input('Would you like bacon? (Y or N):')
        if bacon.upper() == 'Y':
            newtotal += BACON
        if bacon.upper() == 'N':
            newtotal + total
        avocado = input('Would you like avocado? (Y or N):')
        if avocado.upper() == 'Y':
            newtotal += AVOCADO + total
        if avocado.upper() == 'N':
            newtotal + total
        chili = input('Would you like cheese? (Y or N):')
        if chili.upper() == 'Y':
            newtotal += CHILLI + total
        if chili.upper() == 'N':
            newtotal + total
    sides = input('Would you like Fries(F) or Onion Rings(R)? or N:')
    if sides.upper() == 'F':
        newtotal += FRIES + total
    if sides.upper() == 'R':
        newtotal += ONION_RINGS + total
    if sides.upper() == 'N':
        newtotal + total

    print('Order Summary:')
    print('===============')
    print(f'Order total: ${newtotal:.2f}')

    enter = input('Press ENTER to continue, Q to quit:')
    if enter.upper() == 'Q':
        grandtotal = newtotal + total
        print(grandtotal)
        break
# grandtotal = newtotal+total
# print(grandtotal)

num = 3
row = 0
while row < num:
    star = row + 1
    while star > 0:
        print("*", end='')
        star = star - 1
    row = row + 1
    print()

print("===============Today's Sales Report===============")
length = 3
for i in range(0, length):
    for j in range(0, length - i):
        print("*" + "", end='')
    print()

print("==================================================")